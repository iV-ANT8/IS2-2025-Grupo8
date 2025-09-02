from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base import Base

class DepositoORM(Base):
    """
    Tabla para representar los depósitos físicos.
    Columnas created_at y updated_at para llevar trazabilidad de la tabla.
    Se utilizan foreign keys en las relationships ya que creamos relaciones con la misma tabla.
    Restricción de longitud en las columnas nombre y ubicación para mayor seguridad y ante problemas de almacenamiento.
    Se indexan nombre y ubicación para que las búsquedas de los mismos sean más rápidas.
    El nombre debe ser único.
    """
    __tablename__ = "depositos"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(120), nullable=False, unique=True, index=True)
    ubicacion = Column(String(200), nullable=False, index=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    movimientos_origen = relationship(
        "MovimientoORM",
        back_populates="deposito_origen",
        foreign_keys="MovimientoORM.deposito_origen_id",
    )
    movimientos_destino = relationship(
        "MovimientoORM",
        back_populates="deposito_destino",
        foreign_keys="MovimientoORM.deposito_destino_id"
    )