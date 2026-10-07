import numpy as np
from scipy.stats import norm

class DerivativesPricingEngine:
    @staticmethod
    def black_scholes_call(S: float, K: float, T: float, r: float, sigma: float) -> dict:
        """
        Calculates Black-Scholes Call Price and Primary Sensitivity Greeks.
        S: Spot Price, K: Strike Price, T: Time to Expiry (Years), r: Risk-free rate, sigma: Volatility
        """
        d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
        d2 = d1 - sigma * np.sqrt(T)
        
        call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
        delta = norm.cdf(d1)
        gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))
        vega = S * norm.pdf(d1) * np.sqrt(T) / 100.0  # Normalized for 1% vol shift
        
        return {
            "option_price": round(float(call_price), 4),
            "delta": round(float(delta), 4),
            "gamma": round(float(gamma), 4),
            "vega": round(float(vega), 4)
        }

if __name__ == "__main__":
    # Example Trade Parameters
    spot, strike, expiry, rate, volatility = 100.0, 105.0, 0.5, 0.05, 0.20
    results = DerivativesPricingEngine.black_scholes_call(spot, strike, expiry, rate, volatility)
    
    print("--- Quantitative Derivatives Risk Assessment ---")
    for greek, val in results.items():
        print(f"{greek.upper()}: {val}")
