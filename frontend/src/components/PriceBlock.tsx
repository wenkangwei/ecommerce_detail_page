import type { InstallmentInfo } from '../types';

interface PriceBlockProps {
  price: number;
  originalPrice: number;
  currency: string;
  discountPercentage: number;
  installments: InstallmentInfo;
}

export default function PriceBlock({
  price,
  originalPrice,
  currency,
  discountPercentage,
  installments,
}: PriceBlockProps) {
  return (
    <div className="price-block">
      <div className="price-row">
        {discountPercentage > 0 && (
          <span className="price-original">
            {currency} {originalPrice.toLocaleString('en-US', { minimumFractionDigits: 2 })}
          </span>
        )}
        {discountPercentage > 0 && (
          <span className="price-discount">{discountPercentage}% OFF</span>
        )}
      </div>
      <div className="price-current">
        {currency} {price.toLocaleString('en-US', { minimumFractionDigits: 2 })}
      </div>
      {installments && (
        <div className="price-installments">
          in <strong>{installments.count} installments</strong> of {currency}{' '}
          {installments.amount.toLocaleString('en-US', { minimumFractionDigits: 2 })}{' '}
          {installments.interest_free && <span className="interest-free">without interest</span>}
        </div>
      )}
    </div>
  );
}
