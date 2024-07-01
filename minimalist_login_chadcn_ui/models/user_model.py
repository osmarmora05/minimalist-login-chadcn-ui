import reflex as rx
from typing import Optional
from sqlmodel import Field

class Users(rx.Model, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    github_username: str
    password: str