# Usage Examples

## Fetching a Product

```bash
# Get product detail
curl http://localhost:8000/api/v1/products/1 | python3 -m json.tool

# Get product reviews
curl http://localhost:8000/api/v1/products/1/reviews | python3 -m json.tool

# List all products
curl http://localhost:8000/api/v1/products | python3 -m json.tool
```

## Navigating the UI

| URL | Page |
|-----|------|
| `http://localhost:5173` | Redirects to `/products/1` |
| `http://localhost:5173/products/1` | Samsung Galaxy A55 5G |
| `http://localhost:5173/products/2` | Apple iPhone 15 |
| `http://localhost:5173/products/3` | Samsung Galaxy Tab S9 |
| `http://localhost:5173/products/4` | Sony WH-1000XM5 |
| `http://localhost:5173/products/5` | MacBook Air M3 |
| `http://localhost:5173/products/6` | Logitech MX Master 3S |

## API Interaction Examples

### Filter by Category

```bash
curl "http://localhost:8000/api/v1/products?category=Electronics"
```

### Paginate Reviews

```bash
curl "http://localhost:8000/api/v1/products/1/reviews?page=1&page_size=5"
```

### Get Seller Profile

```bash
curl http://localhost:8000/api/v1/sellers/1
```

## Frontend Component Usage

### Using the API Client

```typescript
import { fetchProduct, fetchReviews, fetchPaymentMethods } from './api/client';

// Fetch product detail
const product = await fetchProduct('1');
console.log(product.title);        // "Samsung Galaxy A55 5G..."
console.log(product.price);         // 439.0
console.log(product.seller.name);   // "Samsung Official Store"

// Fetch reviews
const reviewData = await fetchReviews('1', 1, 10);
console.log(reviewData.summary.average);  // 4.8

// Fetch payment methods
const methods = await fetchPaymentMethods();
console.log(methods[0].name);  // "VISA"
```

### TypeScript Types

```typescript
import type { ProductDetail, ReviewData, PaymentMethod } from './types';

const product: ProductDetail = await fetchProduct('1');

// All fields are typed
product.images.forEach((img) => {
  console.log(img.url, img.alt_text);
});

product.specs.forEach((spec) => {
  console.log(`${spec.key}: ${spec.value}`);
});
```

## Running the Automation

```bash
cd ecommerce-detail

# Check current progress
./scripts/auto_run.sh --status

# See what features are pending
./scripts/auto_run.sh --dry-run

# Run all pending features
./scripts/auto_run.sh
```

## Re-seeding the Database

```bash
cd backend
source .venv/bin/activate
python -m app.seed
# Drops all tables, recreates, and inserts fresh demo data
```

## Running Tests

```bash
# Backend tests (12 tests)
cd backend
source .venv/bin/activate
python -m pytest tests/ -v

# Frontend type check
cd frontend
npx tsc --noEmit

# Frontend build
cd frontend
npm run build
```
