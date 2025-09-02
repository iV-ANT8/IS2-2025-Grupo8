from app.db.engine import engine
from app.db.base import Base
from app.db.models import producto
from app.db.session import SessionLocal

Base.metadata.create_all(bind=engine, tables=[producto.ProductoORM.__table__])

nuevo_producto = producto.ProductoORM(
    nombre="Producto Ejemplo",
    sku="0010",
    descripcion="Test",
    stock=10,
    stock_minimo=2
)

with SessionLocal() as db:
    db.add(nuevo_producto)
    db.commit()

print("Producto insertado correctamente")