import type { CategoryItem } from '../types';

interface BreadcrumbProps {
  items: CategoryItem[];
  productName: string;
}

export default function Breadcrumb({ items, productName }: BreadcrumbProps) {
  return (
    <nav className="breadcrumb">
      <a href="/" className="breadcrumb-link">Home</a>
      {items.map((item) => (
        <span key={item.id}>
          <span className="breadcrumb-sep">›</span>
          <a href={`/${item.slug}`} className="breadcrumb-link">{item.name}</a>
        </span>
      ))}
      <span className="breadcrumb-sep">›</span>
      <span className="breadcrumb-current">{productName.slice(0, 50)}...</span>
    </nav>
  );
}
