from pydantic import BaseModel, Field, ConfigDict

class CreditAccountResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    accountId: int = Field(validation_alias="id")                 # если сервер шлёт id
    amount: float
    termMonths: int
    balance: float = Field(validation_alias="monthlyPayment")     # если сервер шлёт monthlyPayment
    creditId: int
