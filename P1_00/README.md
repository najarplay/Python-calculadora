# 🧮 Calculadora 1P-00

Proyecto de desarrollo de una calculadora en Python, orientado al aprendizaje, la experimentación y la implementación de una arquitectura modular mediante programación orientada a objetos (POO).

El proyecto evoluciona desde una calculadora básica hasta un sistema modular, buscando separar la lógica matemática de las interfaces de usuario para facilitar su mantenimiento, ampliación y reutilización.

## 🚀 Características

- Operaciones aritméticas básicas.
- Funciones algebraicas.
- Operaciones trigonométricas.
- Logaritmos y funciones exponenciales.
- Combinatoria.
- Estadística.
- Conversiones angulares.
- Generación de números aleatorios.
- Validación de entradas.
- Manejo de excepciones.
- Arquitectura modular y reutilizable.

## 🛠️ Tecnologías utilizadas

- Python 3.
- Programación orientada a objetos (POO).
- Módulos y paquetes de Python.
- Manejo de excepciones.
- Importación y reutilización de clases.
- Interfaz de consola.

## 📂 Estructura del proyecto

```text
calculadora/
└── P1_00/
    ├── __init__.py
    │
    ├── nucleo/
    │   ├── __init__.py
    │   ├── calculadora.py
    │   ├── cientifica.py
    │   ├── x_aleatorios.py
    │   ├── x_algebra.py
    │   ├── x_aritmetica.py
    │   ├── x_combinatoria.py
    │   ├── x_configuracion.py
    │   ├── x_constantes.py
    │   ├── x_conversiones.py
    │   ├── x_estadistica.py
    │   ├── x_logaritmos.py
    │   └── x_trigonometria.py
    │
    ├── consola_oop/
    │   ├── __init__.py
    │   ├── entrada.py
    │   ├── menu.py
    │   ├── ejecutor.py
    │   ├── aplicacion.py
    │   └── main.py
    │
    └── verciones/
        ├── v01.01.01
        ├── v01.02.01
        └── v01.02.02
```

## 🏗️ Arquitectura

El proyecto se divide en componentes independientes que permiten separar las responsabilidades y facilitar la evolución del sistema.

### Nucleo

Contiene la lógica matemática de la calculadora, organizada en módulos especializados.

Su objetivo es permitir que las operaciones sean reutilizadas por diferentes interfaces o tecnologías sin depender de una implementación específica.

### Consola OOP

Gestiona la interacción con el usuario desde la terminal.

Se encarga de la captura y validación de datos, presentación de menús, ejecución de operaciones y coordinación de la aplicación.

### Versiones

Contiene la documentación de las diferentes etapas de desarrollo, permitiendo identificar los cambios, funcionalidades y evolución de la arquitectura.

## ⚙️ Requisitos

- Python 3.
- No requiere librerías externas para el funcionamiento actual.

## ▶️ Ejecución

Desde la raíz del proyecto, ejecutar:

```bash
python -m P1_00.consola_oop.main
```

## 🎯 Objetivo del proyecto

Este proyecto forma parte de mi proceso de aprendizaje y desarrollo en Python.

Su propósito es experimentar con programación orientada a objetos, modularidad, organización de código, reutilización de componentes y separación de responsabilidades, construyendo una base que permita integrar futuras interfaces y tecnologías.

## 📌 Versiones

- **V01.01.01** — Primera versión estable de la calculadora básica.
- **V01.02.01** — Evolución monolítica con nuevas funcionalidades matemáticas.
- **V01.02.02** — Reestructuración modular del sistema y separación del núcleo matemático de la interfaz de consola.

Consulta la carpeta `verciones/` para conocer la documentación específica de cada versión.