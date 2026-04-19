import math

from fastapi import APIRouter, Depends, Query
from sqlalchemy import func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload

from app.database import get_db
from app.models import Product
from app.schemas import (
    ApiResponse,
    CategoryItem,
    InstallmentInfo,
    Pagination,
    ProductDetail,
    ProductImageOut,
    ProductList,
    ProductListItem,
    ProductSpecOut,
    SellerBrief,
)

router = APIRouter(tags=["products"])


def _compute_discount(original: float, current: float) -> int:
    if original <= 0:
        return 0
    return int(round((1 - current / original) * 100))


def _product_to_detail(p: Product) -> ProductDetail:
    discount = _compute_discount(p.original_price, p.price)
    installment_count = 10
    installment_amount = round(p.price / installment_count, 2)

    category_path = []
    if p.category:
        category_path.append(CategoryItem(id=1, name=p.category, slug=p.category.lower().replace(" ", "-")))
    if p.subcategory:
        category_path.append(CategoryItem(id=2, name=p.subcategory, slug=p.subcategory.lower().replace(" ", "-")))

    specs = [ProductSpecOut(key=s.spec_key, value=s.spec_value) for s in p.specs]

    seller_brief = SellerBrief(
        id=p.seller.id,
        name=p.seller.name,
        is_official=p.seller.is_official,
        reputation=p.seller.reputation,
        location=p.seller.location,
        logo_url=p.seller.logo_url,
    )

    return ProductDetail(
        id=p.id,
        title=p.title,
        description=p.description,
        price=p.price,
        original_price=p.original_price,
        currency=p.currency,
        discount_percentage=discount,
        category=p.category,
        subcategory=p.subcategory,
        stock=p.stock,
        rating_avg=p.rating_avg,
        rating_count=p.rating_count,
        free_shipping=p.free_shipping,
        warranty_months=p.warranty_months,
        installments=InstallmentInfo(count=installment_count, amount=installment_amount),
        category_path=category_path,
        seller=seller_brief,
        images=[ProductImageOut(id=img.id, url=img.url, alt_text=img.alt_text) for img in p.images],
        specs=specs,
    )


@router.get("/products", response_model=ApiResponse[ProductList])
async def list_products(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=50),
    category: str | None = None,
    db: AsyncSession = Depends(get_db),
):
    query = select(Product).options(selectinload(Product.images))
    count_query = select(func.count(Product.id))

    if category:
        query = query.where(Product.category == category)
        count_query = count_query.where(Product.category == category)

    total_result = await db.execute(count_query)
    total = total_result.scalar() or 0

    total_pages = math.ceil(total / page_size)
    query = query.offset((page - 1) * page_size).limit(page_size)
    result = await db.execute(query)
    products = result.scalars().unique().all()

    items = []
    for p in products:
        thumb = p.images[0].url if p.images else ""
        items.append(
            ProductListItem(
                id=p.id,
                title=p.title,
                price=p.price,
                currency=p.currency,
                thumbnail=thumb,
                category=p.category,
                rating_avg=p.rating_avg,
                rating_count=p.rating_count,
                free_shipping=p.free_shipping,
            )
        )

    return ApiResponse(
        data=ProductList(
            items=items,
            pagination=Pagination(page=page, page_size=page_size, total=total, total_pages=total_pages),
        )
    )


@router.get("/products/{product_id}", response_model=ApiResponse[ProductDetail])
async def get_product(product_id: int, db: AsyncSession = Depends(get_db)):
    query = (
        select(Product)
        .where(Product.id == product_id)
        .options(selectinload(Product.seller), selectinload(Product.images), selectinload(Product.specs))
    )
    result = await db.execute(query)
    product = result.scalar_one_or_none()

    if not product:
        return ApiResponse(code=404, data=None, message=f"Product with id {product_id} not found")

    return ApiResponse(data=_product_to_detail(product))
