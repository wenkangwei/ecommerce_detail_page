import type { RelatedProduct } from '../types';

interface SidebarRelatedProductsProps {
  products: RelatedProduct[];
}

export default function SidebarRelatedProducts({ products }: SidebarRelatedProductsProps) {
  return (
    <div className="sidebar-related">
      <div className="sidebar-related-header">
        <h3 className="sidebar-related-title">Productos relacionados</h3>
        <span className="sidebar-related-sponsored">Patrocinado</span>
      </div>

      <div className="sidebar-related-list">
        {products.slice(0, 4).map((product) => (
          <a key={product.id} href={`/products/${product.id}`} className="sidebar-related-item">
            <div className="sidebar-related-img-wrap">
              <img src={product.image_url} alt={product.title} className="sidebar-related-img" />
            </div>
            <div className="sidebar-related-info">
              {product.discount_percentage > 0 && (
                <div className="sidebar-original-price">
                  {product.currency} {product.original_price.toLocaleString('es-AR')}
                </div>
              )}
              <div className="sidebar-price-row">
                <span className="sidebar-price">{product.currency} {product.price.toLocaleString('es-AR')}</span>
                {product.discount_percentage > 0 && (
                  <span className="sidebar-discount">{product.discount_percentage}% OFF</span>
                )}
              </div>
              <div className="sidebar-installments">
                {product.installments.count} cuotas de $ {product.installments.amount.toLocaleString('es-AR', { minimumFractionDigits: 0 })}
                {product.installments.interest_free && ' sin interés'}
              </div>
              {product.free_shipping && (
                <div className="sidebar-shipping">Envío gratis</div>
              )}
              <div className="sidebar-title">{product.title}</div>
            </div>
          </a>
        ))}
      </div>
    </div>
  );
}
