# Overnight-Vs-Intraday-Return-SPY-Backtest
This is an empirical analysis aimed to explore whether historical equity risk premium of the S&P 500 (SPY) is captured during overnight market closure or regular trading hours during the day. Ended up being a multi asset test of this same principle.

# Progress
1. Data Acquisition - Data ingestion engine built using python with yfinance API to pull OHLCV metrics.

2. Return Stream Computation - Implemented pandas logic to isolate daily Intraday and Overnight return streams. 

3. Data viz - Generated performace visualization using matplotlib to graph compounding equity curves.

4. Statistical Validation - Implement two-sample t-test to evaluate the p-value of overnight strat.

5. Out of sample test - Backtesting the same strat against NQ (QQQ) OHLCV metrics to see if the same results apply across indexes.

6. Dashboard - Built responsive web app using StreamLit to transition static file scripts into a dynamic interface. Integrated real time parameter configuration.

### Findings
SPY: 
T-statistic: 0.3135
P-value: 0.7539
Result: Not statistically significant, the overnight difference may be due to market noise.

QQQ: 
T-statistic: 0.3758
P-value: 0.7071
Result: Not statistically significant, the overnight difference may be due to market noise.

### Prerequisites
This project requires Python  3 and the following third-party libraries
pip install yfinance pandas matplotlib scipy streamlit

### Usage

## How to Run Backtest
Backtest Script: Open 'backtest.py' and locate execution block
```python
if __name__ == '__main__':
    TICKER = 'QQQ' #Change this to 'SPY' or 'QQQ' or ANY asset ticker
```
Execute the backtest directly from the terminal:
```bash
python backtest.py
```
## How to Run Interactive Dashboard
'app.py':  Includes interactive web interface
Run Streamlit application from terminal
```bash
streamlit run app.py
```
