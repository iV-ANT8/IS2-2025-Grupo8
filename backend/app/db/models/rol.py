from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class RolObjRM(Base):
    __tablename__ = "ROL"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)

    usuario_roles = relationship("UsuarioRolObjRM", back_populates="rol")