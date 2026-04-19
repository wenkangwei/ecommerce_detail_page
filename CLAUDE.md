# E-Commerce Detail Page — Development Standards

> All development must strictly follow these standards. When in doubt, refer to this file.

## Project Overview

A MercadoLibre-style e-commerce product detail page. Full-stack web app with FastAPI backend serving product data from local JSON files, and a React + TypeScript frontend rendering a responsive product detail page.

Core flow: User navigates to `/products/{id}` → frontend fetches product data from API → renders image gallery, title, price, payment methods, seller info, reviews, stock/shipping, and specifications.

## Tech Stack

- **Frontend**: React 18 + Vite + TypeScript
- **Backend**: Python 3.10+ / FastAPI
- **Data Storage**: Local JSON files (no database)
- **Testing**: pytest + httpx (backend)
- **Documentation**: MkDocs Material
- **Styling**: Plain CSS (no CSS framework)

## Code Conventions

### Python Style
- Use f-strings, not `format()` or `%`
- Type hints required on all function signatures
- Use Pydantic models for API schemas
- Use `logging` module, **no `print()`** for logging
- Module-level logger: `logger = logging.getLogger(__name__)`

### TypeScript Style
- Use functional components with hooks (no class components)
- Define interfaces for all API response types in `src/types/`
- Use `fetch` for API calls (no axios dependency)
- Named exports for components

### Naming Conventions
- Python modules: `snake_case` (`product_router.py`)
- Python classes: `PascalCase` (`ProductDetail`)
- Python functions: `snake_case` (`get_product`)
- TypeScript files: `PascalCase` for components (`ImageGallery.tsx`)
- TypeScript interfaces: `PascalCase` (`ProductData`)
- Constants: `UPPER_SNAKE_CASE`

### Error Handling
- Only catch expected exceptions, no bare `except`
- Validate input at system boundaries (API endpoints)

### Dependencies
- Minimize dependencies — only add what's necessary
- New Python deps go in both `pyproject.toml` and `requirements.txt`
- New frontend deps go in `package.json`
- **No database drivers** — data is stored in JSON files

## Module Rules

### Backend (`backend/app/`)
- `main.py` — FastAPI app factory, CORS, router registration
- `database.py` — JSON file loader, in-memory store, helper functions (`find_by_id`, `find_all`, `get_collection`)
- `schemas.py` — Pydantic request/response schemas
- `routers/` — One file per resource (products, sellers, reviews, payments)
- `seed.py` — Writes demo data to JSON files in `data/`

### Data Storage
- All data persisted in `backend/data/*.json` files
- Collections: `products.json`, `sellers.json`, `reviews.json`, `payment_methods.json`, `product_images.json`, `product_specs.json`
- Loaded into memory at startup via `database.init_store()`
- No ORM, no SQL — plain dict lookups via `find_by_id()` and `find_all()`

### Frontend (`frontend/src/`)
- `api/client.ts` — Base API client with fetch wrapper
- `components/` — One file per UI component
- `pages/` — Page-level components that compose components
- `types/` — TypeScript interfaces for API data
- `styles/` — CSS files matching MercadoLibre visual style

### API Design
- Prefix: `/api/v1/`
- Response format: `{ "code": 0, "data": {...}, "message": "ok" }`
- Error format: `{ "code": N, "data": null, "message": "error description" }`
- CORS: allow `http://localhost:5173`

## Testing

- Backend: `pytest` with `httpx.AsyncClient` for API tests
- One test file per router: `test_products.py`, `test_sellers.py`, etc.
- `conftest.py` loads seed data into the in-memory store before each test
- No mocks needed for database — just load JSON data
- Run: `cd backend && python -m pytest tests/ -v`

## Git Conventions

- Commit format: `type(scope): description`
  - type: feat / fix / docs / test / refactor / chore
  - scope: backend / frontend / docs / scripts
- Example: `feat(backend): add product detail API endpoint`
- Commit after each feature completion
- Do not commit `data/*.json` or `node_modules/`

## File Structure

```
ecommerce-detail/
├── CLAUDE.md              # This file — dev standards
├── feature_list.json      # Feature tracking (agent harness)
├── claude-progress.txt    # Cross-session progress log
├── init.sh                # Dev server startup script
├── backend/               # FastAPI backend
│   ├── app/
│   │   ├── main.py        # App entry point
│   │   ├── database.py    # JSON file loader + in-memory store
│   │   ├── schemas.py     # Pydantic schemas
│   │   ├── routers/       # API endpoints
│   │   └── seed.py        # Writes JSON data files
│   └── tests/             # Backend tests
├── frontend/              # React frontend
│   └── src/
│       ├── api/           # API client
│       ├── components/    # UI components
│       ├── pages/         # Page components
│       ├── types/         # TypeScript types
│       └── styles/        # CSS styles
├── scripts/               # Automation scripts
├── docs/                  # MkDocs documentation
└── data/                  # JSON data files (gitignored)
```

## Prohibitions

- No `print()` for logging → use `logging`
- No hardcoded API keys → environment variables
- No real external API calls in tests → use loaded JSON data
- No CSS frameworks (Bootstrap, Tailwind) → plain CSS
- No checkout/payment logic → detail page only
- No recommendation widgets → out of scope
- No database engines (SQLite, PostgreSQL, etc.) → JSON files only
- No ORM libraries (SQLAlchemy, etc.) → plain dict lookups
- No modifying existing feature descriptions in `feature_list.json`
- No marking features as passed without testing
