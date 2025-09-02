from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base import Base


class RolORM(Base):
    """
    Modelo para representar los diferentes roles del sistema
    Columnas created_at y updated_at para llevar trazabilidad de la tabla.
    Utilizamos la restricción unique en el nombre del rol para que no se repitan roles en la tabla.
    """
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(120), unique=True, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    usuario_roles = relationship("UsuarioRolORM", back_populates="rol")