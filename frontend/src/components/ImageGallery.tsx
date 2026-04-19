import { useState, useCallback } from 'react';
import type { ProductImage } from '../types';

interface ImageGalleryProps {
  images: ProductImage[];
}

export default function ImageGallery({ images }: ImageGalleryProps) {
  const [selectedIdx, setSelectedIdx] = useState(0);
  const [fade, setFade] = useState(false);

  const switchImage = useCallback((idx: number) => {
    if (idx === selectedIdx) return;
    setFade(true);
    setTimeout(() => {
      setSelectedIdx(idx);
      setFade(false);
    }, 150);
  }, [selectedIdx]);

  if (!images.length) {
    return <div className="gallery-main"><div className="gallery-placeholder">No image</div></div>;
  }

  return (
    <div className="image-gallery">
      {/* Vertical thumbnail strip */}
      <div className="gallery-thumbs-vertical">
        {images.map((img, idx) => (
          <button
            key={img.id}
            className={`gallery-thumb ${idx === selectedIdx ? 'active' : ''}`}
            onMouseEnter={() => switchImage(idx)}
            onClick={() => switchImage(idx)}
            aria-label={`View image ${idx + 1}`}
          >
            <img src={img.url} alt={img.alt_text} />
          </button>
        ))}
      </div>

      {/* Main image */}
      <div className="gallery-main">
        <img
          src={images[selectedIdx].url}
          alt={images[selectedIdx].alt_text}
          className={`gallery-main-img ${fade ? 'gallery-fade-out' : ''}`}
        />
        <span className="gallery-counter">{selectedIdx + 1}/{images.length}</span>
      </div>
    </div>
  );
}
