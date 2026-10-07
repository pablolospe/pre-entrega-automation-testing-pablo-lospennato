from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.helpers import add_first_product_to_cart, login

def test_01_login(driver):
    login(driver)
    assert "/inventory.html" in driver.current_url , "ERROR: No se redirigió a /inventory.html"
    assert driver.title == "Swag Labs"
    assert driver.find_element(By.CLASS_NAME, "title").text == "Products"


def test_02_verificar_inventario(logged_in_driver):
    driver = logged_in_driver
    page_title = driver.title
    section_title = driver.find_element(By.CLASS_NAME, "title").text

    assert page_title == "Swag Labs" , f'ERROR: Titulo de ventana esperado "swag labs", Obtenido {page_title}'

    assert section_title == 'Products' , f'ERROR: Titulo de seccion esperado "products", Obtenido {section_title}'


def test_03_productos_visibles(logged_in_driver):
    driver = logged_in_driver
    inventory_item = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    assert len(inventory_item) > 0 , f'ERROR: No se encontraron productos visibles'
    

def test_04_validad_interfaz(logged_in_driver):
    driver = logged_in_driver
    menu_button = driver.find_element(By.ID, 'react-burger-menu-btn')
    filtro = driver.find_element(By.CLASS_NAME, 'product_sort_container')


    assert menu_button.is_displayed(), f'ERROR: Menu no esta visible'
    assert filtro.is_displayed(), f'ERROR: filtro no esta visible'


def test_05_añadir_producto_al_carrito(logged_in_driver):
    add_first_product_to_cart(logged_in_driver)
    boton = logged_in_driver.find_element(
        By.CSS_SELECTOR, ".inventory_item button"
    )
    assert boton.text == "Remove", 'ERROR: el boton no cambio a "Remove"'


def test_06_verificar_contador_carrito(logged_in_driver):
    add_first_product_to_cart(logged_in_driver)
    contador_carrito = logged_in_driver.find_element(
        By.CLASS_NAME, 'shopping_cart_badge'
    ).text

    assert contador_carrito == "1" ,f'ERROR: Se esperaba 1 , obtuvo {contador_carrito}'


def test_07_navegar_carrito(logged_in_driver):
    driver = logged_in_driver
    driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
    assert "/cart.html" in driver.current_url , "ERROR: No se redirigió a /cart.html"

def test_08_comprobar_poducto_en_el_carrito(logged_in_driver):
    add_first_product_to_cart(logged_in_driver)
    logged_in_driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
    producto_nombre_en_carrito = logged_in_driver.find_element(
        By.CLASS_NAME, 'inventory_item_name'
    ).text

    assert producto_nombre_en_carrito == 'Sauce Labs Backpack' , f'ERROR: NO ES EL MISMO NOMBRE'

def test_09_primer_producto_tiene_nombre_y_precio(logged_in_driver):
    driver = logged_in_driver
    first_item = driver.find_element(By.CLASS_NAME, 'inventory_item')
    nombre = first_item.find_element(By.CLASS_NAME, 'inventory_item_name').text
    precio = first_item.find_element(By.CLASS_NAME, 'inventory_item_price').text

    assert nombre != '', 'ERROR: El primer producto no tiene nombre'
    assert precio != '', 'ERROR: El primer producto no tiene precio'
    assert nombre == 'Sauce Labs Backpack', 'ERROR: El primer producto no tiene el nombre esperado'
    assert precio == '$29.99', 'ERROR: El primer producto no tiene el precio esperado'