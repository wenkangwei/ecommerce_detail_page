# Backend Design Specification

> This document describes the FastAPI backend architecture, database schema, API endpoints, and data models.

---

## 1. Architecture Overview

```
┌─────────────────────────────────────────────────┐
│                  FastAPI Application              │
│                                                   │
│  ┌─────────────────────────────────────────────┐ │
│  │              Router Layer                     │ │
│  │  /api/v1/products     → products.py          │ │
│  │  /api/v1/sellers      → sellers.py           │ │
│  │  /api/v1/reviews      → reviews.py           │ │
│  │  /api/v1/payment-methods → payments.py       │ │
│  └──────────────────┬──────────────────────────┘ │
│                     │                             │
│  ┌──────────────────▼──────────────────────────┐ │
│  │             Schema Layer (Pydantic)           │ │
│  │   Request validation + Response serialization │ │
│  └──────────────────┬──────────────────────────┘ │
│                     │                             │
│  ┌──────────────────▼──────────────────────────┐ │
│  │           Database Layer (SQLAlchemy)         │ │
│  │   ORM Models  ──▶  SQLite (data/ecommerce.db)│ │
│  └─────────────────────────────────────────────┘ │
│                                                   │
│  Static Files: /static/images/ → product images   │
└─────────────────────────────────────────────────┘
```

---

## 2. Technology Choices

| Component | Choice | Reason |
|-----------|--------|--------|
| Framework | FastAPI | Async, auto OpenAPI docs, Pydantic integration |
| ORM | SQLAlchemy 2.0 | Python standard ORM, async support |
| Database | SQLite | Zero-config, file-based, perfect for demo |
| Validation | Pydantic v2 | Integrated with FastAPI, type-safe schemas |
| Testing | pytest + httpx | Async test client for FastAPI |
| Server | uvicorn | ASGI server for FastAPI |

### Python Dependencies

```
fastapi>=0.110.0
uvicorn>=0.29.0
sqlalchemy>=2.0.0
pydantic>=2.0.0
httpx>=0.27.0          # for tests
pytest>=8.0.0
pytest-asyncio>=0.23.0
```

---

## 3. Database Schema

### Entity-Relationship Diagram

```
┌──────────────┐       ┌──────────────────┐
│   sellers     │       │    products       │
├──────────────┤       ├──────────────────┤
│ id (PK)      │◀──┐   │ id (PK)          │
│ name         │   │   │ title            │
│ is_official  │   ├───│ seller_id (FK)   │
│ reputation   │   │   │ description      │
│ location     │   │   │ price            │
│ logo_url     │   │   │ original_price   │
│ created_at   │   │   │ currency         │
└──────────────┘   │   │ category         │
                   │   │ subcategory      │
                   │   │ stock            │
                   │   │ rating_avg       │
                   │   │ rating_count     │
                   │   │ free_shipping    │
                   │   │ warranty_months  │
                   │   │ created_at       │
                   │   │ updated_at       │
                   │   └────────┬─────────┘
                   │            │
                   │   ┌────────┴─────────┐
                   │   │ product_images    │
                   │   ├──────────────────┤
                   │   │ id (PK)          │
                   │   │ product_id (FK)  │
                   │   │ url              │
                   │   │ alt_text         │
                   │   │ sort_order       │
                   │   └──────────────────┘
                   │
                   │   ┌──────────────────┐
                   │   │ product_specs    │
                   │   ├──────────────────┤
                   │   │ id (PK)          │
                   │   │ product_id (FK)  │
                   │   │ spec_key         │
                   │   │ spec_value       │
                   │   │ sort_order       │
                   │   └──────────────────┘
                   │
                   │   ┌──────────────────┐
                   │   │    reviews        │
                   │   ├──────────────────┤
                   │   │ id (PK)          │
                   │   │ product_id (FK)  │
                   │   │ user_name        │
                   │   │ rating (1-5)     │
                   │   │ title            │
                   │   │ content          │
                   │   │ created_at       │
                   │   └──────────────────┘
                   │
                   │   ┌──────────────────┐
                   └───│payment_methods   │
                       ├──────────────────┤
                       │ id (PK)          │
                       │ name             │
                       │ type             │
                       │ icon_url         │
                       │ max_installments │
                       │ sort_order       │
                       └──────────────────┘
```

### SQLAlchemy Models

