interface StockShippingProps {
  stock: number;
  freeShipping: boolean;
  warrantyMonths: number;
}

export default function StockShipping({ stock, freeShipping, warrantyMonths }: StockShippingProps) {
  const today = new Date();
  const estFrom = new Date(today);
  const estTo = new Date(today);
  estFrom.setDate(today.getDate() + 4);
  estTo.setDate(today.getDate() + 7);
  const fmt = (d: Date) => d.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });

  return (
    <div className="stock-shipping">
      <div className="stock-row">
        <span className="icon-check">✓</span>
        <span className="stock-label">{stock > 0 ? 'In Stock' : 'Out of Stock'}</span>
        {stock > 0 && <span className="stock-count">({stock} available)</span>}
      </div>
      {freeShipping && (
        <div className="stock-row">
          <span className="icon-truck">🚚</span>
          <div>
            <span className="shipping-free">Free Shipping</span>
            <span className="shipping-to">to all country</span>
          </div>
        </div>
      )}
      <div className="stock-row">
        <span className="icon-calendar">📅</span>
        <span className="delivery-est">Estimated delivery between {fmt(estFrom)} - {fmt(estTo)}</span>
      </div>
      <div className="stock-row">
        <span className="icon-shield">🛡️</span>
        <span className="warranty">{warrantyMonths}-month manufacturer warranty</span>
      </div>
    </div>
  );
}
