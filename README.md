# 🚀 challenge-envioclick

Este proyecto es parte de un reto técnico para **EnvioClick**, diseñado para demostrar habilidades en Python mediante la creación de scripts funcionales para el procesamiento de datos.

## 📁 Estructura del Proyecto

El repositorio contiene dos scripts principales:

- `priority_filter.py`: Filtra elementos en una lista según los criterios y su prioridad.
- `word_counter.py`: Cuenta la cantidad de palabras únicas en una entrada de texto.


## 🛠️ Configuración del entorno

Sigue estos pasos para clonar y preparar el entorno de desarrollo:

### 1. Clonar el repositorio

```bash
git clone https://github.com/StevenSanchezEs/challenge-envioclick.git
cd challenge-envioclick
```

### 2. Crear un entorno virtual

```bash
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

Esto instalará:

flake8 — Linter para mantener estilo y calidad del código.

black — Formateador automático de código Python.

pre-commit — Framework para ejecutar hooks antes de cada commit.

## ✅ Pre-commit

Este proyecto utiliza pre-commit para automatizar chequeos de calidad de código antes de cada commit.

### Instalación de hooks

```bash
pre-commit install
```
A partir de este punto, cada vez que hagas un commit se ejecutarán automáticamente flake8 y black.