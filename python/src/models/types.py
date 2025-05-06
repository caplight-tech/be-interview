from datetime import datetime
from typing import Optional, Literal
from pydantic import BaseModel


class Company(BaseModel):
    id: str
    name: str
    logoUrl: str
    hqCountry: str
    marketpricePPS: Optional[float] = None
    lastFundingRoundPPS: Optional[float] = None
    lastFundingRoundDate: Optional[datetime] = None


class OrderCompany(BaseModel):
    name: str
    id: str


class Order(BaseModel):
    id: str
    direction: Literal["bid", "offer"]
    company: OrderCompany
    price: float
    targetSizeInMillions: float
    userId: int
    createdAt: datetime


class ClosedTrade(BaseModel):
    id: str
    company: OrderCompany
    price: float
    numShares: float
    userId: int
    transactionDate: datetime
    createdAt: datetime

class OrderOutliers(BaseModel):
    id: str
    direction: Literal["bid", "offer"]
    company: OrderCompany
    price: float
    targetSizeInMillions: float
    userId: int
    createdAt: datetime
    outlier: bool
    avg_price: float
    threshold: float