```python
# models.py

class Seller(Base):
    __tablename__ = "sellers"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200))
    is_official: Mapped[bool] = mapped_column(default=False)
    reputation: Mapped[str] = mapped_column(String(100))
    location: Mapped[str] = mapped_column(String(200))
    logo_url: Mapped[str] = mapped_column(String(500))
    created_at: Mapped[datetime]

    products: Mapped[List["Product"]] = relationship(back_populates="seller")


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(500))
    description: Mapped[str] = mapped_column(Text)
    price: Mapped[float]
    original_price: Mapped[float]
    currency: Mapped[str] = mapped_column(String(10), default="US$")
    category: Mapped[str] = mapped_column(String(200))
    subcategory: Mapped[str] = mapped_column(String(200))
    stock: Mapped[int] = mapped_column(default=0)
    rating_avg: Mapped[float] = mapped_column(default=0.0)
    rating_count: Mapped[int] = mapped_column(default=0)
    free_shipping: Mapped[bool] = mapped_column(default=False)
    warranty_months: Mapped[int] = mapped_column(default=12)
    seller_id: Mapped[int] = mapped_column(ForeignKey("sellers.id"))
    created_at: Mapped[datetime]
    updated_at: Mapped[datetime]

    seller: Mapped["Seller"] = relationship(back_populates="products")
    images: Mapped[List["ProductImage"]] = relationship(back_populates="product",
                                                          order_by="ProductImage.sort_order")
    specs: Mapped[List["ProductSpec"]] = relationship(back_populates="product",
                                                       order_by="ProductSpec.sort_order")
    reviews: Mapped[List["Review"]] = relationship(back_populates="product")


class ProductImage(Base):
    __tablename__ = "product_images"

    id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    url: Mapped[str] = mapped_column(String(500))
    alt_text: Mapped[str] = mapped_column(String(200))
    sort_order: Mapped[int] = mapped_column(default=0)

    product: Mapped["Product"] = relationship(back_populates="images")


class ProductSpec(Base):
    __tablename__ = "product_specs"

    id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    spec_key: Mapped[str] = mapped_column(String(200))
    spec_value: Mapped[str] = mapped_column(String(500))
    sort_order: Mapped[int] = mapped_column(default=0)

    product: Mapped["Product"] = relationship(back_populates="specs")


class Review(Base):
    __tablename__ = "reviews"

    id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    user_name: Mapped[str] = mapped_column(String(100))
    rating: Mapped[int]                         # 1-5
    title: Mapped[str] = mapped_column(String(200))
    content: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime]

    product: Mapped["Product"] = relationship(back_populates="reviews")


class PaymentMethod(Base):
    __tablename__ = "payment_methods"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    type: Mapped[str] = mapped_column(String(50))  # credit_card, debit_card, digital_wallet
    icon_url: Mapped[str] = mapped_column(String(500))
    max_installments: Mapped[int] = mapped_column(default=1)
    sort_order: Mapped[int] = mapped_column(default=0)
```

---

## 4. API Endpoints

### Base URL: `/api/v1`

### 4.1 Health Check

```
GET /health
```
**Response:**
```json
{
  "code": 0,
  "data": { "status": "healthy", "version": "1.0.0" },
  "message": "ok"
}
```

### 4.2 Product Endpoints

#### Get Product Detail
```
GET /api/v1/products/{product_id}
```

