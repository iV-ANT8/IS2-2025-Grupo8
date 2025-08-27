from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base import Base

class UsuarioORM(Base):
    """
    Modelo de usuario, incluye roles, movimientos y trazabilidad.
    La contraseña debe estar hasheada.
    Los emails deben se únicos.
    Las columnas username, email y hashed_password tienen restricción de longitud para mayor seguridad y ante problemas de almacenamiento.
    Se indexan el username y el email para que las búsquedas de los mismos sean más rápidas.
    Columnas created_at y updated_at para llevar trazabilidad de la tabla.
    Si se borra un usuario se borran sus roles.
    """
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, index=True)
    email = Column(String(120), unique=True, nullable=False, index=True)
    hashed_password = Column(String(128), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    usuario_roles = relationship("UsuarioRolORM", back_populates="usuario", cascade="all, delete-orphan")
    movimientos = relationship("MovimientoORM", back_populates="usuario")