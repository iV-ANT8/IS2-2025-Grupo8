# Este archivo es para probar que las clases de domain y schemas funcionan.

# Importa las clases que creaste
from backend.app.domain.producto import Producto
from backend.app.schemas.producto import ProductoCreate, ProductoRead

# --- Prueba del dominio (la clase Producto) ---
print("--- Prueba del modelo de dominio ---")
producto_dominio = Producto(
    nombre="Lapicera",
    sku="LP001",
    stock=50,
    stock_minimo=5
)
print(f"Objeto de dominio creado: {producto_dominio.nombre}")
print("---")

# --- Prueba de los esquemas (Pydantic) ---
print("--- Prueba del esquema Pydantic ---")

# Crea una instancia del esquema de creación (ProductoCreate)
producto_create = ProductoCreate(
    nombre="Goma",
    sku="G001",
    stock=100,
    stock_minimo=10
)

# Imprime el esquema en formato de diccionario
print(f"Objeto de esquema creado: {producto_create.nombre}")
print(producto_create.model_dump_json(indent=2))
print("---")

# Crea una instancia del esquema de lectura (ProductoRead)
# Este simula un objeto que viene de la base de datos con un ID
producto_read = ProductoRead(
    id=1,
    nombre="Sacapuntas",
    sku="S001",
    stock=20,
    stock_minimo=2
)
print(f"Objeto de lectura (con ID) creado: {producto_read.nombre}")
print(producto_read.model_dump_json(indent=2))
