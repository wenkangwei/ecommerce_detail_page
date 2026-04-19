# Module Design

## Backend Modules

### `app/main.py` — Application Entry Point

Creates the FastAPI application, configures CORS middleware, registers routers, and mounts static file serving.

### `app/database.py` — Database Connection

Manages the SQLAlchemy async engine and session factory. Uses `aiosqlite` driver for async SQLite access. Computes the database path relative to the backend directory.

### `app/models.py` — ORM Models

Defines 6 SQLAlchemy models:

| Model | Table | Purpose |
|-------|-------|---------|
| `Seller` | `sellers` | Store/vendor profiles |
| `Product` | `products` | Product catalog items |
| `ProductImage` | `product_images` | Product image URLs |
| `ProductSpec` | `product_specs` | Generic key-value specs |
| `Review` | `reviews` | Customer reviews |
| `PaymentMethod` | `payment_methods` | Payment options |

Key design: `ProductSpec` uses a generic `spec_key`/`spec_value` pattern to support any product category without schema changes.

### `app/schemas.py` — Pydantic Schemas

Defines request/response schemas with Pydantic v2:

- `ApiResponse[T]` — Generic envelope wrapper
- `ProductDetail` — Full product with nested seller, images, specs
- `ProductList` — Paginated product listing
- `ReviewList` — Reviews with summary and distribution
- `PaymentMethodOut` — Payment method data

### `app/routers/` — API Endpoints

Each resource has its own router:

- `products.py` — Product listing and detail, uses `selectinload` for eager loading
- `sellers.py` — Seller profiles with product count
- `reviews.py` — Reviews with star distribution computation
- `payments.py` — Static payment method list

### `app/seed.py` — Database Seeder

Populates the database with realistic demo data:
- 3 sellers (official and third-party)
- 6 products across multiple categories
- 3-5 images per product (placeholder URLs)
- 8-20 reviews per product
- 6 payment methods

---

## Frontend Modules

### `src/api/client.ts` — API Client

Thin `fetch` wrapper that:
- Prepends the API base URL
- Unwraps the `{code, data, message}` envelope
- Throws on errors

Three exported functions:
```ts
fetchProduct(id)       → ProductDetail
fetchReviews(id, page) → ReviewListResponse
fetchPaymentMethods()  → PaymentMethod[]
```

### `src/types/index.ts` — TypeScript Interfaces

Defines types for all API response data:
- `ProductDetail`, `ProductImage`, `ProductSpec`
- `SellerBrief`, `CategoryItem`, `InstallmentInfo`
- `ReviewData`, `ReviewSummary`, `ReviewDistribution`
- `PaymentMethod`

### `src/pages/ProductDetail.tsx` — Main Page

Orchestrator component that:
1. Reads `:id` from URL params
2. Fetches product, reviews, and payments in parallel
3. Renders loading skeleton → error or full page
4. Composes all child components in two-column layout

### `src/components/` — UI Components

| Component | Props | Description |
|-----------|-------|-------------|
| `Breadcrumb` | `items[]`, `productName` | Category path navigation |
| `ImageGallery` | `images[]` | Main image + thumbnail strip |
| `PriceBlock` | `price`, `originalPrice`, `discount`, `installments` | Price display with discount badge |
| `StockShipping` | `stock`, `freeShipping`, `warranty` | Availability and shipping info |
| `SellerCard` | `seller` | Seller profile with official badge |
| `PaymentMethods` | `methods[]` | Payment options with icons |
| `ProductSpecs` | `specs[]` | Expandable spec table |
| `ReviewsSection` | `reviews[]`, `summary`, `pagination` | Review list with distribution chart |

### `src/styles/product.css` — Stylesheet

Implements the MercadoLibre visual style using CSS custom properties:
- 15+ color tokens
- Responsive grid (desktop 60/40, tablet 55/45, mobile stacked)
- Card shadows and border radius
- Typography scale from 12px to 48px
- Breakpoints at 768px and 1024px

---

## Automation

### `scripts/auto_run.sh`

Agent harness automation script that:
1. Reads `feature_list.json` for next pending feature
2. Builds a coding prompt for that feature
3. Invokes `claude -p` with restricted tools
4. Verifies the feature was marked as passed
5. Retries once on failure
6. Commits after each session
7. Compresses progress log periodically

Commands: `run`, `--status`, `--dry-run`, `--help`
