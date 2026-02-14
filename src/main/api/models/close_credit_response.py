from src.main.api.models.base_model import BaseModel



class CloseCreditResponse(BaseModel):
    creditId: int
    amountDeposited: float