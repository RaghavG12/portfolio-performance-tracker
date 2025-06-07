import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Define portfolio settings
# tickers string array with different aussie etfs listed on asx
tickers = ["VAS.AX", "VGS.AX", "BOND.AX"]  
 # sample portfolio allocation
weights = [0.4, 0.4, 0.2]       
# setting variable to show we start with $10,000          
initial_investment = 10000                

# Define the date range for historical data
start_date = "2020-01-01"
end_date = "2024-12-31"

# Step 2: Download daily adjusted close prices
# yf.download tells program to fetch historical stock/etf price data from yahoo finance
# yf.download returns a DataFrame which is its own type - where each row is a date
price_data = yf.download(tickers, start=start_date, end=end_date, auto_adjust=True)
# we include auto_adjust=True because without it we receive data that is not adjusted dividends or stock splits
# for accuracy, auto_adjust=True is a requirement

# testing: show first few rows to check data frame is correct and working
#print(price_data.head())

# Monitoring only overall portfolio performance so we only care about closing prices
# closing_prices is name of a type DataFrame - where the only column is the closing column 
closing_prices = price_data["Close"]


# normalised is also a dataframe type with 3 columns - standardised prices for each etf in portfolio
# iloc[0] means integer location 0th index. So this gives normalised = 1 for the first row
normalised = closing_prices / closing_prices.iloc[0]
#print(normalised.head())

# same thing as normalised tables - except weighted according to scale of contribution to initial $10k
weighted = normalised * weights

#print(weighted.head())

# Sum across columns to get total portfolio value over time
# note that if we had axis = 1, we would be summing down the columns, not rows
portfolio_growth = weighted.sum(axis=1)

#print(portfolio_growth.head())

# multiplying by initial investment
portfolio_value = portfolio_growth * initial_investment

# Show the first few rows of the portfolio's value because otherwise too many rows
print("Portfolio value over time:")
# print(portfolio_value.head()) 

# since too many rows to just print the entire portfolio_value table - need to graph growth

# Step 3: Plot the portfolio value over time
plt.figure(figsize=(10, 6))  # Set the size of the plot
portfolio_value.plot(title="Portfolio Value Over Time", linewidth=2)

# Add labels and grid
plt.xlabel("Date")
plt.ylabel("Portfolio Value ($)")
plt.grid(True)

# Show the plot
plt.tight_layout()
plt.show()
