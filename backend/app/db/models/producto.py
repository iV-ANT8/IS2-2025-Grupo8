from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base import Base

class ProductoORM(Base):
    """
    Tabla que representa los productos localizados en los depósitos.
    Restricción de longitud en las columnas nombre, sku y descripcion para mayor seguridad y ante problemas de almacenamiento.
    La descripción puede estar vacía.
    El SKU debe ser único.
    Nombres indexados para búsquedas mas rápidas.
    Columnas created_at y updated_at para llevar trazabilidad de la tabla.
    """
    __tablename__ = "productos"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150), nullable=False, index=True)
    sku = Column(String(50), unique=True, nullable=False)
    descripcion = Column(String(250), nullable=True)
    stock = Column(Integer, default=0)
    stock_minimo = Column(Integer, default=0)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    movimientos = relationship("MovimientoORM", back_populates="producto")