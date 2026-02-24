from typing import List
from datetime import datetime
from src.main.api.models.base_model import BaseModel


class CreditHistoryItemResponse(BaseModel):
    creditId: int
    accountId: int
    amount: float
    termMonths: int
    balance: float
    createdAt: datetime


class GetHistoryResponse(BaseModel):
    userId: int
    credits: List[CreditHistoryItemResponse]