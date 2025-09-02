from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base import Base


class UsuarioRolORM(Base):
    """
    Tabla intermedia para la relación muchos-a-muchos entre Usuario y Rol.
    Cada registro une un usuario con un rol específico.
    Se indexan el usuario_id y rol_id para que las búsquedas de los mismos sean más rápidas.
    Columnas created_at y updated_at para llevar trazabilidad de la tabla.
    """
    __tablename__ = "usuarios_roles"
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), primary_key=True, index=True)
    rol_id = Column(Integer, ForeignKey("roles.id"), primary_key=True, index=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    usuario = relationship("UsuarioORM", back_populates="usuario_roles")
    rol = relationship("RolORM", back_populates="usuario_roles")