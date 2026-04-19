from fastapi import APIRouter

from app.database import get_collection
from app.schemas import ApiResponse, PaymentMethodOut

router = APIRouter(tags=["payments"])


@router.get("/payment-methods", response_model=ApiResponse[list[PaymentMethodOut]])
async def list_payment_methods():
    methods = sorted(get_collection("payment_methods"), key=lambda m: m.get("sort_order", 0))

    return ApiResponse(
        data=[
            PaymentMethodOut(
                id=m["id"],
                name=m["name"],
                type=m["type"],
                icon_url=m.get("icon_url", ""),
                max_installments=m.get("max_installments", 1),
            )
            for m in methods
        ]
    )
