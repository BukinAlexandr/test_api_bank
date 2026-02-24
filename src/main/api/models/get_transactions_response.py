from src.main.api.models.base_model import BaseModel
from typing import List, Optional


class TransactionResponse(BaseModel):
    transactionId: int
    type: str
    amount: float
    fromAccountId: Optional[int] = None
    toAccountId: Optional[int] = None
    createdAt: str


class AccountResponse(BaseModel):
    id: int
    number: str
    balance: float
    transactions: List[TransactionResponse]