import yfinance as yf
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt

def equity_correlation_detector(ticker1: str, ticker2: str, period:str):
    ticker1 = ticker1.upper()
    ticker2 = ticker2.upper()
    period = period.lower()

    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    # Valid Time Periods: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max

    data_t1 = yf.download(ticker1, period=period)
    data_t2 = yf.download(ticker2, period=period)

    data_t1['Percent Change'] = data_t1['Adj Close'].pct_change() * 100
    data_t1 = data_t1.dropna(subset=['Percent Change'])

    data_t2['Percent Change'] = data_t2['Adj Close'].pct_change() * 100
    data_t2 = data_t2.dropna(subset=['Percent Change'])

    correlation = np.corrcoef(data_t1["Percent Change"], data_t2["Percent Change"])
    return correlation