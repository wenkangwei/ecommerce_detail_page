import math

from fastapi import APIRouter, Query

from app.database import find_all, find_by_id, get_collection
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


def _make_product_detail(p: dict) -> ProductDetail:
    """Assemble a full product detail from flat JSON data."""
    price = p["price"]
    original = p["original_price"]
    discount = int(round((1 - price / original) * 100)) if original > 0 else 0
    installment_count = 10
    installment_amount = round(price / installment_count, 2)

    # Resolve seller
    seller_raw = find_by_id("sellers", p["seller_id"])
    seller = SellerBrief(**seller_raw) if seller_raw else SellerBrief(id=0, name="Unknown", is_official=False, reputation="", location="", logo_url="")

    # Category path
    category_path = []
    if p.get("category"):
        category_path.append(CategoryItem(id=1, name=p["category"], slug=p["category"].lower().replace(" ", "-")))
    if p.get("subcategory"):
        category_path.append(CategoryItem(id=2, name=p["subcategory"], slug=p["subcategory"].lower().replace(" ", "-")))

    # Specs
    all_specs = find_all("product_specs", product_id=p["id"])
    specs = [ProductSpecOut(key=s["spec_key"], value=s["spec_value"]) for s in sorted(all_specs, key=lambda x: x.get("sort_order", 0))]

    # Images
    all_images = find_all("product_images", product_id=p["id"])
    images = [ProductImageOut(id=img["id"], url=img["url"], alt_text=img["alt_text"]) for img in sorted(all_images, key=lambda x: x.get("sort_order", 0))]

    return ProductDetail(
        id=p["id"],
        title=p["title"],
        description=p["description"],
        price=price,
        original_price=original,
        currency=p.get("currency", "US$"),
        discount_percentage=discount,
        category=p.get("category", ""),
        subcategory=p.get("subcategory", ""),
        stock=p.get("stock", 0),
        rating_avg=p.get("rating_avg", 0.0),
        rating_count=p.get("rating_count", 0),
        free_shipping=p.get("free_shipping", False),
        warranty_months=p.get("warranty_months", 12),
        installments=InstallmentInfo(count=installment_count, amount=installment_amount),
        category_path=category_path,
        seller=seller,
        images=images,
        specs=specs,
    )


@router.get("/products", response_model=ApiResponse[ProductList])
async def list_products(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=50),
    category: str | None = None,
):
    all_products = get_collection("products")

    if category:
        all_products = [p for p in all_products if p.get("category") == category]

    total = len(all_products)
    total_pages = math.ceil(total / page_size) if total > 0 else 0
    start = (page - 1) * page_size
    page_items = all_products[start:start + page_size]

    items = []
    for p in page_items:
        images = find_all("product_images", product_id=p["id"])
        images_sorted = sorted(images, key=lambda x: x.get("sort_order", 0))
        thumb = images_sorted[0]["url"] if images_sorted else ""
        items.append(
            ProductListItem(
                id=p["id"],
                title=p["title"],
                price=p["price"],
                currency=p.get("currency", "US$"),
                thumbnail=thumb,
                category=p.get("category", ""),
                rating_avg=p.get("rating_avg", 0.0),
                rating_count=p.get("rating_count", 0),
                free_shipping=p.get("free_shipping", False),
            )
        )

    return ApiResponse(
        data=ProductList(
            items=items,
            pagination=Pagination(page=page, page_size=page_size, total=total, total_pages=total_pages),
        )
    )


@router.get("/products/{product_id}", response_model=ApiResponse[ProductDetail])
async def get_product(product_id: int):
    product = find_by_id("products", product_id)

    if not product:
        return ApiResponse(code=404, data=None, message=f"Product with id {product_id} not found")

    return ApiResponse(data=_make_product_detail(product))
