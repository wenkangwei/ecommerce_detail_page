# API Reference

Base URL: `http://localhost:8000/api/v1`

All responses use a unified envelope format:

```json
{
  "code": 0,
  "data": { ... },
  "message": "ok"
}
```

## Health Check

### `GET /health`

**Response:**

```json
{ "code": 0, "data": { "status": "healthy", "version": "1.0.0" }, "message": "ok" }
```

---

## Products

### `GET /api/v1/products`

List products with pagination and filtering.

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `page` | int | 1 | Page number |
| `page_size` | int | 10 | Items per page (max 50) |
| `category` | string | null | Filter by category |

### `GET /api/v1/products/{product_id}`

Get full product detail including seller, images, specs, color, and sold count.

**Response fields:** `id`, `title`, `description`, `price`, `original_price`, `currency`, `discount_percentage`, `category`, `subcategory`, `stock`, `rating_avg`, `rating_count`, `free_shipping`, `warranty_months`, `installments`, `category_path`, `seller`, `images`, `specs`, `color`, `sold_count`

### `GET /api/v1/products/{product_id}/related`

Get related products for cross-selling display.

### `GET /api/v1/products/{product_id}/brand`

Get products from the same brand.

---

## Sellers

### `GET /api/v1/sellers/{seller_id}`

Get seller profile including `sales_count`.

---

## Reviews

### `GET /api/v1/products/{product_id}/reviews`

Get paginated reviews with star distribution summary.

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `page` | int | 1 | Page number |
| `page_size` | int | 10 | Reviews per page |

---

## Payment Methods

### `GET /api/v1/payment-methods`

List all available payment methods grouped by type (credit_card, debit_card, cash).

---

## Error Codes

| Code | Meaning |
|------|---------|
| `0` | Success |
| `400` | Bad request |
| `404` | Resource not found |
| `500` | Internal server error |
