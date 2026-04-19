# E-Commerce Product Detail Page

A **MercadoLibre-style** e-commerce product detail page built with a modern full-stack architecture. Features a polished, responsive UI with real product images, Spanish-language interface, and interactive components.

![Tech Stack](https://img.shields.io/badge/React_18-TypeScript-blue) ![FastAPI](https://img.shields.io/badge/FastAPI-Python_3.10+-green) ![Data](https://img.shields.io/badge/Data-JSON_Files-orange)

---

## Screenshot

The page renders a MercadoLibre-style product detail with:
- Grey background with white card containers
- 3-column layout: Image Gallery | Product Info | Purchase Panel
- Yellow suggestion bar, "MÁS VENDIDO" badges, branded payment card icons
- Related products grid, seller card with dark banner, customer reviews

---

## Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| Frontend | React 18 + TypeScript + Vite | UI rendering, SPA |
| Styling | Plain CSS | MercadoLibre visual style |
| Backend | FastAPI (Python 3.10+) | REST API |
| Data | Local JSON files | Zero-config data storage |
| Images | Static file serving | Local product images |
| Testing | pytest + httpx | Backend API tests |

---

## Quick Start

### Prerequisites

- Python 3.10+
- Node.js 18+
- npm 9+
- Git

### 1. Clone & Setup

```bash
git clone https://github.com/wenkangwei/ecommerce_detail_page.git
cd ecommerce_detail_page
```

### 2. Backend

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m app.seed           # Seed demo data (6 products, 26 reviews)
uvicorn app.main:app --port 8000 --reload
```

### 3. Frontend

```bash
cd frontend
npm install
npm run dev
```

### 4. Open in Browser

Navigate to **http://localhost:5173** — you'll see the Samsung Galaxy A55 product page.

### Demo Products

| URL | Product |
|-----|---------|
| `/products/1` | Samsung Galaxy A55 5G |
| `/products/2` | Apple iPhone 15 |
| `/products/3` | Samsung Galaxy Tab S9 |
| `/products/4` | Sony WH-1000XM5 |
| `/products/5` | MacBook Air M3 |
| `/products/6` | Logitech MX Master 3S |

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check |
| GET | `/api/v1/products` | List products (paginated) |
| GET | `/api/v1/products/{id}` | Product detail with seller, images, specs |
| GET | `/api/v1/products/{id}/related` | Related products |
| GET | `/api/v1/products/{id}/brand` | Same-brand products |
| GET | `/api/v1/sellers/{id}` | Seller profile |
| GET | `/api/v1/products/{id}/reviews` | Paginated reviews with star distribution |
| GET | `/api/v1/payment-methods` | Available payment methods |

Swagger UI available at **http://localhost:8000/docs**

---

## Project Structure

```
ecommerce-detail/
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI app, CORS, static files
│   │   ├── database.py          # JSON file loader, in-memory store
│   │   ├── schemas.py           # Pydantic schemas
│   │   ├── seed.py              # Demo data seeder
│   │   └── routers/
│   │       ├── products.py      # Product + related + brand endpoints
│   │       ├── sellers.py       # Seller endpoints
│   │       ├── reviews.py       # Review endpoints
│   │       └── payments.py      # Payment method endpoints
│   ├── static/images/products/  # Product images
│   ├── data/                    # JSON data files (seeded)
│   └── tests/                   # pytest test suite
├── frontend/
│   └── src/
│       ├── api/client.ts        # API fetch wrapper
│       ├── components/          # 12 UI components
│       │   ├── TopBar.tsx        # Yellow suggestion bar
│       │   ├── ImageGallery.tsx  # Thumbnail strip + main image + favorite
│       │   ├── ProductInfo.tsx   # Title, badges, specs preview
│       │   ├── PriceBlock.tsx    # Price, discount, installments
│       │   ├── PurchasePanel.tsx # Shipping, quantity, buy buttons
│       │   ├── SellerCard.tsx    # Dark banner seller card
│       │   ├── PaymentMethods.tsx# Branded card icons
│       │   ├── ProductSpecs.tsx  # Icon-based expandable specs
│       │   ├── ProductDescription.tsx
│       │   ├── RelatedProducts.tsx
│       │   └── SidebarRelatedProducts.tsx
│       ├── pages/ProductDetail.tsx
│       ├── types/index.ts
│       └── styles/product.css
└── docs/                        # Design & architecture docs
```

---

## Key Features

- **3-Column Responsive Layout** — Gallery (380px) | Product Info | Purchase Panel (320px)
- **Image Gallery** — Vertical thumbnail strip, hover-to-switch, favorite button, fade transition
- **Real Product Images** — Downloaded and served locally via FastAPI static files
- **Spanish UI** — MercadoLibre-style with "MÁS VENDIDO" badge, "Envío gratis", "Cuotas sin interés"
- **Interactive Quantity Selector** — +/− buttons with stock-aware limits
- **Branded Payment Icons** — VISA (blue), Mastercard (red/yellow), OCA (blue)
- **Dark Seller Banner** — "Tienda Oficial" with sales stats grid
- **Related Products** — 4-column product grid + sidebar list
- **Customer Reviews** — Star distribution chart, review cards with avatars
- **Expandable Specs** — Icon-based 2-column grid, expand button
- **Yellow Top Bar** — Search suggestions matching MercadoLibre style

---

## Running Tests

```bash
# Backend tests
cd backend
source .venv/bin/activate
python -m pytest tests/ -v

# Frontend type check
cd frontend
npx tsc --noEmit

# Frontend production build
npm run build
```

---

## Re-seeding Data

```bash
cd backend
source .venv/bin/activate
python -m app.seed
```

This overwrites all JSON files in `backend/data/` with fresh demo data.

---

## Documentation

### Design Documents
- [Frontend Style Guide](docs/design/frontend-style-guide.md) — Color palette, typography, component specs
- [Frontend Mechanism](docs/design/frontend-mechanism.md) — Data flow, component tree, props interfaces
- [Backend Design](docs/design/backend-design.md) — API endpoints, JSON collections, schemas
- [Run Guide](docs/design/run.md) — How to run, troubleshoot, environment variables

### Architecture Documents
- [Architecture Overview](docs/docs/architecture.md) — System diagram, design decisions
- [Quick Start Guide](docs/docs/quickstart.md) — Get running in 5 minutes
- [API Reference](docs/docs/api-reference.md) — Full endpoint documentation
- [Module Design](docs/docs/modules.md) — Backend & frontend module details
- [Usage Examples](docs/docs/examples.md) — Code samples, API interaction

---

## License

MIT
