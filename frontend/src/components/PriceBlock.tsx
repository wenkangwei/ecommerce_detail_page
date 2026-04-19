import type { InstallmentInfo } from '../types';

interface PriceBlockProps {
  price: number;
  originalPrice: number;
  currency: string;
  discountPercentage: number;
  installments: InstallmentInfo;
}

export default function PriceBlock({ price, originalPrice, currency, discountPercentage, installments }: PriceBlockProps) {
  return (
    <div className="price-block">
      {discountPercentage > 0 && (
        <div className="price-original-row">
          <span className="price-original">{currency} {originalPrice.toLocaleString('es-AR')}</span>
        </div>
      )}

      <div className="price-current-row">
        <span className="price-current">{currency} {price.toLocaleString('es-AR')}</span>
        {discountPercentage > 0 && (
          <span className="price-discount">{discountPercentage}% OFF</span>
        )}
      </div>

      {installments && (
        <div className="price-installments">
          en <span className="installment-count">{installments.count} cuotas</span> de{' '}
          <span className="installment-amount">$ {installments.amount.toLocaleString('es-AR', { minimumFractionDigits: 0 })}</span>
          {installments.interest_free && <span className="interest-free"> sin interés</span>}
        </div>
      )}

      <a href="#medios-pago" className="payment-link">Ver medios de pago y promociones</a>
    </div>
  );
}
