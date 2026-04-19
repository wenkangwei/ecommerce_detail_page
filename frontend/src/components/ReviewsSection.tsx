import type { ReviewData, ReviewSummary } from '../types';

interface ReviewsSectionProps {
  reviews: ReviewData[];
  summary: ReviewSummary;
  pagination: { page: number; page_size: number; total: number; total_pages: number };
}

function StarBar({ label, count, max }: { label: string; count: number; max: number }) {
  const pct = max > 0 ? (count / max) * 100 : 0;
  return (
    <div className="star-bar-row">
      <span className="star-bar-label">{label}</span>
      <div className="star-bar-track">
        <div className="star-bar-fill" style={{ width: `${pct}%` }} />
      </div>
      <span className="star-bar-count">{count}</span>
    </div>
  );
}

function StarRating({ rating }: { rating: number }) {
  return (
    <span className="review-stars">
      {[1, 2, 3, 4, 5].map((s) => (
        <span key={s} className={s <= rating ? 'star-filled' : 'star-empty'}>★</span>
      ))}
    </span>
  );
}

function ReviewCard({ review }: { review: ReviewData }) {
  const initials = review.user_name.slice(0, 2).toUpperCase();
  return (
    <div className="review-card">
      <div className="review-header">
        <div className="review-avatar">{initials}</div>
        <div className="review-meta">
          <span className="review-user">{review.user_name}</span>
          <span className="review-date">{review.date}</span>
        </div>
        <StarRating rating={review.rating} />
      </div>
      <h4 className="review-title">{review.title}</h4>
      <p className="review-content">{review.content}</p>
    </div>
  );
}

export default function ReviewsSection({ reviews, summary, pagination }: ReviewsSectionProps) {
  const dist = summary.distribution;
  const maxCount = Math.max(dist.star_5, dist.star_4, dist.star_3, dist.star_2, dist.star_1, 1);

  return (
    <div className="product-section reviews-section">
      <h2 className="section-title">Reviews</h2>
      <div className="reviews-layout">
        <div className="reviews-summary">
          <div className="reviews-avg">
            <span className="reviews-avg-number">{summary.average}</span>
            <span className="reviews-avg-stars">{'★'.repeat(Math.round(summary.average))}{'☆'.repeat(5 - Math.round(summary.average))}</span>
            <span className="reviews-avg-total">{pagination.total} reviews</span>
          </div>
          <div className="reviews-distribution">
            <StarBar label="5★" count={dist.star_5} max={maxCount} />
            <StarBar label="4★" count={dist.star_4} max={maxCount} />
            <StarBar label="3★" count={dist.star_3} max={maxCount} />
            <StarBar label="2★" count={dist.star_2} max={maxCount} />
            <StarBar label="1★" count={dist.star_1} max={maxCount} />
          </div>
        </div>
        <div className="reviews-list">
          {reviews.map((review) => (
            <ReviewCard key={review.id} review={review} />
          ))}
        </div>
      </div>
    </div>
  );
}
