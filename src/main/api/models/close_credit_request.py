from src.main.api.models.base_model import BaseModel



class CloseCreditRequest(BaseModel):
    creditId: int
    accountId: int
    amount: float
