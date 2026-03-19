"""Módulo simple de registro de productos.
Este script permite registrar productos desde la consola, mostrando validación
básica de entrada (nombre no vacío, precio no negativo, cantidad entera no negativa)
y posteriormente listar los productos registrados.

Estructura interna:
products = { id_producto: (nombre, precio, cantidad) }

ID de producto es autoincremental interno y se calcula según la cantidad de productos,
conel pobjetivo de tener un identificador único para cada producto.
"""

def input_str(message:str, required=True)->str:
    """Leer una cadena desde input y validar que no esté vacía.

    Args:
        message (str): Mensaje que se muestra al usuario en entrada de datos..
        required (bool): Si True, vuelve a pedir si la cadena está vacía.

    Returns:
        str: Cadena ingresada (puede ser vacía si required=False).
    """
    
    while True:
        value = input(message).strip()
        if not value and required:
            print("Error 01: el valor no puede estar vacío. Intenta de nuevo.")
            continue
        return value

def input_float(message:str, min_value:int)->float:
    """Leer un número float desde input y validar que sea un número válido y mayor o igual a min_value.
    Args:
        message (str): Mensaje que muetsra al usuario en entrada de datos.
        min_value (float): Valor mínimo permitido.
    Returns:
        float: Número ingresado por el usuario.
    """
    while True:
        
        try:
            value = float(input(message))
        except ValueError:
            print("Error 02: ingresa un número válido (ej: 15.50).")
            continue
        if min_value is not None and value < min_value:
            print(f"Error 03: el valor debe ser mayor o igual a {min_value}.")
            continue
        return value

def input_int(message, min_value):
    """Leer un entero válido y opcionalmente validar mínimo.

    Args:
        message (str): Mensaje que se muestra al usuario.
        min_value (int|None): valor mínimo aceptado. Si None, no hay restricción.

    Returns:
        int: Valor ingresado.
    """
    while True:
        try:
            value = int(input(message))
        except ValueError:
            print("Error 04: ingresa un entero válido (ej: 10).")
            continue
        if min_value is not None and value < min_value:
            print(f"Error 03: el valor debe ser mayor o igual a {min_value}.")
            continue
        return value

def register_product(products):
    """Registrar un producto nuevo en el diccionario de productos.

        Args:
            products (dict): Diccionario donde se almacenan los productos.

    Returns:
        None
    """
    #ID autoincremental basado en la cantidad de productos registrados.
    id_product = len (products) + 1 

    #Entrada del nombre a través de función de validacion de cadenas.
    name_product = input_str ('1.Enter the name of the product: ')
    price_product = input_float ('2.Enter the price of the product: ', 0)
    quantity_product = input_int ('3.Enter the quantity of the product: ', 1)

    #Registros de productos en el diccionario, despues de ser validados.
    products[id_product] = (name_product, price_product, quantity_product)

    #Confirmación de registro exitoso y vista de productos registrados.
    print(f'\nProduct registered successfully. Total products: {len(products)}')
    
    #Vista de productos diccionario.
    for ID, product in products.items():
        print (f'PRODUCTOS: ID: {ID} | Name: {product[0]} | Price: {product[1]} | Quantity: {product[2]}\n')

"""Función principal que controla el flujo de registro continuo."""
o=0
products = {}
while o == 0 :
    register_product(products)
    o= int(input ("Do you want to make a new register? 0 for yes, 1 for no: "))




