# Module Design

## Backend Modules

### `app/main.py` — Application Entry Point

Creates the FastAPI application, configures CORS middleware, registers routers, and mounts static file serving.

### `app/database.py` — JSON File Loader

Loads all JSON files from `backend/data/` into an in-memory dict at startup via `init_store()`. Provides helper functions for data access:

- `get_collection(name)` -- return a full collection by file stem name
- `find_by_id(collection, item_id)` -- look up a single item by `id`
- `find_many(collection, field, value)` -- filter items by any field value

### `app/schemas.py` — Pydantic Schemas

Defines request/response schemas with Pydantic v2:

- `ApiResponse[T]` — Generic envelope wrapper
- `ProductDetail` — Full product with nested seller, images, specs
- `ProductList` — Paginated product listing
- `ReviewList` — Reviews with summary and distribution
- `PaymentMethodOut` — Payment method data

### `app/routers/` — API Endpoints

Each resource has its own router:

- `products.py` — Product listing and detail, uses dict lookups to join related data
- `sellers.py` — Seller profiles with product count
- `reviews.py` — Reviews with star distribution computation
- `payments.py` — Static payment method list

### `app/seed.py` — JSON File Seeder

Writes JSON data files to `backend/data/` with realistic demo data:
- 3 sellers (official and third-party)
- 6 products across multiple categories
- 3-5 images per product (placeholder URLs)
- 8-20 reviews per product
- 6 payment methods

Each collection is written as a top-level JSON array to its own file (e.g. `products.json`, `sellers.json`). Existing files are overwritten on each run.

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
3. Renders loading spinner → error or full page
4. Composes all child components in **3-column layout** (Gallery | Info | Purchase)

### `src/components/` — UI Components

| Component | Props | Description |
|-----------|-------|-------------|
| `Breadcrumb` | `items[]`, `productName` | Category path navigation |
| `ImageGallery` | `images[]` | Vertical thumbnail strip + main image, hover-to-switch |
| `PriceBlock` | `price`, `originalPrice`, `discount`, `installments` | Price display with discount badge and installment info |
| `StockShipping` | `stock`, `freeShipping`, `warrantyMonths` | Free shipping badge (green), stock dot indicator, quantity |
| `SellerCard` | `seller` | Official store badge, seller name, sales, store link |
| `PaymentMethods` | `methods[]` | Payment options with card icons, expandable |
| `ProductSpecs` | `specs[]` | Expandable 2-column spec grid |
| `ReviewsSection` | `reviews[]`, `summary`, `pagination` | Review list with star distribution chart |

### `src/styles/product.css` — Stylesheet

Implements the MercadoLibre visual style using CSS custom properties:
- 15+ color tokens
- 3-column CSS Grid: `grid-template-columns: 440px 1fr 320px` (desktop)
- Vertical thumbnail gallery strip
- Purchase panel with buy/cart buttons and buyer protection section
- Responsive breakpoints at 768px (mobile, single column) and 1024px (tablet, compressed 3-column)
- Typography scale from 12px to 48px

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
