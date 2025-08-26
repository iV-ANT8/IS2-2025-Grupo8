from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class ProductoObjRM(Base):
    __tablename__ = "PRODUCTO"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    sku = Column(String, unique=True, nullable=False)
    descripcion = Column(String, nullable=True)
    stock = Column(Integer, default=0)
    stock_minimo = Column(Integer, default=0)

    movimientos = relationship("MovimientoObjRM", back_populates="producto")