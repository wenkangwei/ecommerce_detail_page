import type { SellerBrief } from '../types';

interface SellerCardProps {
  seller: SellerBrief;
}

export default function SellerCard({ seller }: SellerCardProps) {
  return (
    <div className="seller-card">
      <div className="seller-header">
        {seller.is_official && (
          <span className="seller-official-badge">Official Store</span>
        )}
        <span className="seller-name">{seller.name}</span>
      </div>
      <div className="seller-sales">+5M sales</div>
      <a href={`/sellers/${seller.id}`} className="seller-link">Go to official store</a>
    </div>
  );
}
