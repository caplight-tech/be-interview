import json
from pathlib import Path
from typing import List
from datetime import datetime

from models.types import Company, Order, ClosedTrade


def parse_date(date_str: str) -> datetime:
    return datetime.strptime(date_str, "%Y-%m-%d")


def get_companies() -> List[Company]:
    data_path = Path("data/generated_companies.json")
    with open(data_path, "r") as f:
        companies_data = json.load(f)

    # Parse dates before creating Company objects
    for company in companies_data:
        if company.get("lastFundingRoundDate"):
            company["lastFundingRoundDate"] = parse_date(
                company["lastFundingRoundDate"]
            )

    return [Company(**company) for company in companies_data]


def get_orders() -> List[Order]:
    data_path = Path("data/generated_orders.json")
    with open(data_path, "r") as f:
        orders_data = json.load(f)

    # Parse dates before creating Order objects
    for order in orders_data:
        order["createdAt"] = parse_date(order["createdAt"])

    return [Order(**order) for order in orders_data]


def get_closed_trades() -> List[ClosedTrade]:
    data_path = Path("data/generated_trades.json")
    with open(data_path, "r") as f:
        trades_data = json.load(f)

    # Parse dates before creating ClosedTrade objects
    for trade in trades_data:
        trade["transactionDate"] = parse_date(trade["transactionDate"])
        trade["createdAt"] = parse_date(trade["createdAt"])

    return [ClosedTrade(**trade) for trade in trades_data]
