import type { ApiResponse, ProductDetail, ReviewListResponse, PaymentMethod, RelatedProduct } from '../types';

const API_BASE = import.meta.env.VITE_API_URL || '/api/v1';

async function apiFetch<T>(path: string): Promise<T> {
  const res = await fetch(`${API_BASE}${path}`);
  if (!res.ok) {
    throw new Error(`API Error: ${res.status} ${res.statusText}`);
  }
  const json: ApiResponse<T> = await res.json();
  if (json.code !== 0) {
    throw new Error(json.message);
  }
  return json.data;
}

export function fetchProduct(id: string): Promise<ProductDetail> {
  return apiFetch<ProductDetail>(`/products/${id}`);
}

export function fetchReviews(
  productId: string,
  page = 1,
  pageSize = 10,
): Promise<ReviewListResponse> {
  return apiFetch<ReviewListResponse>(
    `/products/${productId}/reviews?page=${page}&page_size=${pageSize}`,
  );
}

export function fetchPaymentMethods(): Promise<PaymentMethod[]> {
  return apiFetch<PaymentMethod[]>('/payment-methods');
}

export function fetchRelatedProducts(productId: string): Promise<RelatedProduct[]> {
  return apiFetch<RelatedProduct[]>(`/products/${productId}/related`);
}

export function fetchBrandProducts(productId: string): Promise<RelatedProduct[]> {
  return apiFetch<RelatedProduct[]>(`/products/${productId}/brand`);
}
