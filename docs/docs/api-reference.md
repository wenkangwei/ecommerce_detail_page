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

Check if the API is running.

**Response:**

```json
{
  "code": 0,
  "data": {
    "status": "healthy",
    "version": "1.0.0"
  },
  "message": "ok"
}
```

---

## Products

### `GET /api/v1/products`

List products with pagination and filtering.

**Query Parameters:**

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `page` | int | 1 | Page number |
| `page_size` | int | 10 | Items per page (max 50) |
| `category` | string | null | Filter by category |

**Response:**

```json
{
  "code": 0,
  "data": {
    "items": [
      {
        "id": 1,
        "title": "Samsung Galaxy A55 5G...",
        "price": 439.0,
        "currency": "US$",
        "thumbnail": "/static/images/...",
        "category": "Electronics",
        "rating_avg": 4.8,
        "rating_count": 950,
        "free_shipping": true
      }
    ],
    "pagination": {
      "page": 1,
      "page_size": 10,
      "total": 6,
      "total_pages": 1
    }
  }
}
```

### `GET /api/v1/products/{product_id}`

Get full product detail including seller, images, and specs.

**Response:** See [Product Detail Schema](#product-detail-schema)

---

## Sellers

### `GET /api/v1/sellers/{seller_id}`

Get seller profile.

**Response:**

```json
{
  "code": 0,
  "data": {
    "id": 1,
    "name": "Samsung Official Store",
    "is_official": true,
    "reputation": "MercadoLíder Platinum",
    "location": "Montevideo, Uruguay",
    "logo_url": "/static/images/sellers/samsung.png",
    "product_count": 2,
    "created_at": "2026-01-01T00:00:00"
  }
}
```

---

## Reviews

### `GET /api/v1/products/{product_id}/reviews`

Get paginated reviews with summary statistics.

**Query Parameters:**

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `page` | int | 1 | Page number |
| `page_size` | int | 10 | Reviews per page |

**Response:**

```json
{
  "code": 0,
  "data": {
    "items": [
      {
        "id": 1,
        "user_name": "Juan P.",
        "rating": 5,
        "title": "Excellent phone!",
        "content": "Great value for money...",
        "date": "2025-12-15"
      }
    ],
    "pagination": { "page": 1, "page_size": 10, "total": 950, "total_pages": 95 },
    "summary": {
      "average": 4.8,
      "distribution": {
        "star_5": 680,
        "star_4": 200,
        "star_3": 45,
        "star_2": 15,
        "star_1": 10
      }
    }
  }
}
```

---

## Payment Methods

### `GET /api/v1/payment-methods`

List all available payment methods.

**Response:**

```json
{
  "code": 0,
  "data": [
    {
      "id": 1,
      "name": "VISA",
      "type": "credit_card",
      "icon_url": "/static/images/payments/visa.svg",
      "max_installments": 12
    }
  ]
}
```

---

## Error Codes

| Code | Meaning |
|------|---------|
| `0` | Success |
| `400` | Bad request |
| `404` | Resource not found |
| `500` | Internal server error |

## Product Detail Schema

The full product detail response includes:

| Field | Type | Description |
|-------|------|-------------|
| `id` | int | Product ID |
| `title` | string | Full product title |
| `description` | string | Detailed description |
| `price` | float | Current sale price |
| `original_price` | float | Original price before discount |
| `currency` | string | Currency symbol (e.g., "US$") |
| `discount_percentage` | int | Discount percentage |
| `category` | string | Main category |
| `subcategory` | string | Subcategory |
| `stock` | int | Available stock count |
| `rating_avg` | float | Average rating (1-5) |
| `rating_count` | int | Total review count |
| `free_shipping` | bool | Free shipping available |
| `warranty_months` | int | Warranty period |
| `installments` | object | Installment plan info |
| `category_path` | array | Breadcrumb path |
| `seller` | object | Seller information |
| `images` | array | Product images |
| `specs` | array | Key-value specifications |
