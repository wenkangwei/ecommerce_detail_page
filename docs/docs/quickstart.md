# Quick Start Guide

Get the e-commerce detail page running locally in under 5 minutes.

## Prerequisites

- Python 3.10+
- Node.js 18+
- npm 9+

## One-Command Start

```bash
cd ecommerce-detail
chmod +x init.sh
./init.sh
```

This starts both the backend (port 8000) and frontend (port 5173).

## Manual Setup

### 1. Backend

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m app.seed        # Seed demo data + download images
uvicorn app.main:app --port 8000 --reload
```

### 2. Frontend

```bash
cd frontend
npm install
npm run dev
```

### 3. Open in Browser

Navigate to **http://localhost:5173** — you'll be redirected to `/products/1` (Samsung Galaxy A55).

## Demo Products

| URL | Product |
|-----|---------|
| `http://localhost:5173/products/1` | Samsung Galaxy A55 5G |
| `http://localhost:5173/products/2` | Apple iPhone 15 |
| `http://localhost:5173/products/3` | Samsung Galaxy Tab S9 |
| `http://localhost:5173/products/4` | Sony WH-1000XM5 |
| `http://localhost:5173/products/5` | MacBook Air M3 |
| `http://localhost:5173/products/6` | Logitech MX Master 3S |

## Verify

```bash
# Backend health check
curl http://localhost:8000/health

# Product API
curl http://localhost:8000/api/v1/products/1 | python3 -m json.tool

# Related products
curl http://localhost:8000/api/v1/products/1/related | python3 -m json.tool

# Backend tests
cd backend && source .venv/bin/activate && python -m pytest tests/ -v
```

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `VITE_API_URL` | `/api/v1` | Backend API base URL (frontend) |
