from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt
from datetime import datetime
from enum import Enum

class Categoria(str, Enum):
    categoria1 = "Categoria 1"
    categoria2 = "Categoria 2"
    categoria3 = "Categoria 3"


class Vendas(BaseModel):
    email: EmailStr
    data: datetime
    valor: PositiveFloat
    produto: str
    quantidade: PositiveInt
    categoria: Categoria

