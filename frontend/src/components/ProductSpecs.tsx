import { useState } from 'react';
import type { ProductSpec } from '../types';

interface ProductSpecsProps {
  specs: ProductSpec[];
}

export default function ProductSpecs({ specs }: ProductSpecsProps) {
  const [expanded, setExpanded] = useState(false);
  const visibleSpecs = expanded ? specs : specs.slice(0, 5);
  const hasMore = specs.length > 5;

  if (!specs.length) return null;

  return (
    <div className="product-section">
      <h2 className="section-title">Product specifications</h2>
      <div className="specs-table">
        {visibleSpecs.map((spec, idx) => (
          <div key={idx} className={`spec-row ${idx % 2 === 0 ? 'even' : 'odd'}`}>
            <span className="spec-key">{spec.key}</span>
            <span className="spec-value">{spec.value}</span>
          </div>
        ))}
      </div>
      {hasMore && (
        <button className="specs-expand-btn" onClick={() => setExpanded(!expanded)}>
          {expanded ? 'See less' : 'See all specifications'}
        </button>
      )}
    </div>
  );
}
