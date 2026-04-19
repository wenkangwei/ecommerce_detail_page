import math

from fastapi import APIRouter, Depends, Query
from sqlalchemy import func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.database import get_db
from app.models import Review
from app.schemas import ApiResponse, Pagination, ReviewDistribution, ReviewList, ReviewOut, ReviewSummary

router = APIRouter(tags=["reviews"])


@router.get("/products/{product_id}/reviews", response_model=ApiResponse[ReviewList])
async def get_reviews(
    product_id: int,
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=50),
    db: AsyncSession = Depends(get_db),
):
    query = select(Review).where(Review.product_id == product_id).order_by(Review.created_at.desc())
    count_query = select(func.count(Review.id)).where(Review.product_id == product_id)

    total_result = await db.execute(count_query)
    total = total_result.scalar() or 0
    total_pages = math.ceil(total / page_size)

    query = query.offset((page - 1) * page_size).limit(page_size)
    result = await db.execute(query)
    reviews = result.scalars().all()

    # Compute distribution
    dist_query = select(Review.rating, func.count(Review.id)).where(Review.product_id == product_id).group_by(Review.rating)
    dist_result = await db.execute(dist_query)
    dist_rows = dict(dist_result.all())

    avg_query = select(func.avg(Review.rating)).where(Review.product_id == product_id)
    avg_result = await db.execute(avg_query)
    average = round(avg_result.scalar() or 0, 1)

    items = [
        ReviewOut(
            id=r.id,
            user_name=r.user_name,
            rating=r.rating,
            title=r.title,
            content=r.content,
            date=r.created_at.isoformat()[:10] if r.created_at else "",
        )
        for r in reviews
    ]

    return ApiResponse(
        data=ReviewList(
            items=items,
            pagination=Pagination(page=page, page_size=page_size, total=total, total_pages=total_pages),
            summary=ReviewSummary(
                average=average,
                distribution=ReviewDistribution(
                    star_5=dist_rows.get(5, 0),
                    star_4=dist_rows.get(4, 0),
                    star_3=dist_rows.get(3, 0),
                    star_2=dist_rows.get(2, 0),
                    star_1=dist_rows.get(1, 0),
                ),
            ),
        )
    )
