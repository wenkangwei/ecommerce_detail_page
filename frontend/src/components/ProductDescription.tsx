interface ProductDescriptionProps {
  description: string;
}

export default function ProductDescription({ description }: ProductDescriptionProps) {
  const sections = description.split('\n\n');

  return (
    <div className="product-description-section">
      <h2 className="section-title">Descripción</h2>

      <div className="description-body">
        {sections.map((section, idx) => {
          const lines = section.split('\n');
          const title = lines[0];
          const content = lines.slice(1).join('\n');

          return (
            <div key={idx} className="description-section">
              {content ? (
                <>
                  <h3 className="description-subtitle">{title}</h3>
                  <p className="description-text">{content}</p>
                </>
              ) : (
                <p className="description-text">{title}</p>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
}
