import { useState, useCallback } from 'react';
import type { ProductImage } from '../types';

interface ImageGalleryProps {
  images: ProductImage[];
}

export default function ImageGallery({ images }: ImageGalleryProps) {
  const [selectedIdx, setSelectedIdx] = useState(0);
  const [liked, setLiked] = useState(false);
  const [fade, setFade] = useState(false);

  const switchImage = useCallback((idx: number) => {
    if (idx === selectedIdx) return;
    setFade(true);
    setTimeout(() => {
      setSelectedIdx(idx);
      setFade(false);
    }, 120);
  }, [selectedIdx]);

  if (!images.length) {
    return <div className="gallery-main"><span className="gallery-placeholder">Sin imagen</span></div>;
  }

  return (
    <div className="image-gallery">
      <div className="gallery-thumbs-vertical">
        {images.map((img, idx) => (
          <button
            key={img.id}
            className={`gallery-thumb ${idx === selectedIdx ? 'active' : ''}`}
            onMouseEnter={() => switchImage(idx)}
            onClick={() => switchImage(idx)}
            aria-label={`Ver imagen ${idx + 1}`}
          >
            <img src={img.url} alt={img.alt_text} />
          </button>
        ))}
      </div>

      <div className="gallery-main">
        <img
          src={images[selectedIdx].url}
          alt={images[selectedIdx].alt_text}
          className={`gallery-main-img ${fade ? 'gallery-fade-out' : ''}`}
        />
        <button
          className={`gallery-fav ${liked ? 'liked' : ''}`}
          onClick={() => setLiked(!liked)}
          aria-label="Agregar a favoritos"
        >
          <svg viewBox="0 0 24 24" width="20" height="20" fill={liked ? '#3483fa' : 'none'} stroke="#3483fa" strokeWidth="2">
            <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/>
          </svg>
        </button>
      </div>
    </div>
  );
}
