# Sistema de Inventario de Perfumes - v1.0 (Estructura de Listas)

Este proyecto consiste en una aplicacion de consola desarrollada en Python para la gestion de un inventario de perfumeria. En esta version inicial, el sistema utiliza una estructura de lista de listas para el almacenamiento y manipulacion de los datos en memoria.

## Funcionalidades Actuales (CRUD)

El programa implementa las cuatro operaciones basicas de gestion:

* Agregar Perfume: Inserta un nuevo registro validando que el ID sea unico.
* Mostrar Inventario: Lista todos los perfumes registrados con su detalle completo.
* Buscar por ID: Recupera la informacion de un perfume especifico mediante su identificador.
* Eliminar Perfume: Remueve un registro del inventario utilizando el ID.
* Actualizar Stock: Permite modificar la cantidad de existencias de un producto de forma acumulativa.

## Detalles Tecnicos

### Estructura de Datos
Cada perfume se representa como una sublista dentro de una lista principal, siguiendo este esquema de indices:

| Indice | Campo      | Tipo Dato  |
| :----- | :--------- | :--------- |
| 0      | ID         | int        |
| 1      | Nombre     | str        |
| 2      | Marca      | str        |
| 3      | Familia    | str        |
| 4      | Precio     | float      |
| 5      | Stock      | int        |
| 6      | Proveedor  | str        |

### Modularizacion
El codigo esta dividido en tres modulos para separar la logica de la interfaz:

1. main.py: Inicializacion del programa.
2. menu.py: Manejo de entradas del usuario y visualizacion en consola.
3. logica.py: Funciones de procesamiento y manipulacion de la lista.

---
Nota: Esta documentacion registra el estado del proyecto antes de realizar la migracion de la estructura de datos a diccionarios.
