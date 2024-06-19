import pandas as pd
import numpy as np
import cvxpy as cp

class PortfolioOptimizer:
    def __init__(self, returns):
        self.returns = returns
    
    def optimize_portfolio(self):
        n = len(self.returns.columns)
        w = cp.Variable(n)
        ret = self.returns.mean().values @ w
        risk = cp.quad_form(w, self.returns.cov().values)
        gamma = 1  # Risk aversion parameter
        prob = cp.Problem(cp.Maximize(ret - gamma * risk), [cp.sum(w) == 1, w >= 0])
        prob.solve()
        return w.value

if __name__ == "__main__":
    data = pd.read_csv('../data/processed/processed_data.csv', index_col=0, parse_dates=True)
    returns = data.pct_change().dropna()
    optimizer = PortfolioOptimizer(returns)
    weights = optimizer.optimize_portfolio()
    print("Optimized Weights:", weights)
