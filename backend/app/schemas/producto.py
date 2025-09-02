# backend/app/schemas/producto.py
from pydantic import BaseModel, Field
from typing import Optional

class ProductoSchema(BaseModel):
    """
    Esquema de validación de datos del objeto Producto.
    Los tres puntos (...) indican campos que deben ser obligatorios.
    El nombre debe tener un máximo de 150 caracteres, el sku un máximo de 50 caracteres y la descripción un máximo de 250.
    La descripción puede ser opcional.
    La validación ge asegura que el valor de stock mínimo sea mayor o igual a 0 (en este caso), lo mismo para el stock.
    """
    nombre: str = Field(..., min_length=1, max_length=150)
    sku: str = Field(..., min_length=1, max_length=50)
    descripcion: Optional[str] = Field(default=None, max_length=250)
    stock: int = Field(default=0, ge=0)
    stock_minimo: int = Field(default=0, ge=0)

class ProductoRead(ProductoCreate):
    id: int

    class Config:
        orm_mode = True
