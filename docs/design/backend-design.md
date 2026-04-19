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
│  │        Data Layer (JSON File Store)           │ │
│  │   dict lookups  ◀──  backend/data/*.json     │ │
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
| Data Store | JSON files | Zero-config, human-readable, no database dependency |
| Validation | Pydantic v2 | Integrated with FastAPI, type-safe schemas |
| Testing | pytest + httpx | Async test client for FastAPI |
| Server | uvicorn | ASGI server for FastAPI |

### Python Dependencies

```
fastapi>=0.110.0
uvicorn>=0.29.0
pydantic>=2.0.0
httpx>=0.27.0          # for tests
pytest>=8.0.0
pytest-asyncio>=0.23.0
```

---

## 3. Data Collections (JSON Files)

Data is stored in `backend/data/*.json` files, each containing a JSON array of objects. All collections are loaded into an in-memory dict at startup via `init_store()` in `database.py`.

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

### JSON Collections

Data is stored as JSON arrays in `backend/data/`:

| File | Collection | Purpose |
|------|-----------|---------|
| `data/sellers.json` | sellers | Store/vendor profiles |
| `data/products.json` | products | Product catalog items |
| `data/product_images.json` | product_images | Product image URLs |
| `data/product_specs.json` | product_specs | Generic key-value specs |
| `data/reviews.json` | reviews | Customer reviews |
| `data/payment_methods.json` | payment_methods | Payment options |

Each file contains a top-level JSON array of objects whose keys match the field names shown in the ER diagram above. Relationships are maintained via `id` / `seller_id` / `product_id` fields, resolved at query time through dict lookups in `database.py`.

**Example** -- a single product in `data/products.json`:
```json
[
  {
    "id": 1,
    "title": "Samsung Galaxy A55 5G 256GB Dark Blue 8GB RAM",
    "description": "Experience the power of 5G...",
    "price": 439.00,
    "original_price": 499.00,
    "currency": "US$",
    "category": "Smartphones",
    "subcategory": "Cell Phones",
    "stock": 15,
    "rating_avg": 4.8,
    "rating_count": 950,
    "free_shipping": true,
    "warranty_months": 12,
    "seller_id": 1,
    "created_at": "2024-01-15T10:00:00",
    "updated_at": "2025-01-15T10:00:00"
  }
]
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

import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

# In-memory store: dict[str, list[dict]]
_store: dict[str, list[dict]] = {}


def init_store() -> None:
    """Load all JSON collections into memory at startup."""
    for path in DATA_DIR.glob("*.json"):
        _store[path.stem] = json.loads(path.read_text(encoding="utf-8"))


def get_collection(name: str) -> list[dict]:
    """Return a collection by file stem name (e.g. 'products')."""
    return _store.get(name, [])


def find_by_id(collection: str, item_id: int) -> dict | None:
    """Look up a single item by its 'id' field."""
    for item in get_collection(collection):
        if item.get("id") == item_id:
            return item
    return None


def find_many(collection: str, field: str, value) -> list[dict]:
    """Return all items where item[field] == value."""
    return [item for item in get_collection(collection) if item.get(field) == value]
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

The seed script (`app/seed.py`) writes realistic demo data to JSON files in `backend/data/`:

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

### Test Data Store
- Use in-memory store populated from seed data in `conftest.py` fixture
- `init_store()` is called before each test to load JSON collections
- Each test gets a fresh in-memory copy of the seed data

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
│   ├── database.py        # JSON file loader, init_store, helper lookups
│   ├── schemas.py         # Pydantic request/response schemas
│   ├── seed.py            # JSON file seeding script
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
├── data/                   # JSON data files (created by seed.py)
│   ├── sellers.json
│   ├── products.json
│   ├── product_images.json
│   ├── product_specs.json
│   ├── reviews.json
│   └── payment_methods.json
└── tests/
    ├── conftest.py
    ├── test_products.py
    ├── test_sellers.py
    ├── test_reviews.py
    └── test_payments.py
```
