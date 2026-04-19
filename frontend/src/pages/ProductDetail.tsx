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

        <div className="product-main">
          {/* Left Column */}
          <div className="product-left">
            <ImageGallery images={product.images} />
            <div className="product-section">
              <h2 className="section-title">Product description</h2>
              <p className="product-description">{product.description}</p>
            </div>
            <ProductSpecs specs={product.specs} />
          </div>

          {/* Right Column */}
          <div className="product-right">
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
            <StockShipping
              stock={product.stock}
              freeShipping={product.free_shipping}
              warrantyMonths={product.warranty_months}
            />
            <SellerCard seller={product.seller} />
            <PaymentMethods methods={paymentMethods} />
          </div>
        </div>

        {/* Full-width sections */}
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
