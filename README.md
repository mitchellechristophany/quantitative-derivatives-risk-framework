# 📈 Quantitative Derivatives Pricing & Portfolio Risk Analytics

An institutional-grade quantitative finance pipeline designed for multi-asset derivatives pricing, volatility modeling, and portfolio-level risk aggregation.

## 📌 Features
- **Analytic & Stochastic Pricing:** Closed-form Black-Scholes and Monte Carlo valuation methods for derivative instruments.
- **Sensitivity Risk (Greeks):** Analytical calculation of Delta, Gamma, Vega, and Theta exposure vectors.
- **Value at Risk (VaR):** Implements Historical and Parametric VaR calculation across multi-asset portfolios.

## 📐 Architecture
```text
[ Market Data & Volatility Inputs ]
               │
               ▼
  ┌─────────────────────────┐
  │ Valuation & Option      │
  │ Pricing Engine          │
  └────────────┬────────────┘
               │
               ▼
  ┌─────────────────────────┐
  │ Sensitivity Risk &      │
  │ Portfolio Greeks Vector │
  └────────────┬────────────┘
               │
               ▼
  [ Real-Time Executive Risk Dashboard ]
