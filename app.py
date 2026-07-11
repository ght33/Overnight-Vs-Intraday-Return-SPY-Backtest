import streamlit as st
import datetime

from backtest import download_data. calculate_returns

#Web page layout
st.set_page_config(page_title='Overnight vs Intraday Backtest', layout='wide')
st.title('Overnight Vs Intraday Return Backtest')

#Sidebar
st.sidebar.header('Strategy Settings')
ticker = st.sidebar.selectbox('Select Asset Ticker', ['SPY', 'QQQ'])

#Date Windows
start_date = st.sidebar.date_input("Start Date", datetime.date(2020, 1, 1))
end_date = st.sidebar.date_input('End Date', datetime.date(2026, 6, 1))

#Pass sidebar options into backend engine
if ticker:
    st.write(f"### Analyzing {ticker} from {start_date} to {end_date}")

    # Fetch data
    data = download_data(ticker, start_date.strftime('%Y-%m-%d'),end_date.strftime('%Y-%m-%d'))

    # Calculate returns
    data = calculate_returns(data)

    st.success("Data loaded completely")
