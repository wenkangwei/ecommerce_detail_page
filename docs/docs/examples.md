# Usage Examples

## API Requests

```bash
# Get product detail
curl http://localhost:8000/api/v1/products/1 | python3 -m json.tool

# Get related products
curl http://localhost:8000/api/v1/products/1/related | python3 -m json.tool

# Get brand products (Samsung)
curl http://localhost:8000/api/v1/products/1/brand | python3 -m json.tool

# Get product reviews
curl http://localhost:8000/api/v1/products/1/reviews | python3 -m json.tool

# List all products
curl http://localhost:8000/api/v1/products | python3 -m json.tool
```

## Available Product Pages

| URL | Product |
|-----|---------|
| `http://localhost:5173/products/1` | Samsung Galaxy A55 5G |
| `http://localhost:5173/products/2` | Apple iPhone 15 |
| `http://localhost:5173/products/3` | Samsung Galaxy Tab S9 |
| `http://localhost:5173/products/4` | Sony WH-1000XM5 |
| `http://localhost:5173/products/5` | MacBook Air M3 |
| `http://localhost:5173/products/6` | Logitech MX Master 3S |

## Frontend API Client

```typescript
import { fetchProduct, fetchRelatedProducts, fetchBrandProducts } from './api/client';

const product = await fetchProduct('1');
console.log(product.title);          // "Samsung Galaxy A55 5G..."
console.log(product.color);           // "Azul oscuro"
console.log(product.sold_count);      // 500
console.log(product.seller.sales_count); // "+5mil ventas"

const related = await fetchRelatedProducts('1');
console.log(related.length);         // 4

const brand = await fetchBrandProducts('1');
console.log(brand.length);           // 2
```

## Re-seeding Data

```bash
cd backend
source .venv/bin/activate
python -m app.seed
```

## Running Tests

```bash
# Backend tests
cd backend && source .venv/bin/activate && python -m pytest tests/ -v

# Frontend type check
cd frontend && npx tsc --noEmit

# Frontend build
cd frontend && npm run build
```
