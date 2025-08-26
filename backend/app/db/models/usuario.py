from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.db.base import Base

class UsuarioObjRM(Base):
    __tablename__ = "USUARIO"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

    usuario_roles = relationship("UsuarioRolObjRM", back_populates="usuario")
    movimientos = relationship("MovimientoObjRM", back_populates="usuario")