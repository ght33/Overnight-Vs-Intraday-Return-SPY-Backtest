import yfinance as yf
import pandas as pd 
import matplotlib.pyplot as plt


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

def plot_results(df):
    """
    Computing cumulative compunding returns and plotting equity curves.
    """
    # 1. Calculate compounding returns starting from $1
    df['Intraday_Equity'] = (1 + df['Intraday_Return']).cumprod()
    df['Overnight_Equity'] = (1 + df['Overnight_Return']).cumprod()

    # 2. Initializing plot canvas
    plt.figure(figsize=(12, 6))

    # 3. Plotting both strategies lines
    plt.plot(df.index, df['Intraday_Equity'], label='Intraday Strategy (Buy Open, Sell Close)', color = 'blue', lw=1.5)
    plt.plot(df.index, df['Overnight_Equity'], label='Overnight Strategy (Buy Close, Sell Open)', color = 'orange', lw=1.5)

    #4 Styling
    plt.title('SPY Performance: Intraday Vs Overnight Compunding from 2020-2026', fontsize=14, fontweight='bold')
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Growth of $1 Investment', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend(fontsize=11)

    #5 Displaying chart
    plt.tight_layout()
    print('Generating plot... (Close the chart window to return to terminal)')
    plt.savefig('spy_performance.png')



if __name__ == '__main__':
    # Defining real variables
    TICKER = 'SPY'
    START = '2020-01-01'
    END = '2026-01-01'

    # Fetching raw data
    raw_data = download_data(TICKER, START, END)

    # Calculating returns
    df = calculate_returns(raw_data)

    # Calling visualization function
    plot_results(df)
    
