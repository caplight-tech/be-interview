import json
from pathlib import Path
from typing import List, Optional, Union
from datetime import datetime

from models.types import Company, Order, ClosedTrade

class DB:
    @staticmethod
    def parse_date(date_str: str) -> datetime:
        return datetime.strptime(date_str, "%Y-%m-%d")

    @staticmethod
    def save(item: Union[Order, ClosedTrade]) -> None:
        """Save an order or trade to the database"""
        # ... save to database
        print("Saved")

    @staticmethod
    def get_companies() -> List[Company]:
        data_path = Path("data/generated_companies.json")
        with open(data_path, "r") as f:
            companies_data = json.load(f)

        for company in companies_data:
            if company.get("lastFundingRoundDate"):
                company["lastFundingRoundDate"] = DB.parse_date(
                    company["lastFundingRoundDate"]
                )

        return [Company(**company) for company in companies_data]

    @staticmethod
    def get_company(id: str) -> Optional[Company]:
        """Get a single company by ID"""
        companies = DB.get_companies()
        return next((company for company in companies if company.id == id), None)

    @staticmethod
    def get_orders() -> List[Order]:
        data_path = Path("data/generated_orders.json")
        with open(data_path, "r") as f:
            orders_data = json.load(f)

        for order in orders_data:
            order["createdAt"] = DB.parse_date(order["createdAt"])

        return [Order(**order) for order in orders_data]

    @staticmethod
    def get_trades() -> List[ClosedTrade]:
        data_path = Path("data/generated_trades.json")
        with open(data_path, "r") as f:
            trades_data = json.load(f)

        for trade in trades_data:
            trade["transactionDate"] = DB.parse_date(trade["transactionDate"])
            trade["createdAt"] = DB.parse_date(trade["createdAt"])

        return [ClosedTrade(**trade) for trade in trades_data]

# Create a db object to mirror the TypeScript structure
db = {
    "get_companies": DB.get_companies,
    "get_company": DB.get_company,
    "get_orders": DB.get_orders,
    "get_trades": DB.get_trades,
    "save": DB.save,
}
