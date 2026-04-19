# How to Run This Project

> Complete guide to set up, run, and develop the E-Commerce Detail Page project.

---

## Prerequisites

| Tool | Version | Check Command |
|------|---------|---------------|
| Python | 3.10+ | `python3 --version` |
| Node.js | 18+ | `node --version` |
| npm | 9+ | `npm --version` |
| Git | 2.0+ | `git --version` |

---

## Quick Start (One Command)

```bash
cd /home/wwk/workspace/ai_project/ecommerce-detail

# Start both backend + frontend servers
chmod +x init.sh
./init.sh
```

- Backend: `http://localhost:8000`
- Frontend: `http://localhost:5173`
- API Docs (Swagger): `http://localhost:8000/docs`

---

## Step-by-Step Setup

### 1. Backend Setup

```bash
cd /home/wwk/workspace/ai_project/ecommerce-detail/backend

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Seed the data files (creates backend/data/*.json with demo data)
python -m app.seed

# Start backend server
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

Verify: `curl http://localhost:8000/health` should return `{"code":0,"data":{"status":"healthy"},"message":"ok"}`

### 2. Frontend Setup

```bash
cd /home/wwk/workspace/ai_project/ecommerce-detail/frontend

# Install dependencies
npm install

# Start dev server
npm run dev
```

Verify: Open `http://localhost:5173` in browser — should redirect to `/products/1` and render the product detail page.

### 3. Stop Servers

```bash
./init.sh stop
```

Or press `Ctrl+C` in the respective terminal windows.

---

## Running Tests

### Backend Tests

```bash
cd /home/wwk/workspace/ai_project/ecommerce-detail/backend
source .venv/bin/activate
python -m pytest tests/ -v
```

### Frontend Build Check

```bash
cd /home/wwk/workspace/ai_project/ecommerce-detail/frontend
npm run build
```

---

## Seeding the Data Files

```bash
cd /home/wwk/workspace/ai_project/ecommerce-detail/backend
source .venv/bin/activate

# Seed (or re-seed) — overwrites existing JSON files with fresh demo data
python -m app.seed
```

This populates:
- 3 sellers (Samsung Official Store, TechWorld, Global Electronics)
- 6 products (phones, tablet, headphones, laptop, mouse)
- 3-5 images per product
- 8-20 reviews per product
- 4+ payment methods (VISA, Mastercard, Mercado Pago, etc.)

---

## API Quick Reference

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check |
| GET | `/api/v1/products` | List products (paginated) |
| GET | `/api/v1/products/{id}` | Get product detail |
| GET | `/api/v1/sellers/{id}` | Get seller profile |
| GET | `/api/v1/products/{id}/reviews` | Get product reviews |
| GET | `/api/v1/payment-methods` | List payment methods |

Swagger UI: `http://localhost:8000/docs`

---

## Environment Variables

### Backend (optional, defaults provided)

| Variable | Default | Description |
|----------|---------|-------------|
| `CORS_ORIGIN` | `http://localhost:5173` | Allowed frontend origin |

### Frontend (optional, defaults provided)

| Variable | Default | Description |
|----------|---------|-------------|
| `VITE_API_URL` | `http://localhost:8000/api/v1` | Backend API base URL |

Create `frontend/.env` if you need to override:
```
VITE_API_URL=http://localhost:8000/api/v1
```

---

## Automation (auto_run.sh)

The project includes an agent harness automation script:

```bash
cd /home/wwk/workspace/ai_project/ecommerce-detail

# Check current progress
./scripts/auto_run.sh --status

# See what features are pending
./scripts/auto_run.sh --dry-run

# Run all pending features automatically
./scripts/auto_run.sh
```

---

## Documentation Server

```bash
cd /home/wwk/workspace/ai_project/ecommerce-detail/docs
pip install mkdocs-material
mkdocs serve
```

Documentation available at `http://localhost:8001`

---

## Project Directory Structure

```
ecommerce-detail/
├── init.sh                  # Start/stop both servers
├── CLAUDE.md                # Development standards
├── feature_list.json        # Feature tracking
├── claude-progress.txt      # Session progress log
├── backend/                 # FastAPI backend
│   ├── app/
│   │   ├── main.py          # App entry point
│   │   ├── database.py      # JSON file loader, init_store, helper lookups
│   │   ├── schemas.py       # Pydantic schemas
│   │   ├── routers/         # API endpoints
│   │   └── seed.py          # JSON file seeder
│   ├── data/                # JSON data files (created by seed.py)
│   │   ├── sellers.json
│   │   ├── products.json
│   │   ├── product_images.json
│   │   ├── product_specs.json
│   │   ├── reviews.json
│   │   └── payment_methods.json
│   ├── static/              # Static image files
│   ├── tests/               # Backend tests
│   ├── requirements.txt
│   └── pyproject.toml
├── frontend/                # React frontend
│   ├── src/
│   │   ├── api/             # API client
│   │   ├── components/      # UI components
│   │   ├── pages/           # Page components
│   │   ├── types/           # TypeScript types
│   │   └── styles/          # CSS styles
│   ├── package.json
│   └── vite.config.ts
├── scripts/
│   └── auto_run.sh          # Automation script
├── docs/                    # MkDocs documentation
│   ├── mkdocs.yml
│   └── docs/
│       └── design/          # Design specification docs
└── data/                    # JSON data files (gitignored)
```

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError` | Activate venv: `source backend/.venv/bin/activate` |
| Port 8000 in use | `lsof -i :8000` then `kill <PID>` |
| Port 5173 in use | `lsof -i :5173` then `kill <PID>` |
| Data files missing | Re-run: `cd backend && python -m app.seed` |
| CORS error | Verify backend CORS allows `http://localhost:5173` |
| Frontend blank | Check `VITE_API_URL` points to running backend |
