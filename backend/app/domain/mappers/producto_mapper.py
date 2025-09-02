from app.db.models.producto import ProductoORM
from app.schemas.producto import ProductoRead as Producto

def producto_orm_to_dto(orm: ProductoORM) -> Producto:

    """
        Usando Pydantic se convierte un ORM a dominio
    """
    return Producto.model_validate(orm)

def producto_dom_to_orm(dom: Producto) -> ProductoORM:
    """
        Usando Pydantic se convierte un dominio a ORM
    """
    data = dom.model_dump(exclude_unset=True) # no sobreescribe valores nulos
    return ProductoORM(**data) # convierte el diccionario en un objeto ORM