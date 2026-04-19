export default function PaymentMethods() {
  return (
    <div className="payment-methods" id="medios-pago">
      <h3 className="pm-title">Medios de pago</h3>

      <div className="pm-installment-banner">
        <span className="pm-installment-text">Paga en</span>
        <span className="pm-installment-badge">hasta 12 cuotas sin interés</span>
      </div>

      <div className="pm-section">
        <h4 className="pm-section-title">Tarjetas de crédito</h4>
        <p className="pm-section-desc">¡Cuotas sin interés con bancos seleccionados!</p>
        <div className="pm-icons">
          <div className="pm-card pm-visa"><span>VISA</span></div>
          <div className="pm-card pm-mastercard">
            <span className="mc-circle mc-red"></span>
            <span className="mc-circle mc-yellow"></span>
          </div>
          <div className="pm-card pm-oca"><span>OCA</span></div>
        </div>
      </div>

      <div className="pm-section">
        <h4 className="pm-section-title">Tarjetas de débito</h4>
        <div className="pm-icons">
          <div className="pm-card pm-visa-debit"><span>VISA</span><span className="debit-suffix">débito</span></div>
          <div className="pm-card pm-mc-debit">
            <span className="mc-circle mc-red"></span>
            <span className="mc-circle mc-yellow"></span>
          </div>
        </div>
      </div>

      <div className="pm-section">
        <h4 className="pm-section-title">Efectivo</h4>
        <div className="pm-icons">
          <div className="pm-card pm-abitab"><span>Abitab</span></div>
        </div>
      </div>

      <a href="#" className="pm-expand-link">Conoce otros medios de pago</a>
    </div>
  );
}
