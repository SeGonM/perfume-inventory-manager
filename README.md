# Perfume Inventory Manager - v2.0

Bienvenido a la versión 2.0 de nuestro gestor de inventario. Este proyecto es una herramienta de software diseñada para administrar existencias, catálogos y flujos logísticos de perfumes de manera altamente eficiente, robusta, segura y profesional.

---
---

## Novedades de esta Versión

En esta actualización, hemos dado un salto de calidad masivo desde la lógica básica de programación hacia la ingeniería de software avanzada. El núcleo del sistema se ha transformado por completo: dejamos atrás el almacenamiento volátil y temporal en memoria para migrar hacia una arquitectura basada en la persistencia real, la separación estricta de responsabilidades por capas y el blindaje corporativo del sistema (Garantía de Principios ACID).

### 1. Nuevo Módulo: database.py y Persistencia Real Relacional
Hemos erradicado por completo el uso de arrays locales, listas y diccionarios en memoria que hacían que los datos se borraran al cerrar la consola. Ahora, el software se integra de forma nativa con un motor de bases de datos relacionales a gran escala.
* **Pool de Conexión Centralizado:** Implementamos un puente de comunicación seguro con MySQL Server utilizando la librería especializada `mysql-connector-python`.
* **Aislamiento de Entorno:** El módulo se encarga exclusivamente de la autenticación, control de estados de conexión y gestión de errores de handshake (como fallos de plugins de contraseñas o denegación de accesos). Esto abstrae por completo la capa de conexión para que ningún otro archivo del sistema deba preocuparse por el estado del servidor físico.

### 2. Implementación de Transacciones y Rollbacks Automatizados (Blindaje ACID)
El programa ahora es infinitamente más resistente y seguro ante fallos del sistema o del suministro eléctrico. Diseñamos un mecanismo de protección transaccional para garantizar que la base de datos jamás sufra de corrupción o almacenamiento de datos basura:
* **Atomicidad (Operaciones Todo o Nada):** El proceso para agregar un perfume es complejo, ya que requiere consultar e insertar datos de manera secuencial en múltiples tablas (Marcas, Familias, Ciudades, Proveedores y la tabla intermedia de Costos). Si el flujo se interrumpe o falla en cualquiera de estos subpasos (por ejemplo, si el NIT del proveedor está duplicado), el sistema intercepta el error y ejecuta inmediatamente un `conexion.rollback()`. Esto deshace de forma automática cualquier cambio previo, asegurando la consistencia del sistema.
* **Integridad Referencial por Motor:** Delegamos las restricciones de negocio más importantes directamente a las Llaves Foráneas (FK) y restricciones de unicidad (`UNIQUE`) de MySQL, impidiendo la creación de registros huérfanos o ubicaciones físicas duplicadas en la bodega.

### 3. Refactorización de la Arquitectura Modular por Capas
Aplicamos una reestructuración de código para separar las responsabilidades del sistema. Con este diseño, cada archivo tiene un único propósito dentro del ciclo de vida de la aplicación, eliminando el código acoplado o espagueti:
* **`logica.py` (Capa de Negocio y Datos):** Este archivo actúa como el motor central del sistema. Está completamente aislado de la interfaz de usuario; no contiene funciones `input()` ni `print()`. Su única tarea es procesar las reglas de negocio y estructurar consultas SQL de alta complejidad (sentencias transaccionales, inserciones multitabla y lecturas profundas optimizadas mediante cláusulas `JOIN` condicionales).
* **Eliminación de Redundancia:** Centralizamos la manipulación de datos para garantizar que el inventario y las búsquedas se rendericen con fluidez matemática, sin importar si el sistema maneja 10 o miles de registros simultáneos.

### 4. Robustez Operativa mediante solicitudes.py (El Escudo del Menú)
Separamos de forma definitiva la responsabilidad de capturar información desde la terminal para blindar la Experiencia de Usuario (UX) frente a fallos humanos de digitación.
* **Captura Especializada y Tipado Estricto:** Diseñamos funciones dedicadas para la conversión en tiempo real de cadenas de texto a enteros (`int`) y flotantes (`float`). Si un usuario ingresa texto por accidente en el campo de precio o stock, el sistema captura la excepción de forma silenciosa sin romper ni congelar el software.
* **Validación Dirigida mediante Lanzamiento de Excepciones (`raise`):** El programa no solo valida que el tipo de dato sea correcto, sino que evalúa la lógica del negocio. Utilizando la sentencia `raise ValueError`, forzamos al sistema a rechazar de inmediato datos numéricos incongruentes (como precios en cero, existencias negativas o identificadores inválidos), obligando al usuario a corregir la entrada antes de enviarla a la base de datos.

