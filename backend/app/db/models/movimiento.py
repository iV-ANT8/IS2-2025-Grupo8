from sqlalchemy import Column, Integer, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from app.db.base import Base
import enum

class TipoMovimientoEnum(enum.Enum):
    ENTRADA = "entrada"
    SALIDA = "salida"

class MovimientoObjRM(Base):
    __tablename__ = "MOVIMIENTO"
    id = Column(Integer, primary_key=True, index=True)
    producto_id = Column(Integer, ForeignKey("PRODUCTO.id"))
    deposito_origen_id = Column(Integer, ForeignKey("DEPOSITO.id"))
    deposito_destino_id = Column(Integer, ForeignKey("DEPOSITO.id"))
    usuario_id = Column(Integer, ForeignKey("USUARIO.id"))
    cantidad =  Column(Integer, nullable=False)
    fecha = Column(DateTime, nullable=False)
    tipo = Column(Enum(TipoMovimientoEnum), nullable=False)

    producto = relationship("ProductoObjRM", back_populates="movimientos")
    usuario = relationship("UsuarioObjRM", back_populates="movimientos")
    deposito_origen = relationship(
        "DepositoObjRM",
        foreign_keys=[deposito_origen_id],
        back_populates="movimientos_origen"
    )
    deposito_destino = relationship(
        "DepositoObjRM",
        foreign_keys=[deposito_destino_id],
        back_populates="movimientos_destino"
    )