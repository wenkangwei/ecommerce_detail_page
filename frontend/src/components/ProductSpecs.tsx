import { useState } from 'react';
import type { ProductSpec } from '../types';

interface ProductSpecsProps {
  specs: ProductSpec[];
}

export default function ProductSpecs({ specs }: ProductSpecsProps) {
  const [expanded, setExpanded] = useState(false);
  const visibleSpecs = expanded ? specs : specs.slice(0, 6);
  const hasMore = specs.length > 6;

  if (!specs.length) return null;

  return (
    <div className="product-section">
      <h2 className="section-title">Characteristics</h2>
      <div className="specs-grid">
        {visibleSpecs.map((spec, idx) => (
          <div key={idx} className="spec-item">
            <span className="spec-key">{spec.key}</span>
            <span className="spec-value">{spec.value}</span>
          </div>
        ))}
      </div>
      {hasMore && (
        <button className="specs-expand-btn" onClick={() => setExpanded(!expanded)}>
          {expanded ? 'See less' : 'View all characteristics'}
        </button>
      )}
    </div>
  );
}