**Response (200):**
```json
{
  "code": 0,
  "data": {
    "id": 1,
    "title": "Samsung Galaxy A55 5G Dual SIM 256GB Dark Blue 8GB RAM",
    "description": "Experience the power of 5G...",
    "price": 439.00,
    "original_price": 499.00,
    "currency": "US$",
    "discount_percentage": 12,
    "category": "Smartphones",
    "subcategory": "Cell Phones",
    "stock": 15,
    "rating_avg": 4.8,
    "rating_count": 950,
    "free_shipping": true,
    "warranty_months": 12,
    "installments": {
      "count": 10,
      "amount": 43.90,
      "interest_free": true
    },
    "category_path": [
      { "id": 1, "name": "Electronics", "slug": "electronics" },
      { "id": 2, "name": "Smartphones", "slug": "smartphones" },
      { "id": 3, "name": "Samsung", "slug": "samsung" }
    ],
    "seller": {
      "id": 1,
      "name": "Samsung Official Store",
      "is_official": true,
      "reputation": "MercadoLíder Platinum",
      "location": "Montevideo, Uruguay",
      "logo_url": "/static/images/sellers/samsung.png"
    },
    "images": [
      { "id": 1, "url": "/static/images/products/samsung-a55-1.jpg", "alt_text": "Samsung Galaxy A55 front" },
      { "id": 2, "url": "/static/images/products/samsung-a55-2.jpg", "alt_text": "Samsung Galaxy A55 back" }
    ],
    "specs": [
      { "key": "Screen Size", "value": "6.6 inches" },
      { "key": "RAM", "value": "8 GB" },
      { "key": "Storage", "value": "256 GB" },
      { "key": "Rear Camera", "value": "50 MP" },
      { "key": "Front Camera", "value": "32 MP" },
      { "key": "Connectivity", "value": "5G, NFC" }
    ]
  },
  "message": "ok"
}
```

**Error (404):**
```json
{
  "code": 404,
  "data": null,
  "message": "Product not found"
}
```

#### List Products
```
GET /api/v1/products?page=1&page_size=10&category=Smartphones
```

**Response (200):**
```json
{
  "code": 0,
  "data": {
    "items": [
      { "id": 1, "title": "...", "price": 439.00, "thumbnail": "/static/...", "category": "..." }
    ],
    "pagination": {
      "page": 1,
      "page_size": 10,
      "total": 5,
      "total_pages": 1
    }
  },
  "message": "ok"
}
```

### 4.3 Seller Endpoints

#### Get Seller
```
GET /api/v1/sellers/{seller_id}
```

**Response (200):**
```json
{
  "code": 0,
  "data": {
    "id": 1,
    "name": "Samsung Official Store",
    "is_official": true,
    "reputation": "MercadoLíder Platinum",
    "location": "Montevideo, Uruguay",
    "logo_url": "/static/images/sellers/samsung.png",
    "product_count": 150,
    "created_at": "2024-01-01T00:00:00"
  },
  "message": "ok"
}
```

### 4.4 Review Endpoints

#### Get Product Reviews
```
GET /api/v1/products/{product_id}/reviews?page=1&page_size=10
```

**Response (200):**
```json
{
  "code": 0,
  "data": {
    "items": [
      {
        "id": 1,
        "user_name": "Juan P.",
        "rating": 5,
        "title": "Excellent phone!",
        "content": "Great value for money...",
        "date": "2025-12-15"
      }
    ],
    "pagination": {
      "page": 1,
      "page_size": 10,
      "total": 950
    },
    "summary": {
      "average": 4.8,
      "distribution": {
        "5": 680,
        "4": 200,
        "3": 45,
        "2": 15,
        "1": 10
      }
    }
  },
  "message": "ok"
}
```

### 4.5 Payment Method Endpoints

#### List Payment Methods
```
GET /api/v1/payment-methods
```

**Response (200):**
```json
{
  "code": 0,
  "data": [
    {
      "id": 1,
      "name": "VISA",
      "type": "credit_card",
      "icon_url": "/static/images/payments/visa.svg",
      "max_installments": 12
    },
    {
      "id": 2,
      "name": "Mastercard",
      "type": "credit_card",
      "icon_url": "/static/images/payments/mastercard.svg",
      "max_installments": 12
    },
    {
      "id": 3,
      "name": "VISA Debit",
      "type": "debit_card",
      "icon_url": "/static/images/payments/visa-debit.svg",
      "max_installments": 1
    },
    {
      "id": 4,
      "name": "Mercado Pago",
      "type": "digital_wallet",
      "icon_url": "/static/images/payments/mercadopago.svg",
      "max_installments": 12
    }
  ],
  "message": "ok"
}
```

---

## 5. Unified Response Format

All API responses follow this envelope:

```python
# schemas.py
class ApiResponse(BaseModel, Generic[T]):
    code: int = 0
    data: T | None = None
    message: str = "ok"
```

| code | meaning |
|------|---------|
| `0` | Success |
| `400` | Bad request (invalid params) |
| `404` | Resource not found |
| `500` | Internal server error |

---

## 6. Application Configuration

```python
# database.py

DATABASE_URL = "sqlite:///./data/ecommerce.db"

engine = create_async_engine(DATABASE_URL, echo=False)
async_session = async_sessionmaker(engine, class_=AsyncSession)

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
```

