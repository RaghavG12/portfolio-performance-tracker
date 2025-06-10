import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import argparse

def get_args():
    # creating an Argument Parser object called 'parser' from argparse library
    parser = argparse.ArgumentParser()

    # nargs just means to allow one or more values 
    # "--tickers" "--weights" etc are the required arguments
    parser.add_argument("--tickers", nargs="+", required=True)
    parser.add_argument("--weights", nargs="+", type=float, required=True)
    parser.add_argument("--start", required=True)
    parser.add_argument("--end", required=True)
    parser.add_argument("--amount", type=float, required=True)

    return parser.parse_args()

args = get_args()

tickers = args.tickers
weights = args.weights
initial_investment = args.amount                
start_date = args.start
end_date = args.end


# error checking
if len(tickers) != len(weights):
    raise ValueError("The number of tickers must match the number of weights.")
if not abs(sum(args.weights) - 1.0) == 0:
    # f-string to evaluate variables inside {}
    # :.4f to tell python to evaluate to 4 decimal place float 
    raise ValueError(f"Sum of weights must be 1.0. You provided: {sum(args.weights):.4f}")


# yf.download tells program to fetch historical stock/etf price data from yahoo finance
# yf.download returns a DataFrame which is its own type - where each row is a date
price_data = yf.download(tickers, start=start_date, end=end_date, auto_adjust=True)
# we include auto_adjust=True because without it we receive data that is not adjusted dividends or stock splits
# for accuracy, auto_adjust=True is a requirement

# testing: show first few rows to check data frame is correct and working
#print(price_data.head())

# monitoring only overall portfolio performance so we only care about closing prices
# closing_prices is name of a type DataFrame - where the only column is the closing column 
closing_prices = price_data["Close"]


# normalised is also a dataframe type with 3 columns - standardised prices for each etf in portfolio
# iloc[0] means integer location 0th index. So this gives normalised = 1 for the first row
normalised = closing_prices / closing_prices.iloc[0]

# same thing as normalised tables - except weighted according to scale of contribution to initial $10k
weighted = normalised * weights

# Sum across columns to get total portfolio value over time
# note that if we had axis = 1, we would be summing down the columns, not rows
portfolio_growth = weighted.sum(axis=1)

# multiplying by initial investment
portfolio_value = portfolio_growth * initial_investment








# since too many rows to just print the entire portfolio_value table - need to graph growth

 # set size of the plot - width 10 inches, hieght 6 inches
plt.figure(figsize=(10, 6)) 
portfolio_value.plot(title="Portfolio Value Over Time")

plt.xlabel("Date")
plt.ylabel("Portfolio Value")
# this adds gridlines so chart is easier to see
plt.grid(True)

plt.show()
