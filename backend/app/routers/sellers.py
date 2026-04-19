from fastapi import APIRouter, Depends
from sqlalchemy import func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.database import get_db
from app.models import Product, Seller
from app.schemas import ApiResponse, SellerDetail

router = APIRouter(tags=["sellers"])


@router.get("/sellers/{seller_id}", response_model=ApiResponse[SellerDetail])
async def get_seller(seller_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Seller).where(Seller.id == seller_id))
    seller = result.scalar_one_or_none()

    if not seller:
        return ApiResponse(code=404, data=None, message=f"Seller with id {seller_id} not found")

    count_result = await db.execute(select(func.count(Product.id)).where(Product.seller_id == seller_id))
    product_count = count_result.scalar() or 0

    return ApiResponse(
        data=SellerDetail(
            id=seller.id,
            name=seller.name,
            is_official=seller.is_official,
            reputation=seller.reputation,
            location=seller.location,
            logo_url=seller.logo_url,
            product_count=product_count,
            created_at=seller.created_at.isoformat() if seller.created_at else "",
        )
    )
