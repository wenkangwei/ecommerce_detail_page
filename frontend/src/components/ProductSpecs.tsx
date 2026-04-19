import { useState } from 'react';
import type { ProductSpec } from '../types';

interface ProductSpecsProps {
  specs: ProductSpec[];
}

function getSpecIcon(key: string): string {
  const k = key.toLowerCase();
  if (k.includes('pantalla') || k.includes('screen') || k.includes('tamaño')) return '🖥';
  if (k.includes('memoria interna') || k.includes('storage') || k.includes('almacenamiento')) return '💾';
  if (k.includes('cámara') || k.includes('camera')) return '📷';
  if (k.includes('nfc')) return '📱';
  if (k.includes('ram') || k.includes('memoria')) return '⚙️';
  if (k.includes('desbloqueo') || k.includes('huella')) return '🔐';
  if (k.includes('procesador') || k.includes('chip')) return '🧠';
  if (k.includes('batería') || k.includes('battery')) return '🔋';
  if (k.includes('peso')) return '⚖️';
  if (k.includes('conectividad')) return '📡';
  return '📱';
}

export default function ProductSpecs({ specs }: ProductSpecsProps) {
  const [expanded, setExpanded] = useState(false);
  const visibleSpecs = expanded ? specs : specs.slice(0, 6);

  if (!specs.length) return null;

  return (
    <div className="product-specs-section" id="caracteristicas">
      <h2 className="section-title">Características del producto</h2>

      <div className="specs-grid">
        {visibleSpecs.map((spec, idx) => (
          <div key={idx} className="spec-item">
            <span className="spec-icon">{getSpecIcon(spec.key)}</span>
            <div className="spec-content">
              <span className="spec-key">{spec.key}: </span>
              <span className="spec-value">{spec.value}</span>
            </div>
          </div>
        ))}
      </div>

      {specs.length > 6 && (
        <button className="specs-expand-btn" onClick={() => setExpanded(!expanded)}>
          {expanded ? 'Ver menos características' : 'Ver todas las características'}
        </button>
      )}
    </div>
  );
}
