# Bitcoin (BTC) Market Simulator:
        
## Table of Contents:
        
        - Introduction
        
        - BtcPriceFetcher
        
        - BTCMarketSimulator
        
        - Getting Started
        
        - Usage
        
        - Contributing
        
        - License
        
## ** Introduction:
This project consists of two Python scripts that allow you to fetch historical Bitcoin (BTC) price data from Binance using the Binance API and simulate trading strategies to analyze market performance.

## ** BtcPriceFetcher:
The BtcPriceFetcher class is responsible for fetching historical BTC price data from Binance within a specified time range and interval and saving it to a CSV file. It utilizes the Binance API to retrieve data.

## ** Usage:
To use BtcPriceFetcher, follow these steps:

Create an instance of the BtcPriceFetcher class, specifying the desired parameters such as symbol (default: "BTCUSDT"), interval (default: "1m"), start_date, and end_date.

Call the fetch_btc_prices method to fetch BTC price data.

Call the save_prices_to_csv method to save the fetched data to a CSV file.

### Here's an example:

python:

if __name__ == "__main__":

    btc_fetcher = BtcPriceFetcher()
    btc_fetcher.fetch_btc_prices()
    btc_fetcher.save_prices_to_csv("btc_prices_2018.csv")

## BTCMarketSimulator
The BTCMarketSimulator class simulates a trading strategy based on historical BTC price data loaded from a CSV file. It allows you to analyze the performance of a trading strategy by specifying buy and sell conditions.

## Usage
To use BTCMarketSimulator, follow these steps:

Create an instance of the BTCMarketSimulator class, specifying the path to the CSV file containing BTC price data.

Define your trading strategy by calling the buy_btc method, specifying the buy and sell conditions, as well as parameters for balancing the wallet.

Plot the results using the plot_results method to visualize the performance of your strategy.

### Here's an example:
python:

if __name__ == "__main__":

    csv_file_path = "btc_prices_2020.csv"
    total_start = 4000
    simulator = BTCMarketSimulator(csv_file_path)
    update_when_buy = simulator.btc_wallet / 10
    update_when_sell = simulator.btc_wallet / 10    
    simulator.buy_btc(1.001, 0.999, update_when_buy, update_when_sell, total_start)
    simulator.plot_results(0, 34000000)
    

# Getting Started:
        ## Clone the project repository from GitHub.
                - git clone https://github.com/yourusername/your-repository.git
        
        ## Install the required dependencies if you haven't already.
                - pip install requests matplotlib
        ## Contributing
                - Contributions to this project are welcome. Feel free to open issues, suggest enhancements, or submit pull requests.

## License
        This project is licensed under the MIT License - see the LICENSE file for details.

