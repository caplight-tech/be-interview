from db import get_companies, get_orders, get_closed_trades


def main():
    try:
        companies = get_companies()
        orders = get_orders()
        trades = get_closed_trades()

        print("\nCaplight Market Data Summary")
        print("===========================")
        print(f"Number of Companies: {len(companies)}")
        print(f"Number of Orders: {len(orders)}")
        print(f"Number of Trades: {len(trades)}")

        return 0
    except Exception as e:
        print(f"Error: {e}")
        return 1


if __name__ == "__main__":
    exit(main())
