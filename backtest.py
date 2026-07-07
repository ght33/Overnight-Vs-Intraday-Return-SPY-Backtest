import yfinance as yf
import pandas as pd 

def download_data(ticker, start_date, end_date):
    """
    Pulling historical price data for SPY
    - Need daily Open, High, Low, and Close prices to be able
    to compute difference between overnight and intraday price
    movement
    """
    print(f'Fetching historical data for {ticker} from {start_date} to {end_date}...')
    data = yf.download(ticker, start=start_date, end=end_date)
    return data


def calculate_returns(data):
    """
    Calculate intraday and overnight return streams using pandas.
    Intraday: (Close - Open) / Open
    Overnight: (Current Open - Previous Close) / Previous Close
    """
    df = data.copy()

    # Intraday: Buy open, sell close of that same day
    df['Intraday_Return'] = (df['Close'] - df['Open']) / df['Open']

    # Overnight: Buy close of previous day, sell open of current day
    #.shift(1) grabs close price from row above (previous day)
    df['Overnight_Return'] = (df['Open'] - df['Close'].shift(1)) / df['Close'].shift(1)
    df = df.dropna()
    return df

if __name__ == '__main__':
    # Defining real variables
    TICKER = 'SPY'
    START = '2020-01-01'
    END = '2026-01-01'

    # Fetching raw data
    raw_data = download_data(TICKER, START, END)

    # Calculating returns
    df = calculate_returns(raw_data)

    # Print new columns to verify math worked
    print(df[['Open', 'Close', 'Intraday_Return', 'Overnight_Return']].head())
    
