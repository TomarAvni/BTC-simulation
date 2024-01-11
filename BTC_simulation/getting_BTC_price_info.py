import requests
import csv
from datetime import datetime


class BtcPriceFetcher:
    """
    BtcPriceFetcher is a class designed to fetch Bitcoin (BTC) prices from the Binance API
    for a specified time range and interval, and save them to a CSV file.

    Attributes:
    - api_url (str): The Binance API URL for fetching klines data.
    - symbol (str): The trading pair symbol (default is "BTCUSDT").
    - interval (str): The time interval for klines (default is "1m" for 1 minute).
    - start_date (datetime): The start date for fetching prices (default is January 1, 2018).
    - end_date (datetime): The end date for fetching prices (default is January 1, 2019).
    - start_timestamp (int): The start timestamp in milliseconds calculated from start_date.
    - end_timestamp (int): The end timestamp in milliseconds calculated from end_date.
    - limit (int): The limit parameter for the Binance API request (default is a large value).
    - prices (list): A list to store fetched prices as tuples of (timestamp, price).

    Methods:
    - fetch_btc_prices(): Fetches BTC prices from the Binance API and populates the prices list.
    - save_prices_to_csv(filename): Saves the fetched BTC prices to a CSV file with the specified filename.
    """

    def __init__(self, symbol="BTCUSDT", interval="1m", start_date=datetime(2018, 1, 1), end_date=datetime(2019, 1, 1)):
        """
        Initializes a new instance of the BtcPriceFetcher class with default or user-specified values.

        Parameters:
        - symbol (str): The trading pair symbol (default is "BTCUSDT").
        - interval (str): The time interval for klines (default is "1m" for 1 minute).
        - start_date (datetime): The start date for fetching prices (default is January 1, 2018).
        - end_date (datetime): The end date for fetching prices (default is January 1, 2019).
        """
        self.api_url = "https://api.binance.com/api/v3/klines"
        self.symbol = symbol
        self.interval = interval
        self.start_timestamp = int(start_date.timestamp() * 1000)
        self.end_timestamp = int(end_date.timestamp() * 1000)
        self.limit = 100000000000000
        self.prices = []

    def fetch_btc_prices(self):
        """
        Fetches BTC prices from the Binance API for the specified time range and interval
        and populates the prices list with tuples of (timestamp, price).
        """
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
        """
        Saves the fetched BTC prices to a CSV file with the specified filename.

        Parameters:
        - filename (str): The name of the CSV file to save the prices to.
        """
        header = ["Timestamp", "Price"]

        with open(filename, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header)

            for timestamp, price in self.prices:
                dt = datetime.fromtimestamp(timestamp)
                row = [dt, price]
                writer.writerow(row)

        print("BTC prices saved to", filename)


# Example usage:
if __name__ == "__main__":
    btc_fetcher = BtcPriceFetcher()
    btc_fetcher.fetch_btc_prices()
    btc_fetcher.save_prices_to_csv("btc_prices_2018.csv")
