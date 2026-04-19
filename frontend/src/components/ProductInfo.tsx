import type { ProductDetail } from '../types';
import PriceBlock from './PriceBlock';

interface ProductInfoProps {
  product: ProductDetail;
}

export default function ProductInfo({ product }: ProductInfoProps) {
  return (
    <div className="product-info">
      {product.seller.is_official && (
        <a href="#tienda" className="info-store-link">
          Visita la Tienda oficial de {product.seller.name}
          <span className="info-store-check">{'\u2713'}</span>
        </a>
      )}

      <div className="info-meta">
        <span>Nuevo</span>
        <span className="info-meta-sep">|</span>
        <span>{product.sold_count ? `+${product.sold_count} vendidos` : '+500 vendidos'}</span>
      </div>

      <div className="info-best-seller">
        <span className="best-seller-badge">MÁS VENDIDO</span>
        <span className="best-seller-rank">8º en Celulares y Smartphones</span>
      </div>

      <h1 className="product-title">{product.title}</h1>

      <div className="product-rating">
        <span className="rating-number">{product.rating_avg}</span>
        <span className="stars">{'★'.repeat(Math.round(product.rating_avg))}{'☆'.repeat(5 - Math.round(product.rating_avg))}</span>
        <a href="#reviews" className="rating-count">({product.rating_count})</a>
      </div>

      <PriceBlock
        price={product.price}
        originalPrice={product.original_price}
        currency={product.currency}
        discountPercentage={product.discount_percentage}
        installments={product.installments}
      />

      <div className="info-oca-badge">
        <span className="oca-discount">10% OFF</span> OCA Blue Visa
      </div>

      {product.color && (
        <div className="info-color">
          <span>Color: </span>
          <span className="info-color-value">{product.color}</span>
        </div>
      )}

      <div className="info-key-specs">
        <h3 className="key-specs-title">Lo que tienes que saber de este producto</h3>
        <ul className="key-specs-list">
          <li>
            <span className="key-specs-bullet">{'\u2022'}</span>
            <span>Memoria RAM: {product.specs.find(s => s.key.includes('RAM') || s.key.includes('Memoria RAM'))?.value || '8 GB'}</span>
          </li>
          <li>
            <span className="key-specs-bullet">{'\u2022'}</span>
            <span>Dispositivo desbloqueado para que elijas tu compañía telefónica preferida.</span>
          </li>
          <li>
            <span className="key-specs-bullet">{'\u2022'}</span>
            <span>Memoria interna de {product.specs.find(s => s.key.includes('interna'))?.value || '256 GB'}.</span>
          </li>
        </ul>
      </div>

      <a href="#caracteristicas" className="view-chars-link">Ver características</a>

      <div className="info-purchase-options">
        <h3 className="purchase-opt-title">Opciones de compra:</h3>
        <a href="#opciones" className="purchase-opt-link">
          3 productos nuevos desde {product.currency} {product.price}
        </a>
      </div>
    </div>
  );
}
