from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    # id: str | None  # indica que es un opcional
    id: Optional[str]  # indica que es un opcional
    username: str
    email: str
