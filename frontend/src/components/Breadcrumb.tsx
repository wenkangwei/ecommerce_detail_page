import type { CategoryItem } from '../types';

interface BreadcrumbProps {
  items: CategoryItem[];
  productName: string;
}

export default function Breadcrumb({ items }: BreadcrumbProps) {
  return (
    <nav className="breadcrumb">
      {items.map((item, index) => (
        <span key={item.id} className="breadcrumb-item">
          {index > 0 && <span className="breadcrumb-sep">{'>'}</span>}
          <a href={`/${item.slug}`} className="breadcrumb-link">{item.name}</a>
        </span>
      ))}
    </nav>
  );
}
