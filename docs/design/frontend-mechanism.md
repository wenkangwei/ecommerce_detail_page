# Frontend Mechanism Design

> This document describes the frontend architecture, data flow, state management, routing, and component interaction patterns.

---

## 1. Architecture Overview

```
┌─────────────────────────────────────────────────────┐
│                   React Application                  │
│                                                      │
│  ┌──────────┐    ┌──────────────┐    ┌───────────┐ │
│  │  Router   │───▶│  Page Layer  │───▶│ Components│ │
│  │ (React    │    │ ProductDetail│    │ (Section  │ │
│  │  Router)  │    │    Page      │    │  Widgets) │ │
│  └──────────┘    └──────┬───────┘    └───────────┘ │
│                         │                            │
│  ┌──────────────────────▼────────────────────────┐  │
│  │              API Client Layer                  │  │
│  │         (fetch wrapper + types)                │  │
│  └──────────────────────┬────────────────────────┘  │
│                         │                            │
└─────────────────────────┼────────────────────────────┘
                          │ HTTP GET
                          ▼
              ┌─────────────────────┐
              │   FastAPI Backend   │
              │   localhost:8000    │
              └─────────────────────┘
```

---

## 2. Routing

### Route Definition

| Path | Page | Description |
|------|------|-------------|
| `/` | Redirect | Redirects to `/products/1` |
| `/products/:id` | `ProductDetailPage` | Main product detail page |

### Implementation

Use **React Router v6** with a single dynamic route:

```tsx
// App.tsx
<BrowserRouter>
  <Routes>
    <Route path="/" element={<Navigate to="/products/1" replace />} />
    <Route path="/products/:id" element={<ProductDetailPage />} />
  </Routes>
</BrowserRouter>
```

No nested routing needed — this is a single-page detail view.

---

## 3. Data Flow

### Fetch Sequence

When user navigates to `/products/1`:

```
ProductDetailPage (mount)
    │
    ├──▶ fetchProduct(1)           // GET /api/v1/products/1
    │       │
    │       └──▶ { product, seller, images, specs, stock }
    │
    ├──▶ fetchReviews(1)           // GET /api/v1/products/1/reviews
    │       │
    │       └──▶ { reviews[], pagination }
    │
    └──▶ fetchPaymentMethods()     // GET /api/v1/payment-methods
            │
            └──▶ { methods[] }
```

All three API calls fire **in parallel** on mount via `Promise.all()`.

### State Shape

```tsx
// Single page state — no Redux needed
interface PageState {
  loading: boolean;
  error: string | null;

  product: ProductData | null;
  reviews: ReviewData[];
  reviewPagination: { page: number; total: number };
  paymentMethods: PaymentMethodData[];
}
```

### State Management Pattern

Use **React hooks** (useState + useEffect). No external state library needed for a single detail page.

```tsx
function ProductDetailPage() {
  const { id } = useParams<{ id: string }>();

  const [product, setProduct] = useState<ProductData | null>(null);
  const [reviews, setReviews] = useState<ReviewData[]>([]);
  const [paymentMethods, setPaymentMethods] = useState<PaymentMethodData[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    loadData(id);
  }, [id]);

  async function loadData(productId: string) {
    setLoading(true);
    setError(null);
    try {
      const [productRes, reviewsRes, paymentsRes] = await Promise.all([
        fetchProduct(productId),
        fetchReviews(productId),
        fetchPaymentMethods(),
      ]);
      setProduct(productRes);
      setReviews(reviewsRes.items);
      setPaymentMethods(paymentsRes);
    } catch (err) {
      setError('Failed to load product details');
    } finally {
      setLoading(false);
    }
  }
}
```

---

## 4. Component Tree

