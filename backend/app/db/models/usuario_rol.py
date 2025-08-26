from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


class UsuarioRolObjRM(Base):
    __tablename__ = "USUARIO_ROL"
    usuario_id = Column(Integer, ForeignKey("USUARIO.id"), primary_key=True)
    rol_id = Column(Integer, ForeignKey("ROL.id"), primary_key=True)

    usuario = relationship("UsuarioObjRM", back_populates="usuario_roles")
    rol = relationship("RolObjRM", back_populates="usuario_roles")