# Portfolio Performance Tracker 📈

This is a Python project that tracks and visualises the performance of a simulated investment portfolio over time.

## Features

- Fetches historical price data using Yahoo Finance (`yfinance`)
- Normalises ETF prices to compare growth from a common starting point
- Calculates portfolio returns based on user-defined weights
- Compares portfolio performance against benchmark of initial investment
- Visualises cumulative returns using Matplotlib

## Tech Stack

- Python 3
- pandas
- matplotlib
- yfinance

## How to Run

1. Clone the repo
   git clone https://github.com/RaghavG12/portfolio-performance-tracker.git
   cd portfolio-performance-tracker
2. Create a virtual environment and install dependencies:
   python3 -m venv venv
   source venv/bin/activate
3. Install dependencies:
   pip install pandas matplotlib yfinance
4. Run the script (can change what products/weights/time period/initial investment):
   python3 main.py --tickers VAS.AX VGS.AX BOND.AX --weights 0.4 0.4 0.2 --start 2020-01-01 --end 2024-12-31 --amount 10000
