import yfinance as yf
import pandas as pd

class DataAcquisition:
    def __init__(self, tickers, start_date, end_date):
        self.tickers = tickers
        self.start_date = start_date
        self.end_date = end_date
    
    def fetch_data(self):
        data = yf.download(self.tickers, start=self.start_date, end=self.end_date)
        return data['Adj Close']

if __name__ == "__main__":
    tickers = ['AAPL', 'MSFT', 'GOOGL']
    data_acq = DataAcquisition(tickers, '2020-01-01', '2023-01-01')
    data = data_acq.fetch_data()
    data.to_csv('../data/processed/market_data.csv')