```
ProductDetailPage
├── Breadcrumb                    ← category_path from product
│   └── CrumbItem[]               ← each: { label, href }
│
├── <ThreeColumnLayout>           ← CSS Grid: 440px | 1fr | 320px
│   ├── <Column1: Gallery>
│   │   └── ImageGallery          ← product.images[]
│   │       ├── ThumbsVertical    ← vertical strip, 52px wide, hover-to-switch
│   │       └── MainImage         ← images[selectedIdx], counter overlay
│   │
│   ├── <Column2: Product Info>
│   │   ├── OfficialBadge         ← conditional: "★ Official {seller.name}"
│   │   ├── ProductTitle          ← h1, 22px
│   │   ├── ProductRating         ← stars + number + review count link
│   │   ├── PriceBlock            ← current/original/discount/installments
│   │   ├── InfoHighlights        ← top 3 specs with ✓ icons
│   │   └── ViewCharsLink         ← anchor to #specs section
│   │
│   └── <Column3: Purchase Panel>
│       ├── StockShipping         ← free shipping badge + stock dot + quantity
│       │   ├── ShippingBadge     ← truck SVG + "Free shipping" (green bg)
│       │   ├── StockInfo         ← green dot + "In stock" + qty available
│       │   └── QuantityRow       ← "Quantity: 1 unit"
│       ├── PurchaseActions       ← "Buy now" + "Add to cart" buttons
│       ├── SellerCard            ← official badge + name + sales + link
│       ├── BuyerProtection       ← 3 items: 🛡️🔄🏆
│       └── PaymentMethods        ← installment banner + card icons + expand
│
├── ProductSpecs                  ← product.specs[], expandable 2-col grid
│   ├── SpecsGrid                 ← 2-column CSS Grid
│   └── ExpandButton              ← "View all characteristics"
│
├── ProductDescription            ← product.description, full width
│
└── ReviewsSection                ← reviews[]
    ├── ReviewSummary             ← average, total, distribution (sticky left)
    │   ├── AverageDisplay        ← 48px number + stars
    │   └── StarDistribution      ← bar chart: 5★ to 1★
    └── ReviewCard[]              ← individual reviews (right column)
        ├── UserInfo              ← avatar, name, date
        ├── RatingStars
        ├── ReviewTitle
        └── ReviewContent
```

---

## 5. Component Props Interfaces

```tsx
// ─── Data Types (from API) ─────────────────────────────

interface ProductData {
  id: number;
  title: string;
  description: string;
  price: number;
  original_price: number;
  currency: string;              // "US$", "$", etc.
  discount_percentage: number;   // 12
  installments: {
    count: number;               // 10
    amount: number;              // 43.90
    interest_free: boolean;
  };
  stock: {
    available: number;
    label: string;               // "In Stock"
  };
  shipping: {
    free: boolean;
    estimated_days: [number, number]; // [4, 7]
    to_country: boolean;
  };
  rating: {
    average: number;             // 4.8
    count: number;               // 950
  };
  images: ProductImage[];
  category_path: CategoryItem[];
  specs: SpecItem[];
  seller: SellerSummary;
}

interface ProductImage {
  id: number;
  url: string;
  alt: string;
}

interface CategoryItem {
  id: number;
  name: string;
  slug: string;                  // for URL
}

interface SpecItem {
  key: string;                   // "Screen Size"
  value: string;                 // "6.6 inches"
}

interface SellerSummary {
  id: number;
  name: string;
  is_official: boolean;
  reputation: string;            // "MercadoLíder Platinum"
  location: string;
  logo_url: string;
}

interface ReviewData {
  id: number;
  user: string;
  rating: number;                // 1-5
  title: string;
  content: string;
  date: string;                  // ISO date
}

interface ReviewListResponse {
  items: ReviewData[];
  pagination: {
    page: number;
    page_size: number;
    total: number;
  };
  summary: {
    average: number;
    distribution: Record<number, number>; // {5: 680, 4: 200, ...}
  };
}

interface PaymentMethodData {
  id: number;
  name: string;                  // "VISA"
  type: "credit_card" | "debit_card" | "digital_wallet";
  icon_url: string;
  installments_available: number; // max installments
}

// ─── Component Props ───────────────────────────────────

interface BreadcrumbProps {
  items: CategoryItem[];
  productName: string;
}

interface ImageGalleryProps {
  images: ProductImage[];
}

interface PriceBlockProps {
  price: number;
  originalPrice: number;
  currency: string;
  discountPercentage: number;
  installments: { count: number; amount: number; interest_free: boolean };
}

interface StockShippingProps {
  stock: number;
  freeShipping: boolean;
  warrantyMonths: number;
}

interface SellerCardProps {
  seller: SellerBrief;
}

interface PaymentMethodsProps {
  methods: PaymentMethod[];
}

interface ProductSpecsProps {
  specs: SpecItem[];
}

interface ReviewsSectionProps {
  reviews: ReviewData[];
  summary: ReviewListResponse['summary'];
  pagination: ReviewListResponse['pagination'];
}
```

