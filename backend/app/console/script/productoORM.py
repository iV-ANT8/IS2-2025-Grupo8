from app.db.models import producto
from app.db.session import SessionLocal

nuevo_producto = producto.ProductoObjRM(
    nombre="Producto Ejemplo",
    sku="0001",
    descripcion="Test",
    stock=10,
    stock_minimo=2
)

with SessionLocal() as db:
    db.add(nuevo_producto)
    db.commit()

print("Producto insertado correctamente")