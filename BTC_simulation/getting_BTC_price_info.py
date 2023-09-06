import requests
import csv
from datetime import datetime


class BtcPriceFetcher:
    def __init__(self, symbol="BTCUSDT", interval="1m", start_date=datetime(2018, 1, 1), end_date=datetime(2019, 1, 1)):
        self.api_url = "https://api.binance.com/api/v3/klines"
        self.symbol = symbol
        self.interval = interval
        self.start_timestamp = int(start_date.timestamp() * 1000)
        self.end_timestamp = int(end_date.timestamp() * 1000)
        self.limit = 100000000000000
        self.prices = []

    def fetch_btc_prices(self):
        while self.start_timestamp < self.end_timestamp:
            params = {
                "symbol": self.symbol,
                "interval": self.interval,
                "startTime": self.start_timestamp,
                "endTime": self.end_timestamp,
                "limit": self.limit
            }

            response = requests.get(self.api_url, params=params)
            data = response.json()

            for item in data:
                timestamp = item[0] / 1000
                price = float(item[4])
                self.prices.append((timestamp, price))

            # Update the start_timestamp for the next request
            self.start_timestamp = int((timestamp + 60) * 1000)  # Add 60 seconds

    def save_prices_to_csv(self, filename):
        header = ["Timestamp", "Price"]

        with open(filename, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header)

            for timestamp, price in self.prices:
                dt = datetime.fromtimestamp(timestamp)
                row = [dt, price]
                writer.writerow(row)

        print("BTC prices saved to", filename)

# Explanation:
# This code defines a class BtcPriceFetcher, which encapsulates the functionality for fetching Bitcoin (BTC) prices
# from the Binance API for a specified time range and interval, and saving them to a CSV file.
# You can create an instance of the BtcPriceFetcher class and then call its methods to fetch and save BTC prices.
# Here's an example of how to use it:


if __name__ == "__main__":
    btc_fetcher = BtcPriceFetcher()
    btc_fetcher.fetch_btc_prices()
    btc_fetcher.save_prices_to_csv("btc_prices_2018.csv")