---

## 6. API Client Layer

### Base Configuration

```tsx
// src/api/client.ts
const API_BASE = import.meta.env.VITE_API_URL || 'http://localhost:8000/api/v1';

async function apiFetch<T>(path: string): Promise<T> {
  const res = await fetch(`${API_BASE}${path}`);
  if (!res.ok) {
    throw new Error(`API Error: ${res.status} ${res.statusText}`);
  }
  const json = await res.json();
  return json.data;  // unwrap { code, data, message }
}
```

### API Functions

```tsx
export function fetchProduct(id: string): Promise<ProductData> {
  return apiFetch<ProductData>(`/products/${id}`);
}

export function fetchReviews(
  productId: string,
  page = 1,
  pageSize = 10
): Promise<ReviewListResponse> {
  return apiFetch<ReviewListResponse>(
    `/products/${productId}/reviews?page=${page}&page_size=${pageSize}`
  );
}

export function fetchPaymentMethods(): Promise<PaymentMethodData[]> {
  return apiFetch<PaymentMethodData[]>('/payment-methods');
}
```

---

## 7. Loading & Error States

### Loading State
- **Skeleton loader** for each section (gray pulsing rectangles matching component shape)
- Image gallery: gray rectangle with camera icon
- Price block: gray bars
- All sections appear as skeletons until data arrives

### Error State
- **Error banner** at top of page: "Failed to load product. Please try again."
- **Retry button** in the banner
- Individual section errors: show section with "Unavailable" text

### Empty State
- Product not found (404): "Product not found" page with link to home

---

## 8. Interaction Patterns

| Interaction | Behavior |
|-------------|----------|
| Click thumbnail | Update main image with fade transition (300ms) |
| Click "See more" (description) | Expand full description, smooth height transition |
| Click "See all specifications" | Expand full spec table |
| Click "See all payment methods" | Expand payment method details |
| Click "Load more reviews" | Fetch next page, append to list |
| Click star distribution bar | Scroll to reviews section, highlight that star level |
| Resize window | Layout reflows at breakpoints (768px, 1024px) |

---

## 9. Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `VITE_API_URL` | `http://localhost:8000/api/v1` | Backend API base URL |

---

## 10. File Organization

```
frontend/src/
├── main.tsx                     # Entry point
├── App.tsx                      # Router setup
├── api/
│   └── client.ts                # API functions + fetch wrapper
├── components/
│   ├── Breadcrumb.tsx
│   ├── ImageGallery.tsx
│   ├── PriceBlock.tsx
│   ├── StockShipping.tsx
│   ├── SellerCard.tsx
│   ├── PaymentMethods.tsx
│   ├── ProductSpecs.tsx
│   ├── ReviewCard.tsx
│   ├── ReviewSummary.tsx
│   └── LoadingSkeleton.tsx
├── pages/
│   └── ProductDetail.tsx        # Main page, orchestrates components
├── types/
│   └── index.ts                 # All TypeScript interfaces
└── styles/
    └── product.css              # Global styles for the detail page
```

Each component file is self-contained: markup + any component-specific styles (CSS class names reference the global stylesheet).
