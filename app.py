import streamlit as st
import datetime
from scipy import stats

from backtest import download_data, calculate_returns

#Web page layout
st.set_page_config(page_title='Overnight vs Intraday Backtest', layout='wide')
st.title('Overnight Vs Intraday Return Backtest')

#Sidebar
st.sidebar.header('Strategy Settings')
ticker = st.sidebar.selectbox('Select Asset Ticker', ['SPY', 'QQQ', 'IWM', 'DIA', 'AAPL', 'MSFT', 'NVDA'])

#Date Windows
start_date = st.sidebar.date_input("Start Date", datetime.date(2020, 1, 1))
end_date = st.sidebar.date_input('End Date', datetime.date(2026, 6, 1))

#PDynamic execution
if ticker:
    try:
        #Fetch and calculating data with sidebars
        raw_data = download_data(ticker, start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'))
        df = calculate_returns(raw_data)

        st.write(f'### Analyzing {ticker} from {start_date} to {end_date}')
        st.success('Data loaded completely')

        #Run stat validation on date range
        overnight_clean = df['Overnight_Return'].dropna()
        intraday_clean = df['Intraday_Return'].dropna()
        t_stat, p_val = stats.ttest_rel(overnight_clean, intraday_clean)

        #Display real stat metrics dynamically
        st.write('### Statistical Metrics')
        col1, col2 = st.columns(2)
        with col1:
            st.metric(label='T-Statistic', value=f'{t_stat: .4f}')
        with col2:
            st.metric(label='P-Value', value=f'{p_val: .4f}')
        
        #Plotting dynamic preformance curve
        st.write('### Strategy Performance Curve')

        # Calculating cumulative returns visualized
        df['Intraday_Cum'] = (1 + df['Intraday_Return'].fillna(0)).cumprod()
        df['Overnight_Cum'] = (1 + df['Overnight_Return'].fillna(0)).cumprod()

        #Clean df for chart
        chart_data = df[['Intraday_Cum', 'Overnight_Cum']]
        chart_data.columns = ['Intraday Strategy (Buy Open, Sell Close)', 'Overnight Strategy (Buy Close, Sell Open)']

        #Render chart
        st.line_chart(chart_data)
    except Exception as e:
        st.error(f"Error Processing Data for selected range: {e}")