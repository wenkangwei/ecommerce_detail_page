import type { SellerBrief } from '../types';

interface SellerCardProps {
  seller: SellerBrief;
}

export default function SellerCard({ seller }: SellerCardProps) {
  return (
    <div className="seller-card">
      {seller.is_official && (
        <div className="seller-official-badge">Official Store</div>
      )}
      <div className="seller-info">
        <span className="seller-name">{seller.name}</span>
        <span className="seller-reputation">{seller.reputation}</span>
        <span className="seller-location">📍 {seller.location}</span>
      </div>
      <a href={`/sellers/${seller.id}`} className="seller-link">See seller's store</a>
    </div>
  );
}
