from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class DepositoObjRM(Base):
    __tablename__ = "DEPOSITO"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    ubicacion = Column(String, nullable=False)

    movimientos_origen = relationship(
        "MovimientoObjRM",
        back_populates="deposito_origen",
        foreign_keys="[MovimientoObjRM.deposito_origen_id]"
    )
    movimientos_destino = relationship(
        "MovimientoObjRM",
        back_populates="deposito_destino",
        foreign_keys="[MovimientoObjRM.deposito_destino_id]"
    )