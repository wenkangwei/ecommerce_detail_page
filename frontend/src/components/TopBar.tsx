export default function TopBar() {
  const suggestions = ['funda samsung a54', 'samsung galaxy', 'celulares', 'samsung a54', 'celulares libres', 'samsung'];

  return (
    <div className="topbar">
      <div className="topbar-inner">
        <div className="topbar-left">
          <span className="topbar-label">También puede interesarte:</span>
          {suggestions.map((item, idx) => (
            <span key={idx} className="topbar-items">
              {idx > 0 && <span className="topbar-sep">-</span>}
              <a href={`/buscar?q=${encodeURIComponent(item)}`} className="topbar-link">{item}</a>
            </span>
          ))}
        </div>
        <div className="topbar-right">
          <a href="#" className="topbar-link">Vender uno igual</a>
        </div>
      </div>
    </div>
  );
}
