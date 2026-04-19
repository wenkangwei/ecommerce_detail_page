import { useState } from 'react';
import type { ProductImage } from '../types';

interface ImageGalleryProps {
  images: ProductImage[];
}

export default function ImageGallery({ images }: ImageGalleryProps) {
  const [selectedIdx, setSelectedIdx] = useState(0);

  if (!images.length) {
    return <div className="gallery-main"><div className="gallery-placeholder">No image</div></div>;
  }

  return (
    <div className="image-gallery">
      <div className="gallery-main">
        <img
          src={images[selectedIdx].url}
          alt={images[selectedIdx].alt_text}
          className="gallery-main-img"
        />
        <span className="gallery-counter">{selectedIdx + 1}/{images.length}</span>
      </div>
      <div className="gallery-thumbnails">
        {images.map((img, idx) => (
          <button
            key={img.id}
            className={`gallery-thumb ${idx === selectedIdx ? 'active' : ''}`}
            onClick={() => setSelectedIdx(idx)}
          >
            <img src={img.url} alt={img.alt_text} />
          </button>
        ))}
      </div>
    </div>
  );
}
