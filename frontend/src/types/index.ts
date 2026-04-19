// ─── API Response Types ───────────────────────────────────────

export interface ApiResponse<T> {
  code: number;
  data: T;
  message: string;
}

// ─── Seller ───────────────────────────────────────────────────

export interface SellerBrief {
  id: number;
  name: string;
  is_official: boolean;
  reputation: string;
  location: string;
  logo_url: string;
  sales_count?: string;
}

// ─── Product ──────────────────────────────────────────────────

export interface ProductImage {
  id: number;
  url: string;
  alt_text: string;
}

export interface ProductSpec {
  key: string;
  value: string;
  icon?: string;
}

export interface CategoryItem {
  id: number;
  name: string;
  slug: string;
}

export interface InstallmentInfo {
  count: number;
  amount: number;
  interest_free: boolean;
}

export interface ProductDetail {
  id: number;
  title: string;
  description: string;
  price: number;
  original_price: number;
  currency: string;
  discount_percentage: number;
  category: string;
  subcategory: string;
  stock: number;
  rating_avg: number;
  rating_count: number;
  free_shipping: boolean;
  warranty_months: number;
  installments: InstallmentInfo;
  category_path: CategoryItem[];
  seller: SellerBrief;
  images: ProductImage[];
  specs: ProductSpec[];
  color?: string;
  sold_count?: number;
}

// ─── Related Product ──────────────────────────────────────────

export interface RelatedProduct {
  id: number;
  title: string;
  price: number;
  original_price: number;
  currency: string;
  discount_percentage: number;
  image_url: string;
  installments: InstallmentInfo;
  free_shipping: boolean;
}

// ─── Review ───────────────────────────────────────────────────

export interface ReviewData {
  id: number;
  user_name: string;
  rating: number;
  title: string;
  content: string;
  date: string;
}

export interface ReviewDistribution {
  star_5: number;
  star_4: number;
  star_3: number;
  star_2: number;
  star_1: number;
}

export interface ReviewSummary {
  average: number;
  distribution: ReviewDistribution;
}

export interface ReviewListResponse {
  items: ReviewData[];
  pagination: { page: number; page_size: number; total: number; total_pages: number };
  summary: ReviewSummary;
}

// ─── Payment Method ───────────────────────────────────────────

export interface PaymentMethod {
  id: number;
  name: string;
  type: string;
  icon_url: string;
  max_installments: number;
}
