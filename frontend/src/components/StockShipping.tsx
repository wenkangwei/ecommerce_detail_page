import { useState } from 'react';

interface StockShippingProps {
  stock: number;
  freeShipping: boolean;
  warrantyMonths: number;
}

export default function StockShipping({ stock, freeShipping, warrantyMonths }: StockShippingProps) {
  const [qty, setQty] = useState(1);
  const maxQty = Math.min(stock, 10);

  return (
    <div className="purchase-shipping">
      {freeShipping && (
        <div className="shipping-badge">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#00a650" strokeWidth="2">
            <rect x="1" y="3" width="15" height="13" rx="1"/><path d="M16 8h4l3 3v5h-7V8z"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/>
          </svg>
          <span className="shipping-free-text">Free shipping</span>
        </div>
      )}
      <div className="stock-info">
        <span className={`stock-dot ${stock > 0 ? 'in-stock' : 'out-stock'}`} />
        <span className="stock-text">{stock > 0 ? 'In stock' : 'Out of stock'}</span>
        {stock > 0 && stock <= 5 && <span className="stock-qty">Only {stock} available</span>}
      </div>
      {stock > 0 && (
        <div className="quantity-row">
          <span className="qty-label">Quantity:</span>
          <div className="qty-selector">
            <button
              className="qty-btn"
              onClick={() => setQty(Math.max(1, qty - 1))}
              disabled={qty <= 1}
              aria-label="Decrease quantity"
            >−</button>
            <span className="qty-value">{qty}</span>
            <button
              className="qty-btn"
              onClick={() => setQty(Math.min(maxQty, qty + 1))}
              disabled={qty >= maxQty}
              aria-label="Increase quantity"
            >+</button>
          </div>
          <span className="qty-unit">({stock} available)</span>
        </div>
      )}
    </div>
  );
}
