# backend/app/schemas/producto.py
from pydantic import BaseModel

class ProductoCreate(BaseModel):
    nombre: str
    sku: str
    stock: int
    stock_minimo: int

class ProductoRead(ProductoCreate):
    id: int

    class Config:
        orm_mode = True
