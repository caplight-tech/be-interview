from db import DB
from python.src.models.types import ClosedTrade, Order


def main():
    try:
        companies = DB.get_companies()
        orders = DB.get_orders()
        trades = DB.get_trades()

        print("\nCaplight Market Data Summary")
        print("===========================")
        print(f"Number of Companies: {len(companies)}")
        print(f"Number of Orders: {len(orders)}")
        print(f"Number of Trades: {len(trades)}")

        return 0
    except Exception as e:
        print(f"Error: {e}")
        return 1

def on_order_placed(order: Order):
    # TODO: Implement outlier check and save updated order to the database
    pass


def on_trade_placed(trade: ClosedTrade):
    # TODO: Implement outlier check and save updated trade to the database
    pass


if __name__ == "__main__":
    exit(main())
