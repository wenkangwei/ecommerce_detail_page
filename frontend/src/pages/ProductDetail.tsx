import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { fetchProduct, fetchReviews, fetchPaymentMethods, fetchRelatedProducts, fetchBrandProducts } from '../api/client';
import type { ProductDetail, ReviewListResponse, PaymentMethod, RelatedProduct } from '../types';
import TopBar from '../components/TopBar';
import Breadcrumb from '../components/Breadcrumb';
import ImageGallery from '../components/ImageGallery';
import ProductInfo from '../components/ProductInfo';
import PurchasePanel from '../components/PurchasePanel';
import SellerCard from '../components/SellerCard';
import PaymentMethods from '../components/PaymentMethods';
import ProductSpecs from '../components/ProductSpecs';
import ProductDescription from '../components/ProductDescription';
import RelatedProducts from '../components/RelatedProducts';
import SidebarRelatedProducts from '../components/SidebarRelatedProducts';
import ReviewsSection from '../components/ReviewsSection';

export default function ProductDetailPage() {
  const { id } = useParams<{ id: string }>();

  const [product, setProduct] = useState<ProductDetail | null>(null);
  const [reviewData, setReviewData] = useState<ReviewListResponse | null>(null);
  const [relatedProducts, setRelatedProducts] = useState<RelatedProduct[]>([]);
  const [brandProducts, setBrandProducts] = useState<RelatedProduct[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!id) return;
    setLoading(true);
    setError(null);

    Promise.all([fetchProduct(id), fetchReviews(id), fetchRelatedProducts(id), fetchBrandProducts(id)])
      .then(([prod, revs, related, brand]) => {
        setProduct(prod);
        setReviewData(revs);
        setRelatedProducts(related);
        setBrandProducts(brand);
      })
      .catch((err) => setError(err.message))
      .finally(() => setLoading(false));
  }, [id]);

  if (loading) {
    return (
      <div className="page-loading">
        <div className="loading-spinner" />
        <p>Cargando producto...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="page-error">
        <h2>Oops! Algo salió mal</h2>
        <p>{error}</p>
        <button onClick={() => window.location.reload()}>Reintentar</button>
      </div>
    );
  }

  if (!product) return null;

  return (
    <div className="product-page">
      <TopBar />

      <div className="product-container">
        <Breadcrumb items={product.category_path} productName={product.title} />

        <div className="main-card">
          <div className="product-main">
            <div className="product-col-gallery">
              <ImageGallery images={product.images} />
            </div>

            <div className="product-col-info">
              <ProductInfo product={product} />
            </div>

            <div className="product-col-purchase">
              <PurchasePanel product={product} />
              <SellerCard seller={product.seller} />
              <PaymentMethods />
            </div>
          </div>
        </div>

        <div className="below-main">
          <div className="below-main-left">
            {relatedProducts.length > 0 && (
              <RelatedProducts title="Productos relacionados" products={relatedProducts} />
            )}

            {brandProducts.length > 0 && (
              <RelatedProducts title={`Productos de ${product.seller.name}`} products={brandProducts} />
            )}

            <div id="caracteristicas">
              <ProductSpecs specs={product.specs} />
            </div>

            <ProductDescription description={product.description} />

            {reviewData && (
              <div id="reviews">
                <ReviewsSection
                  reviews={reviewData.items}
                  summary={reviewData.summary}
                  pagination={reviewData.pagination}
                />
              </div>
            )}
          </div>

          <div className="below-main-right">
            <SidebarRelatedProducts products={relatedProducts} />
          </div>
        </div>
      </div>
    </div>
  );
}
