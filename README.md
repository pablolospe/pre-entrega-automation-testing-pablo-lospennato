# Automatización de Pruebas QA (Selenium + Pytest)

Proyecto de automatización de pruebas web con Python, Selenium y Pytest sobre el sitio [SauceDemo](https://www.saucedemo.com/).

---

## Pasos para empezar a trabajar

### 1. Clonar el repositorio (si estás en otra máquina)
```bash
git clone https://github.com/pablolospe/preLabQA.git
cd preLabQA
```

### 2. Crear y activar el entorno virtual
En la raíz del proyecto ejecuta:

- **macOS / Linux:**
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```
- **Windows:**
  ```bash
  python -m venv .venv
  .venv\Scripts\activate
  ```

### 3. Instalar dependencias
Con el entorno virtual activado:
```bash
pip install -r requirements.txt
```

> **Nota para VS Code / Editor:**  
> Asegúrate de seleccionar el intérprete de Python correcto:
> 1. Presiona `Cmd + Shift + P` (o `Ctrl + Shift + P`).
> 2. Busca y selecciona **`Python: Select Interpreter`**.
> 3. Elige la opción que contiene `('.venv': venv)`.

---

## 🧪 Ejecutar los Tests

### Ejecutar todos los tests
```bash
pytest
```

### Ejecutar con reporte detallado en consola
```bash
pytest -v -s
```

### Ejecutar un archivo específico
```bash
pytest tests/test_saucedemo.py
```

### Ejecutar un test puntual dentro de un archivo
```bash
pytest tests/test_saucedemo.py -k test_01_login
```

---

## 📁 Estructura del Proyecto

```text
├── .venv/               # Entorno virtual (ignorado por git)
├── reports/             # Reportes HTML generados
├── tests/               # Casos de prueba automatizados
│   ├── test_saucedemo.py
│   ├── test_login_exito.py
│   └── test_login_glitsh.py
├── utils/               # Funciones auxiliares / helpers
│   └── helpers.py
├── conftest.py          # Fixtures y configuración global de Pytest
├── pytest.ini           # Configuración de ejecución de Pytest
├── requirements.txt     # Dependencias del proyecto
└── README.md            # Documentación del proyecto
```
