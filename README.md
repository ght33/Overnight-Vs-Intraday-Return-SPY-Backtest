# Overnight-Vs-Intraday-Return-SPY-Backtest
This is an empirical analysis aimed to explore whether historical equity risk premium of the S&P 500 (SPY) is captured during overnight market closure or regular trading hours during the day. 

# Progress
1. Data Acqisition - Data ingestion engine built using python with yfinance API to pull OHLCV metrics.

2. Return Stream Computation - Implemented pandas logic to isolate daily Intraday and Overnight return streams. 

3. Data viz - Generated performace visualization using matplotlib to graph compounding equity curves.

4. Statistical Validation - Implement two-sample t-test to evaluate the p-value of overnight strat.

5. Out of sample test - Backtesting the same strat against NQ (QQQ) OHLCV metrics to see if the same results apply across indexes.


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
pip install yfinance pandas matplotlib scipy 

### Usage
Execute the backtest directly from the terminal:
'''bash
python backtest.py