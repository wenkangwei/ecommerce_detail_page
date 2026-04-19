# Architecture Overview

## System Architecture

```
┌─────────────────────────────────────────────────┐
│                Browser (Client)                  │
│         http://localhost:5173                     │
└───────────────────────┬─────────────────────────┘
                        │ HTTP
                        ▼
┌─────────────────────────────────────────────────┐
│             Vite Dev Server                      │
│         Proxy /api → Backend:8000                │
└───────────────────────┬─────────────────────────┘
                        │
          ┌─────────────┴─────────────┐
          ▼                           ▼
┌──────────────────┐      ┌──────────────────────┐
│  React Frontend   │      │  FastAPI Backend      │
│  - Components     │◀────▶│  - REST API           │
│  - TypeScript     │ API  │  - Pydantic schemas   │
│  - CSS Styles     │      │  - SQLAlchemy ORM     │
└──────────────────┘      └──────────┬───────────┘
                                     │
                                     ▼
                          ┌──────────────────────┐
                          │  SQLite Database      │
                          │  data/ecommerce.db    │
                          └──────────────────────┘
```

## Frontend Architecture

The frontend uses a simple, flat component architecture:

```
ProductDetailPage (orchestrator)
├── Breadcrumb
├── ImageGallery
├── PriceBlock
├── StockShipping
├── SellerCard
├── PaymentMethods
├── ProductSpecs
└── ReviewsSection
    └── ReviewCard (repeated)
```

### Data Flow

1. User navigates to `/products/{id}`
2. `ProductDetailPage` fires 3 parallel API calls:
   - `GET /api/v1/products/{id}` — product + seller + images + specs
   - `GET /api/v1/products/{id}/reviews` — reviews + summary
   - `GET /api/v1/payment-methods` — payment options
3. Data is stored in React `useState` hooks
4. Components receive data via props

### No External State Library

This is a single-page detail view. React hooks are sufficient — no Redux or Zustand needed.

## Backend Architecture

### Layered Design

```
Router Layer (endpoints)
    ↓
Schema Layer (Pydantic validation/serialization)
    ↓
Database Layer (SQLAlchemy ORM)
```

### API Design Principles

- **RESTful** resource-oriented URLs
- **Unified envelope**: `{code, data, message}`
- **Read-only**: only GET endpoints (detail page, not admin)
- **Auto-documented**: Swagger UI at `/docs`

### Database Schema

6 tables with clean relationships:

```
sellers ← products ← product_images
                  ← product_specs
                  ← reviews
payment_methods (standalone)
```

Products use **generic key-value specs** (`product_specs`) to support any product category.

## Design Decisions

| Decision | Rationale |
|----------|-----------|
| SQLite over PostgreSQL | Zero-config, file-based, perfect for demo/prototype |
| Plain CSS over Tailwind | Full control to match MercadoLibre's exact visual style |
| React hooks over Redux | Single page, no complex state management needed |
| Generic specs table | Supports any product type without schema changes |
| Proxy via Vite | Avoids CORS issues in development |
