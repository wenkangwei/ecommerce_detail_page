from fastapi import APIRouter

from app.database import find_by_id, get_collection
from app.schemas import ApiResponse, SellerDetail

router = APIRouter(tags=["sellers"])


@router.get("/sellers/{seller_id}", response_model=ApiResponse[SellerDetail])
async def get_seller(seller_id: int):
    seller = find_by_id("sellers", seller_id)

    if not seller:
        return ApiResponse(code=404, data=None, message=f"Seller with id {seller_id} not found")

    product_count = len([p for p in get_collection("products") if p.get("seller_id") == seller_id])

    return ApiResponse(
        data=SellerDetail(
            id=seller["id"],
            name=seller["name"],
            is_official=seller.get("is_official", False),
            reputation=seller.get("reputation", ""),
            location=seller.get("location", ""),
            logo_url=seller.get("logo_url", ""),
            product_count=product_count,
            created_at=seller.get("created_at", ""),
        )
    )
