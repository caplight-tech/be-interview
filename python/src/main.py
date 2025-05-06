from db import DB
from python.src.models.types import ClosedTrade, Order
import numpy as np

def main():
    try:
        companies = DB.get_companies()
        orders = DB.get_orders()
        trades = DB.get_trades()
        #outlier_table = blah

        print("\nCaplight Market Data Summary")
        print("===========================")
        print(f"Number of Companies: {len(companies)}")
        print(f"Number of Orders: {len(orders)}")
        print(f"Number of Trades: {len(trades)}")

        return 0
    except Exception as e:
        print(f"Error: {e}")
        return 1

def calc_avg_and_std(dict: order_data, str: company):
    prices = []
    for item in order_data:
        if item['company']['name'] == company:
            prices.append(item['price'])
    average = np.mean(prices)
    stdev = np.std(prices)
    output = {'avg': average, 'std': stdev}
    return output

def get_size_data(order_data, company):
    # collect all the order size data for given company

def on_order_placed(order: Order, dict: orders, float: thresh_multip):
    # TODO: Implement outlier check and save updated order to the database
    order_company = Order['company']['name']
    metrics = calc_avg_and_std(orders, order_company)
    order_price = Order['price']
    threshold = thresh_multip * metrics['std']
    avg_price = metrics['avg']

    low_thresh = avg_price - threshold
    high_thresh = avg_price + threshold

    if order_price < low_thresh or order_price > high_thresh:
        Order['outlier'] = True
        Order['avg_price'] = avg_price
        Order['threshold'] = threshold
        outlier_table.save(Order)

    # call the get_size_data function
    # determine upper/lower threshold (could be a param passed to this fn e.g. lower: 0.1, upper 0.9)
    # sort the list of order sizes
    # given the sorted list, and the upper/lower percentiles calc threshold values
    # compare current order size to threshold
    # if outside threshold values, insert in table flagged 'outlier'

    
     
def determine_price_outlier(order: hist_data, dict: current_observation):


def on_trade_placed(dict: trades, trade: ClosedTrade):
    # TODO: Implement outlier check and save updated trade to the database
    order_price = ClosedTrade['price']
    conmpany = ClosedTrade['company']
    current_data ={'order_price': order_price, 'company': company}
    determine_price_outlier(trades, current_data)



if __name__ == "__main__":
    exit(main())
