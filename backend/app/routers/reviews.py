import math

from fastapi import APIRouter, Query

from app.database import find_all
from app.schemas import ApiResponse, Pagination, ReviewDistribution, ReviewList, ReviewOut, ReviewSummary

router = APIRouter(tags=["reviews"])


@router.get("/products/{product_id}/reviews", response_model=ApiResponse[ReviewList])
async def get_reviews(
    product_id: int,
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=50),
):
    all_reviews = find_all("reviews", product_id=product_id)
    all_reviews.sort(key=lambda r: r.get("created_at", ""), reverse=True)

    total = len(all_reviews)
    total_pages = math.ceil(total / page_size) if total > 0 else 0
    start = (page - 1) * page_size
    page_items = all_reviews[start:start + page_size]

    # Distribution
    dist = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    for r in all_reviews:
        rating = r.get("rating", 0)
        if rating in dist:
            dist[rating] += 1

    average = round(sum(r.get("rating", 0) for r in all_reviews) / total, 1) if total > 0 else 0.0

    items = [
        ReviewOut(
            id=r["id"],
            user_name=r["user_name"],
            rating=r["rating"],
            title=r["title"],
            content=r["content"],
            date=r.get("created_at", "")[:10],
        )
        for r in page_items
    ]

    return ApiResponse(
        data=ReviewList(
            items=items,
            pagination=Pagination(page=page, page_size=page_size, total=total, total_pages=total_pages),
            summary=ReviewSummary(
                average=average,
                distribution=ReviewDistribution(
                    star_5=dist[5],
                    star_4=dist[4],
                    star_3=dist[3],
                    star_2=dist[2],
                    star_1=dist[1],
                ),
            ),
        )
    )
