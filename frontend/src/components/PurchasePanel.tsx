import { useState } from 'react';
import type { ProductDetail } from '../types';

interface PurchasePanelProps {
  product: ProductDetail;
}

export default function PurchasePanel({ product }: PurchasePanelProps) {
  const [qty, setQty] = useState(1);
  const maxQty = Math.min(product.stock, 6);

  return (
    <div className="purchase-panel">
      {product.free_shipping && (
        <div className="panel-shipping">
          <div className="shipping-main">
            <svg className="shipping-icon" viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="#00a650" strokeWidth="2">
              <rect x="1" y="3" width="15" height="13" rx="1"/><path d="M16 8h4l3 3v5h-7V8z"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/>
            </svg>
            <div>
              <div className="shipping-title">Envío gratis a todo el país</div>
              <a href="#envio" className="shipping-link">Conoce los tiempos y las formas de envío.</a>
            </div>
          </div>
          <a href="#envio" className="shipping-calc">Calcular cuándo llega</a>
        </div>
      )}

      <div className="panel-stock">
        <span className="stock-label">Stock disponible</span>
      </div>

      <div className="panel-quantity">
        <span className="qty-label">Cantidad:</span>
        <div className="qty-selector">
          <button className="qty-btn" onClick={() => setQty(Math.max(1, qty - 1))} disabled={qty <= 1}>−</button>
          <span className="qty-value">{qty} unidad{qty > 1 ? 'es' : ''}</span>
          <button className="qty-btn" onClick={() => setQty(Math.min(maxQty, qty + 1))} disabled={qty >= maxQty}>+</button>
        </div>
        <span className="qty-available">({maxQty} disponibles)</span>
      </div>

      <div className="panel-actions">
        <button className="btn-buy-now">Comprar ahora</button>
        <button className="btn-add-cart">Agregar al carrito</button>
      </div>

      <div className="panel-protection">
        <div className="protect-item">
          <svg className="protect-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#3483fa" strokeWidth="2">
            <path d="M1 4v6h6v-6h-6zM17 4v6h6v-6h-6zM7 12h10M17 7h6M1 7h6"/>
          </svg>
          <div>
            <a href="#devolucion" className="protect-link">Devolución gratis.</a>
            <span className="protect-text"> Tienes 30 días desde que lo recibes.</span>
          </div>
        </div>

        <div className="protect-item">
          <svg className="protect-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#3483fa" strokeWidth="2">
            <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
          </svg>
          <div>
            <a href="#compra-protegida" className="protect-link">Compra Protegida,</a>
            <span className="protect-text"> recibe el producto que esperabas o te devolvemos tu dinero.</span>
          </div>
        </div>

        <div className="protect-item">
          <svg className="protect-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#666" strokeWidth="2">
            <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
          </svg>
          <span className="protect-text">{product.warranty_months} meses de garantía de fábrica.</span>
        </div>
      </div>
    </div>
  );
}
