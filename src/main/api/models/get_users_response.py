from src.main.api.models.base_model import BaseModel


class GetUsersResponse(BaseModel):
    id: int
    username: str
    role: str