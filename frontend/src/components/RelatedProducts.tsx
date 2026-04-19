import type { RelatedProduct } from '../types';

interface RelatedProductsProps {
  title: string;
  products: RelatedProduct[];
}

export default function RelatedProducts({ title, products }: RelatedProductsProps) {
  return (
    <div className="related-products-section">
      <div className="related-header">
        <div>
          <h2 className="related-title">{title}</h2>
          <span className="related-sponsored">Patrocinado</span>
        </div>
      </div>

      <div className="related-grid">
        {products.slice(0, 4).map((product) => (
          <a key={product.id} href={`/products/${product.id}`} className="related-card">
            <div className="related-img-wrap">
              <img src={product.image_url} alt={product.title} className="related-img" />
            </div>
            <div className="related-info">
              {product.discount_percentage > 0 && (
                <div className="related-original-price">
                  {product.currency} {product.original_price.toLocaleString('es-AR')}
                </div>
              )}
              <div className="related-price-row">
                <span className="related-price">{product.currency} {product.price.toLocaleString('es-AR')}</span>
                {product.discount_percentage > 0 && (
                  <span className="related-discount">{product.discount_percentage}% OFF</span>
                )}
              </div>
              <div className="related-installments">
                en {product.installments.count} cuotas de $ {product.installments.amount.toLocaleString('es-AR', { minimumFractionDigits: 0 })}
                {product.installments.interest_free && ' sin interés'}
              </div>
              {product.free_shipping && (
                <div className="related-shipping">Envío gratis</div>
              )}
            </div>
          </a>
        ))}
      </div>
    </div>
  );
}
