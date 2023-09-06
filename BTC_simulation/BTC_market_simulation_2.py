import csv
import matplotlib.pyplot as plt


class BTCMarketSimulator:
    def __init__(self, csv_file_path):
        self.market_percentage = []
        self.wallet_percentage = []
        self.total_balance = 0
        self.all_action = 0
        self.filtered_btc_prices = []
        self.filtered_btc_time = []
        self.btc_wallet = 0
        self.cash_wallet = 0
        self.load_data(csv_file_path)

    def load_data(self, csv_file_path):
        with open(csv_file_path, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            btc_prices = []
            btc_time = []
            for row in reader:
                btc_prices.append(row[1])
                btc_time.append(row[0])

            self.filtered_btc_prices = [price for price in btc_prices if 'NaN' not in price]
            self.filtered_btc_prices = [float(item) for item in self.filtered_btc_prices[1:]]
            self.filtered_btc_time = [float(x) for x in btc_time if x.isnumeric()]

    def buy_btc(self, sell_price, buy_price, balancing_after_sell, balancing_after_buy, total_start_balance):
        first_price = self.filtered_btc_prices[1]
        self.cash_wallet = total_start_balance / 2
        self.btc_wallet = (total_start_balance / 2) / first_price
        btc_buy_price = first_price * buy_price
        btc_sell_price = first_price * sell_price
        count_sell = 0
        count_buy = 0
        self.total_balance = (self.btc_wallet * first_price) + self.cash_wallet

        for btc_price in self.filtered_btc_prices:
            if btc_price >= btc_sell_price:  # sell
                self.cash_wallet += ((balancing_after_sell * btc_price) * 0.9995)
                self.btc_wallet -= balancing_after_sell
                btc_sell_price = btc_price * sell_price
                btc_buy_price = btc_price * buy_price
                count_sell += 1
                self.total_balance = (self.btc_wallet * btc_price) + self.cash_wallet
                value_to_market = (btc_price / first_price * 100)
                self.market_percentage.append(value_to_market)
                value_to_wallet = (self.total_balance / total_start_balance * 100)
                self.wallet_percentage.append(value_to_wallet)

            if btc_price <= btc_buy_price:  # buy
                self.btc_wallet += ((balancing_after_buy / btc_price) * 0.9995)
                self.cash_wallet -= balancing_after_buy
                btc_buy_price = btc_price * buy_price
                btc_sell_price = btc_price * sell_price
                count_buy += 1
                self.total_balance = (self.btc_wallet * btc_price) + self.cash_wallet
                value_to_market = (btc_price / first_price * 100)
                self.market_percentage.append(value_to_market)
                value_to_wallet = (self.total_balance / total_start_balance * 100)
                self.wallet_percentage.append(value_to_wallet)

        self.all_action = count_sell + count_buy

    def plot_results(self, start_value_to_check, finish_value_to_check):
        time_for_x_axis = list(range(self.all_action))
        x = time_for_x_axis[start_value_to_check:finish_value_to_check]
        y1 = self.market_percentage[start_value_to_check:finish_value_to_check]
        y2 = self.wallet_percentage[start_value_to_check:finish_value_to_check]
        plt.plot(x, y1, label='market')
        plt.plot(x, y2, label='wallet')
        plt.xlabel('Time')
        plt.ylabel('Price')
        plt.title('Price over Time')
        plt.legend()
        plt.show()


if __name__ == "__main__":
    csv_file_path = "/btc_prices_2020.csv"
    total_start = 4000
    simulator = BTCMarketSimulator(csv_file_path)
    update_when_buy = simulator.btc_wallet / 10
    update_when_sell = simulator.btc_wallet / 10
    simulator.buy_btc(1.001, 0.999, update_when_buy, update_when_sell, total_start)
    print('Finish simulation, starting graph...')
    simulator.plot_results(0, 34000000)
    print('Finish plot')

