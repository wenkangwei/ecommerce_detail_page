from typing import Generic, TypeVar

from pydantic import BaseModel

T = TypeVar("T")


# ── Unified API Response ──────────────────────────────────────

class ApiResponse(BaseModel, Generic[T]):
    code: int = 0
    data: T | None = None
    message: str = "ok"


# ── Seller ────────────────────────────────────────────────────

class SellerBrief(BaseModel):
    id: int
    name: str
    is_official: bool
    reputation: str
    location: str
    logo_url: str
    sales_count: str = ""

    model_config = {"from_attributes": True}


class SellerDetail(SellerBrief):
    product_count: int = 0
    created_at: str = ""


# ── Product ───────────────────────────────────────────────────

class ProductImageOut(BaseModel):
    id: int
    url: str
    alt_text: str

    model_config = {"from_attributes": True}


class ProductSpecOut(BaseModel):
    key: str
    value: str

    model_config = {"from_attributes": True}


class CategoryItem(BaseModel):
    id: int
    name: str
    slug: str


class InstallmentInfo(BaseModel):
    count: int
    amount: float
    interest_free: bool = True


class StockInfo(BaseModel):
    available: int
    label: str = "In Stock"


class ShippingInfo(BaseModel):
    free: bool
    estimated_days: list[int]
    to_country: bool = True


class ProductDetail(BaseModel):
    id: int
    title: str
    description: str
    price: float
    original_price: float
    currency: str = "US$"
    discount_percentage: int = 0
    category: str
    subcategory: str
    stock: int
    rating_avg: float
    rating_count: int
    free_shipping: bool
    warranty_months: int = 12
    installments: InstallmentInfo | None = None
    category_path: list[CategoryItem] = []
    seller: SellerBrief
    images: list[ProductImageOut] = []
    specs: list[ProductSpecOut] = []
    color: str = ""
    sold_count: int = 0

    model_config = {"from_attributes": True}


class ProductListItem(BaseModel):
    id: int
    title: str
    price: float
    currency: str = "US$"
    thumbnail: str = ""
    category: str
    rating_avg: float
    rating_count: int
    free_shipping: bool

    model_config = {"from_attributes": True}


class Pagination(BaseModel):
    page: int
    page_size: int
    total: int
    total_pages: int


class ProductList(BaseModel):
    items: list[ProductListItem]
    pagination: Pagination


# ── Review ────────────────────────────────────────────────────

class ReviewOut(BaseModel):
    id: int
    user_name: str
    rating: int
    title: str
    content: str
    date: str

    model_config = {"from_attributes": True}


class ReviewDistribution(BaseModel):
    star_5: int = 0
    star_4: int = 0
    star_3: int = 0
    star_2: int = 0
    star_1: int = 0


class ReviewSummary(BaseModel):
    average: float
    distribution: ReviewDistribution


class ReviewList(BaseModel):
    items: list[ReviewOut]
    pagination: Pagination
    summary: ReviewSummary


# ── Payment Method ────────────────────────────────────────────

class PaymentMethodOut(BaseModel):
    id: int
    name: str
    type: str
    icon_url: str
    max_installments: int

    model_config = {"from_attributes": True}


# ── Health ────────────────────────────────────────────────────

class HealthData(BaseModel):
    status: str = "healthy"
    version: str = "1.0.0"


# ── Related / Brand Products ──────────────────────────────────

class RelatedProductOut(BaseModel):
    id: int
    title: str
    price: float
    original_price: float
    currency: str = "US$"
    discount_percentage: int = 0
    image_url: str = ""
    installments: InstallmentInfo | None = None
    free_shipping: bool = True

    model_config = {"from_attributes": True}
