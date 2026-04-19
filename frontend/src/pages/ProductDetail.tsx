import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { fetchProduct, fetchReviews, fetchPaymentMethods } from '../api/client';
import type { ProductDetail, ReviewListResponse, PaymentMethod } from '../types';
import Breadcrumb from '../components/Breadcrumb';
import ImageGallery from '../components/ImageGallery';
import PriceBlock from '../components/PriceBlock';
import StockShipping from '../components/StockShipping';
import SellerCard from '../components/SellerCard';
import PaymentMethods from '../components/PaymentMethods';
import ProductSpecs from '../components/ProductSpecs';
import ReviewsSection from '../components/ReviewsSection';

export default function ProductDetailPage() {
  const { id } = useParams<{ id: string }>();

  const [product, setProduct] = useState<ProductDetail | null>(null);
  const [reviewData, setReviewData] = useState<ReviewListResponse | null>(null);
  const [paymentMethods, setPaymentMethods] = useState<PaymentMethod[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!id) return;
    setLoading(true);
    setError(null);

    Promise.all([fetchProduct(id), fetchReviews(id), fetchPaymentMethods()])
      .then(([prod, revs, payments]) => {
        setProduct(prod);
        setReviewData(revs);
        setPaymentMethods(payments);
      })
      .catch((err) => setError(err.message))
      .finally(() => setLoading(false));
  }, [id]);

  if (loading) {
    return (
      <div className="page-loading">
        <div className="loading-spinner" />
        <p>Loading product details...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="page-error">
        <h2>Oops! Something went wrong</h2>
        <p>{error}</p>
        <button onClick={() => window.location.reload()}>Try Again</button>
      </div>
    );
  }

  if (!product) return null;

  return (
    <div className="product-page">
      <div className="product-container">
        <Breadcrumb items={product.category_path} productName={product.title} />

        {/* ── Main 3-column layout ────────────────────── */}
        <div className="product-main">
          {/* Column 1: Image Gallery (thumbnails + main image) */}
          <div className="product-col-gallery">
            <ImageGallery images={product.images} />
          </div>

          {/* Column 2: Product Information */}
          <div className="product-col-info">
            {product.seller.is_official && (
              <div className="info-official-badge">
                <span className="badge-icon">★</span> Official {product.seller.name}
              </div>
            )}

            <h1 className="product-title">{product.title}</h1>

            <div className="product-rating">
              <span className="stars">{'★'.repeat(Math.round(product.rating_avg))}{'☆'.repeat(5 - Math.round(product.rating_avg))}</span>
              <span className="rating-value">{product.rating_avg}</span>
              <span className="rating-count">({product.rating_count} reviews)</span>
            </div>

            <PriceBlock
              price={product.price}
              originalPrice={product.original_price}
              currency={product.currency}
              discountPercentage={product.discount_percentage}
              installments={product.installments}
            />

            <div className="info-highlights">
              <ul>
                {product.specs.slice(0, 3).map((s, i) => (
                  <li key={i}><span className="hl-icon">✓</span> <strong>{s.key}:</strong> {s.value}</li>
                ))}
              </ul>
            </div>

            <a href="#specs" className="view-chars-link">View characteristics</a>
          </div>

          {/* Column 3: Purchase Panel */}
          <div className="product-col-purchase">
            <StockShipping
              stock={product.stock}
              freeShipping={product.free_shipping}
              warrantyMonths={product.warranty_months}
            />

            <div className="purchase-actions">
              <button className="btn-buy-now">Buy now</button>
              <button className="btn-add-cart">Add to cart</button>
            </div>

            <SellerCard seller={product.seller} />

            <div className="purchase-protection">
              <div className="protect-item">
                <span className="protect-icon">🛡️</span>
                <div>
                  <span className="protect-title">Buyer protection</span>
                  <span className="protect-desc">Receive the product or get your money back</span>
                </div>
              </div>
              <div className="protect-item">
                <span className="protect-icon">🔄</span>
                <div>
                  <span className="protect-title">Free returns</span>
                  <span className="protect-desc">30 days to return</span>
                </div>
              </div>
              <div className="protect-item">
                <span className="protect-icon">🏆</span>
                <div>
                  <span className="protect-title">Factory warranty</span>
                  <span className="protect-desc">{product.warranty_months} months</span>
                </div>
              </div>
            </div>

            <PaymentMethods methods={paymentMethods} />
          </div>
        </div>

        {/* ── Below main content ──────────────────────── */}
        <div id="specs">
          <ProductSpecs specs={product.specs} />
        </div>

        <div className="product-section">
          <h2 className="section-title">Product description</h2>
          <p className="product-description">{product.description}</p>
        </div>

        {reviewData && (
          <ReviewsSection
            reviews={reviewData.items}
            summary={reviewData.summary}
            pagination={reviewData.pagination}
          />
        )}
      </div>
    </div>
  );
}
