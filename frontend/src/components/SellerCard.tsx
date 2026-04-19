import type { SellerBrief } from '../types';

interface SellerCardProps {
  seller: SellerBrief;
}

export default function SellerCard({ seller }: SellerCardProps) {
  return (
    <div className="seller-card">
      <div className="seller-banner">Tienda Oficial</div>

      <div className="seller-info">
        <h3 className="seller-name">{seller.name}</h3>
        <div className="seller-official-row">
          <span className="seller-check">{'\u2713'}</span>
          <span>Tienda oficial de Mercado Libre</span>
        </div>
        <div className="seller-products-row">
          <span className="seller-products-count">+90</span>
          <span className="seller-products-label">Productos</span>
        </div>
      </div>

      <div className="seller-stats">
        <div className="seller-stat">
          <span className="stat-value">+5mil</span>
          <span className="stat-label">Ventas concretadas</span>
        </div>
        <div className="seller-stat">
          <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="#666" strokeWidth="2">
            <path d="M3 18v-6a9 9 0 0 1 18 0v6"/><path d="M21 19a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3zM3 19a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H3z"/>
          </svg>
          <span className="stat-label">Brinda buena atención</span>
        </div>
        <div className="seller-stat">
          <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="#666" strokeWidth="2">
            <rect x="1" y="3" width="15" height="13" rx="1"/><path d="M16 8h4l3 3v5h-7V8z"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/>
          </svg>
          <span className="stat-label">Entrega sus productos a tiempo</span>
        </div>
      </div>

      <a href={`/tienda/${seller.id}`} className="seller-store-btn">
        Ir a la Tienda oficial
      </a>

      <div className="seller-other">
        <h4 className="seller-other-title">Otras opciones de compra</h4>
        <a href="#opciones" className="seller-other-link">Ver 3 opciones desde US$ 439</a>
      </div>
    </div>
  );
}
