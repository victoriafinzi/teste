from typing import Optional, List
from pydantic import BaseModel, EmailStr, Field, HttpUrl

class Clients(BaseModel):
    name: str = Field (
        title = "Client's name", 
        description = " Client's fullname with a maximum of 70 characters",
        example = "Gertrudes Silva",
        max_length = 70
    )
    phone: str = Field(
        title = "Client's telephone",
        description = "Client's phone with a maximum of 15 characteres",
        example = "(34) 99999-9999",
        max_lenght = 15
    )
    email: EmailStr = Field(
        title = "User's email",
        description = "User's e-mail adress",
        example = "gertrudessilva@email.com"
    )
    passwordbet365: str = Field(
        title = "User's password",
        description = " User's password with a minimum of 5 character and a maximum of 20 characteres",
        example = "F1@gbD412$DD1"
    )
    state: str = Field (
        title = "UF of the client",
        example = "MG",
        description = "UF in uppercase with 2 characters.",
        regex = "^[A-Z]{2}$"
    )
    userbet365: str = Field(
        title = "Client's User from Bet365 account",
        description = "Client's User from Bet365 account", 
        example = "gertrudes123"
    )