# Registro de Mascotas con Herencia y Polimorfismo 

Programa interactivo educativo que permite registrar **perros** o **gatos** usando **Programación Orientada a Objetos** (POO) con herencia múltiple y polimorfismo.

### Qué hace este código
- Clase base `Mascota` (incompleta a propósito para enseñar conceptos)
- Clases `Perro` y `Gato` que heredan de `Mascota`
- Subclases especializadas:
  - Perros: Pequeño / Mediano / Grande (según peso)
  - Gatos: Sin pelo / Pelo largo / Pelo corto
- El programa pregunta al usuario qué mascota quiere registrar
- Clasifica automáticamente según los datos ingresados
- Muestra la información personalizada de la mascota con `__str__`
