# Perfume Inventory Manager - v1.3

Bienvenido a la **versión 1.3** de nuestro gestor de inventario. Este proyecto es una herramienta diseñada para administrar existencias de perfumes de manera eficiente, robusta y profesional.

## Novedades de esta Versión

En esta actualización, hemos dado un salto de calidad desde la programación básica hacia la **ingeniería de software**, enfocándonos en la modularidad y la experiencia del usuario (UX).

### 1. Nuevo Módulo: `solicitudes.py` 
He separado la responsabilidad de capturar datos. Ahora, el menú no "pelea" con el usuario, simplemente delega esa tarea a funciones especializadas que garantizan datos limpios.
* **Encapsulamiento:** El código es más fácil de mantener al estar dividido por funciones.
* **Reutilización:** Una misma función de solicitud sirve para agregar, buscar o actualizar.

### 2. Implementación de `try`, `except` y `raise` 
El programa ahora es mucho más resistente. He implementado un sistema de blindaje para que el software no se detenga ante errores comunes:
* **Manejo de Excepciones:** Usamos `try/except` para capturar ingresos accidentales de texto en campos numéricos.
* **Validación de Negocio:** Mediante el uso de `raise`, forzamos al programa a rechazar datos que, aunque son números, no tienen sentido en nuestro negocio (como precios negativos o IDs inválidas).

### 3. Refactorización del Menú 
Gracias a la nueva arquitectura, el archivo `menu.py` es ahora una pieza de código limpia y elegante. Se eliminó la repetición de código (principio DRY - *Don't Repeat Yourself*), permitiendo una lectura fluida de la lógica principal.

---

## Estructura del Repositorio

- **`main.py`**: El punto de entrada. Aquí definí el inventario inicial y arrancamos la aplicación.
- **`menu.py`**: La interfaz de usuario. Maneja el flujo de opciones del programa.
- **`solicitudes.py`**: El "escudo" del programa. Contiene toda la lógica de validación y captura de datos.
- **`logica.py`**: El motor del sistema. Aquí residen las funciones CRUD (Crear, Leer, Actualizar, Eliminar).
- **`.gitignore`**: Configurado para mantener el repositorio limpio de archivos basura como `__pycache__`.

---

## Un Proceso de Mejora Continua

Este proyecto no es estático; es un reflejo de mi proceso de aprendizaje. 
* **Aprendizaje:** En esta versión dominamos el control de excepciones y la modularización.
* **Mentalidad:** Entendemos que el software siempre puede mejorar. Cada línea de código escrita es un paso hacia una solución más profesional.
* **Próximos pasos:** En futuras versiones buscaremos la persistencia de datos y una interfaz aún más amigable.

---

> "Programar no es solo hacer que funcione, es hacer que sea robusto, legible y fácil de mejorar."
