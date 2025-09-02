# backend/app/domain/producto.py

class Producto:
    def __init__(self, nombre: str, sku: str, stock: int, stock_minimo: int):
        self.nombre = nombre
        self.sku = sku
        self.stock = stock
        self.stock_minimo = stock_minimo
