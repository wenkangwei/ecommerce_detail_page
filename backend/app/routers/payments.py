from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.database import get_db
from app.models import PaymentMethod
from app.schemas import ApiResponse, PaymentMethodOut

router = APIRouter(tags=["payments"])


@router.get("/payment-methods", response_model=ApiResponse[list[PaymentMethodOut]])
async def list_payment_methods(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(PaymentMethod).order_by(PaymentMethod.sort_order))
    methods = result.scalars().all()

    return ApiResponse(
        data=[
            PaymentMethodOut(
                id=m.id,
                name=m.name,
                type=m.type,
                icon_url=m.icon_url,
                max_installments=m.max_installments,
            )
            for m in methods
        ]
    )