```python
# main.py

app = FastAPI(
    title="E-Commerce Detail API",
    version="1.0.0",
    docs_url="/docs",          # Swagger UI
    redoc_url="/redoc",        # ReDoc
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite dev server
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Routers
app.include_router(products.router, prefix="/api/v1")
app.include_router(sellers.router, prefix="/api/v1")
app.include_router(reviews.router, prefix="/api/v1")
app.include_router(payments.router, prefix="/api/v1")
```

---

## 7. Seed Data

The seed script (`app/seed.py`) creates realistic demo data:

### Sellers (3)
| ID | Name | Official | Reputation |
|----|------|----------|------------|
| 1 | Samsung Official Store | Yes | MercadoLíder Platinum |
| 2 | TechWorld | No | MercadoLíder Gold |
| 3 | Global Electronics | Yes | MercadoLíder Platinum |

### Products (5+)
| ID | Title | Price | Category | Seller |
|----|-------|-------|----------|--------|
| 1 | Samsung Galaxy A55 5G 256GB Dark Blue 8GB RAM | $439 | Smartphones | Samsung |
| 2 | Apple iPhone 15 128GB Black | $799 | Smartphones | TechWorld |
| 3 | Samsung Galaxy Tab S9 128GB | $549 | Tablets | Samsung |
| 4 | Sony WH-1000XM5 Headphones | $299 | Audio | Global |
| 5 | MacBook Air M3 256GB | $999 | Laptops | TechWorld |
| 6 | Logitech MX Master 3S Mouse | $79 | Accessories | Global |

### Reviews (per product: 8-20 reviews)
- Random user names, ratings weighted toward 4-5 stars
- Realistic review titles and content

### Payment Methods (4+)
- VISA, Mastercard (credit), VISA Debit (debit), Mercado Pago (wallet)

### Product Images
- Use placeholder URLs: `https://placehold.co/480x480/F5F5F5/333?text=Product+Image+N`
- 3-5 images per product

---

## 8. Error Handling

```python
# Custom exceptions
class AppError(Exception):
    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message

class NotFoundError(AppError):
    def __init__(self, resource: str, id: int):
        super().__init__(404, f"{resource} with id {id} not found")

# Global exception handler
@app.exception_handler(AppError)
async def app_error_handler(request, exc):
    return JSONResponse(
        status_code=exc.code,
        content={"code": exc.code, "data": None, "message": exc.message}
    )
```

---

## 9. Testing Strategy

### Test Structure
```
backend/tests/
├── conftest.py          # Test database fixture, test client
├── test_products.py     # GET /products, GET /products/{id}
├── test_sellers.py      # GET /sellers/{id}
├── test_reviews.py      # GET /products/{id}/reviews
└── test_payments.py     # GET /payment-methods
```

### Test Database
- Use in-memory SQLite (`sqlite+aiosqlite://`) for tests
- Seed test data in `conftest.py` fixture
- Each test gets a fresh database

### Test Cases per Endpoint
1. **Happy path**: valid ID → 200 with correct data shape
2. **Not found**: invalid ID → 404
3. **Pagination**: verify page/page_size params work
4. **Data integrity**: response includes all expected fields

### Run Command
```bash
cd backend && python -m pytest tests/ -v
```

---

## 10. Directory Structure

```
backend/
├── pyproject.toml
├── requirements.txt
├── app/
│   ├── __init__.py
│   ├── main.py            # FastAPI app, CORS, routers, static files
│   ├── database.py        # Engine, session, init_db
│   ├── models.py          # SQLAlchemy ORM models
│   ├── schemas.py         # Pydantic request/response schemas
│   ├── seed.py            # Database seeding script
│   └── routers/
│       ├── __init__.py
│       ├── products.py     # Product endpoints
│       ├── sellers.py      # Seller endpoints
│       ├── reviews.py      # Review endpoints
│       └── payments.py     # Payment method endpoints
├── static/                 # Static files served by FastAPI
│   └── images/
│       ├── products/       # Product images
│       ├── sellers/        # Seller logos
│       └── payments/       # Payment method icons
└── tests/
    ├── conftest.py
    ├── test_products.py
    ├── test_sellers.py
    ├── test_reviews.py
    └── test_payments.py
```
