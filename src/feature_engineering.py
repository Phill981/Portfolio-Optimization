import pandas as pd

class FeatureEngineering:
    def __init__(self, data):
        self.data = data

    def compute_technical_indicators(self):
        data = self.data.copy()
        data['MA50'] = data['AAPL'].rolling(window=50).mean()
        data['MA200'] = data['AAPL'].rolling(window=200).mean()
        data['Returns'] = data['AAPL'].pct_change()
        return data.dropna()

if __name__ == "__main__":
    data = pd.read_csv('../data/processed/market_data.csv', index_col=0, parse_dates=True)
    fe = FeatureEngineering(data)
    processed_data = fe.compute_technical_indicators()
    processed_data.to_csv('../data/processed/processed_data.csv')
