from sqlalchemy import Column, Integer, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base import Base
import enum

class TipoMovimientoEnum(enum.Enum):
    ENTRADA = "entrada"
    SALIDA = "salida"

class MovimientoORM(Base):
    """
    Tabla de movimientos del inventario.
    Columnas created_at y updated_at para llevar trazabilidad de la tabla.
    Se indexan usuario, fecha y producto para que las búsquedas de los mismos sean más rápidas.
    Se utilizan foreign keys en las relationships ya que creamos relaciones con la misma tabla.
    """
    __tablename__ = "movimientos"
    id = Column(Integer, primary_key=True)
    producto_id = Column(Integer, ForeignKey("productos.id"), index=True)
    deposito_origen_id = Column(Integer, ForeignKey("depositos.id"))
    deposito_destino_id = Column(Integer, ForeignKey("depositos.id"))
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), index=True)
    cantidad =  Column(Integer, nullable=False)
    fecha = Column(DateTime, nullable=False, index=True)
    tipo = Column(Enum(TipoMovimientoEnum), nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    producto = relationship("ProductoORM", back_populates="movimientos")
    usuario = relationship("UsuarioORM", back_populates="movimientos")
    deposito_origen = relationship(
        "DepositoORM",
        foreign_keys=[deposito_origen_id],
        back_populates="movimientos_origen"
    )
    deposito_destino = relationship(
        "DepositoORM",
        foreign_keys=[deposito_destino_id],
        back_populates="movimientos_destino"
    )