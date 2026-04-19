import { useState } from 'react';
import type { PaymentMethod } from '../types';

interface PaymentMethodsProps {
  methods: PaymentMethod[];
}

export default function PaymentMethods({ methods }: PaymentMethodsProps) {
  const [expanded, setExpanded] = useState(false);

  const creditCards = methods.filter((m) => m.type === 'credit_card');
  const debitCards = methods.filter((m) => m.type === 'debit_card');
  const wallets = methods.filter((m) => m.type === 'digital_wallet');
  const maxInstallments = Math.max(...methods.map((m) => m.max_installments), 1);

  return (
    <div className="payment-methods">
      <h3 className="pm-title">Payment methods</h3>
      <div className="pm-installment-banner">
        up to <strong>{maxInstallments}</strong> installments <span className="interest-free">without interest</span>
      </div>

      <div className="pm-icons">
        {[...creditCards, ...debitCards, ...wallets].slice(0, expanded ? undefined : 4).map((m) => (
          <div key={m.id} className="pm-item">
            <div className={`pm-icon pm-type-${m.type}`}>
              {m.name.slice(0, 4).toUpperCase()}
            </div>
          </div>
        ))}
      </div>

      {methods.length > 4 && (
        <button className="pm-expand-btn" onClick={() => setExpanded(!expanded)}>
          {expanded ? 'See less' : 'See all payment methods'}
        </button>
      )}
    </div>
  );
}
