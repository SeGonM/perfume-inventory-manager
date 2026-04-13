# Sistema de Inventario de Perfumes - v1.1 (Migracion a Diccionarios)

Esta version representa una evolucion significativa en la arquitectura del proyecto. Se ha migrado la estructura de almacenamiento de una lista de listas a una lista de diccionarios, mejorando la legibilidad, el mantenimiento y la integridad de los datos.

## Mejoras de la Version 1.1

* Acceso por Clave: Se eliminó la dependencia de indices numericos (0, 1, 2...), ahora los datos se consultan por nombres descriptivos.
* Validacion de ID: Mejora en el proceso de insercion para evitar registros duplicados.
* Legibilidad del Codigo: Las funciones del CRUD ahora son mas intuitivas y faciles de depurar.
* Preparacion para Datos: La nueva estructura es 100% compatible con la exportacion a formatos JSON y la creacion de DataFrames con Pandas.

## Estructura de Datos (Diccionario)

Cada perfume se define ahora mediante el siguiente esquema de llaves y valores:

```python
{
    "id": int,
    "nombre": str,
    "marca": str,
    "familia": str,
    "precio": float,
    "stock": int,
    "proveedor": str
}