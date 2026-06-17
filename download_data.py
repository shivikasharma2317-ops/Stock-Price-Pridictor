import yfinance as yf
import os

# Create data folder if it doesn't exist
if not os.path.exists("data"):
    os.makedirs("data")

# Download Apple stock data
data = yf.download(
    "AAPL",
    start="2020-01-01",
    end="2024-01-01"
)

# Save to CSV
data.to_csv("data/stock_data.csv")

print("Stock data downloaded successfully!")
