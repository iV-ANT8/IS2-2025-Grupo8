from app.db.models.producto import ProductoORM
from app.schemas.producto import ProductoRead as Producto
from app.domain.mappers.producto_mapper import producto_orm_to_dto, producto_dom_to_orm

def test_producto_mapper():
    # Definimos el ORM
    orm = ProductoORM(
        nombre="Test",
        sku="123",
        descripcion="desc",
        stock=5,
        stock_minimo=1
    )
    # Convertir de ORM a DTO
    dto = producto_orm_to_dto(orm)
    print(dto)

    # Convertir de DTO a ORM
    nuevo_orm = producto_dom_to_orm(dto)
    print(vars(nuevo_orm))

if __name__ == "__main__":
    test_producto_mapper()