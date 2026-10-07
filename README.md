# Pre-Entrega: Automatización de Pruebas QA

Este proyecto es la pre-entrega del curso de QA Automation. Consiste en automatizar casos de prueba sobre la web [SauceDemo](https://www.saucedemo.com/) usando Selenium WebDriver con Python y Pytest.

El objetivo es validar flujos críticos de usuario (autenticación, catálogo de productos y carrito de compras) aplicando buenas prácticas de testing automatizado, estrategias de localización de elementos, esperas explícitas y modularización de código.

---

## Tecnologías usadas

- Python
- Selenium WebDriver
- Pytest
- pytest-html (para sacar el reporte en html)
- webdriver-manager (para manejar el chromedriver)
- Git / GitHub

---

## Pruebas que están automatizadas

Todo está dentro de `tests/test_saucedemo.py`:

- **Login:**
  - Login con el usuario `standard_user` y contraseña `secret_sauce`.
  - Validación de que redireccione bien a `/inventory.html`, el título de la página y el texto "Products".
- **Catálogo / Inventario:**
  - Que esté visible el menú hamburguesa y el selector de ordenamiento/filtros.
  - Que haya productos cargados en la página.
  - Comprobación de que el primer producto tenga nombre y precio.
- **Carrito de compras:**
  - Agregar el primer producto y chequear que el botón pase a decir "Remove".
  - Comprobar que el número en el icono del carrito cambie a 1.
  - Entrar al carrito (`/cart.html`) y validar que el producto agregado sea el correcto.

---

## Cómo levantarlo y correrlo

### 1. Clonar el repo

```bash
git clone https://github.com/pablolospe/pre-entrega-automation-testing-pablo-lospennato.git
cd pre-entrega-automation-testing-pablo-lospennato
```

### 2. Crear y activar el entorno virtual

En Mac / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

En Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

---

## Ejecución de los tests

Con el entorno virtual activado:

Para correr todos los tests y generar el reporte:

```bash
pytest
```

*(Ya configuré en el `pytest.ini` los flags para que guarde el reporte en la carpeta `reports/`).*

O también se puede correr a mano con los flags que pedía la consigna:

```bash
pytest tests/test_saucedemo.py -v --html=reports/reporte.html --self-contained-html
```

El reporte se genera en `reports/reporte.html` y se puede abrir directo con Chrome o cualquier navegador para ver los resultados.

---

## Estructura del proyecto

```text
pre-entrega-automation-testing-pablo-lospennato/
├── tests/
│   └── test_saucedemo.py     # los tests automatizados
├── utils/
│   └── helpers.py            # funciones auxiliares (login, agregar al carrito)
├── conftest.py               # fixtures de pytest (driver y usuario logueado)
├── pytest.ini                # config de pytest para armar el reporte html
├── requirements.txt          # paquetes necesarios
├── .gitignore                # para ignorar .venv, reportes y cache
└── README.md                 # explicacion del proyecto
```