---

## Estructura de Archivos del Repositorio

El proyecto se encuentra estrictamente organizado bajo la siguiente topología modular:

* **`main.py`:** El punto de entrada oficial de la aplicación. Antes de inicializar la interfaz, ejecuta una "prueba de humo" para verificar de manera síncrona si el servidor MySQL está activo y respondiendo. Si la conexión es exitosa, inicializa el flujo del programa; de lo contrario, interrumpe la ejecución de forma segura y despliega un diagnóstico del error para el administrador.
* **`menu.py`:** La capa de presentación e interfaz de usuario (CLI). Controla de manera limpia, elegante y secuencial el flujo de opciones visuales del programa, delegando toda la captura a la capa de validación y el procesamiento a la capa de negocio.
* **`solicitudes.py`:** El escudo de seguridad perimetral de la aplicación. Contiene la lógica matemática encargada del control de excepciones, la limpieza de espacios en blanco (`strip`) y la validación de magnitudes comerciales.
* **`logica.py`:** El cerebro transaccional del sistema. Contiene las funciones CRUD (`agregar_perfume`, `mostrar_inventario`, `buscar_id`, `actualizar_stock`, `eliminar_perfume`) encargadas de inyectar y extraer información del motor relacional.
* **`database.py`:** La capa de persistencia pura encargada de instanciar los objetos de conexión y suministrar los cursores de comandos al sistema.
* **`scheme.sql`:** El plano arquitectónico y de ingeniería de datos. Un script estructurado que modela e inicializa la base de datos relacional compuesta por **13 tablas totalmente normalizadas** (con soporte para catálogos, tablas pivote para relaciones Muchos a Muchos, y esquemas logísticos de localización de pasillos).
* **`sample_data.sql`:** Script de simulación comercial que contiene **40 registros reales detallados** por tabla. Permite poblar los catálogos instantáneamente para realizar pruebas de estrés, carga masiva de datos y verificar la correcta alineación de los `JOIN` visuales.
* **`.gitignore`:** Archivo de configuración de Git encargado de mantener el repositorio limpio de metadatos del sistema, entornos virtuales y directorios temporales de compilación automática como `__pycache__`.

---

## Un Proceso de Mejora Continua

Este proyecto no es una estructura estática o un ejercicio académico terminado; es el testimonio directo y el reflejo de mi proceso de evolución y maduración técnica dentro del desarrollo de software.
* **Aprendizaje Consolidado:** A través de esta versión, se ha dominado el diseño y modelado de bases de datos relacionales de alta complejidad, la resolución de cardinalidades Muchos a Muchos (N:M), el control estricto de transacciones atómicas mediante código y el desarrollo de arquitecturas de software desacopladas y escalables.
* **Mentalidad de Ingeniería:** Entendemos que el software es un ente vivo que siempre puede ser optimizado. Cada línea de código escrita bajo principios de diseño limpio es un paso fundamental hacia la creación de soluciones de nivel corporativo y listos para producción.

> **"Programar no es solo hacer que un script funcione, es diseñar una estructura que sea robusta ante fallos, legible para otros ingenieros y fácil de expandir en el futuro."**

---

## Próximos pasos (Roadmap v3.0)

La evolución del sistema está planificada bajo los siguientes pilares de analítica e infraestructura de datos:
1. **Funciones de Analítica Comercial:** Desarrollo de reportes de negocio avanzados integrando consultas de agregación en SQL (`GROUP BY`, `SUM`, `COUNT`) para identificar tendencias de mercado.
2. **Ciencia de Datos e Inteligencia de Negocio:** Implementación de la librería **Pandas** para el análisis predictivo y estructurado de la rotación de inventarios, y de **Matplotlib** para la generación automatizada de gráficos estadísticos de rendimiento de stock.
3. **Interoperabilidad de Datos:** Creación de un módulo de exportación nativa para canalizar el inventario y las métricas financieras directamente hacia hojas de cálculo de **Excel (.xlsx / .csv)**.
4. **Garantía de Calidad (QA):** Implementación de una suite de pruebas unitarias (*Unit Testing*) para asegurar la estabilidad, cobertura y blindaje de las nuevas funciones analíticas antes de su despliegue.