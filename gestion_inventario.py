"""
MÓDULO: Entornos de Desarrollo (1DM3)
EXAMEN: Depuración de Código en VS Code
EJERCICIO: Sistema de Gestión de Inventario (gestion_inventario.py)

"""

IVA_fl = 0.21


def fn_EliminarAgotados_lst(productos_lst):
    """
    Elimina del inventario los productos con stock 0
    y devuelve la lista de productos que quedan.
    """
    for producto_dic in productos_lst:
        if producto_dic["stock"] == 0:
            productos_lst.remove(producto_dic)

    return productos_lst


def fn_ValorPorCategoria_dic(productos_lst):
    """
    Calcula el valor del inventario (precio x unidades en stock)
    agrupado por categoría.
    """
    valores_dic = {}

    for producto_dic in productos_lst:
        categoria_str = producto_dic["categoria"]
        precio_fl = producto_dic["precio"]
        unidades_int = producto_dic["minimo"]
        valor_fl = precio_fl * unidades_int

        valores_dic[categoria_str] = valores_dic.get(categoria_str, 0) + valor_fl

    return valores_dic


def fn_ClasificarStock_str(stock_int, minimo_int):
    """
    Clasifica el estado del stock de un producto:
    - 'AGOTADO': stock igual a 0.
    - 'BAJO': stock igual o inferior al mínimo.
    - 'OK': stock por encima del mínimo.
    """
    if stock_int == 0:
        estado_str = "AGOTADO"
    elif stock_int <= minimo_int:
        estado_str = "BAJO"
    else:
        estado_str = "OK"

    return estado_str


def fn_ProductosAReponer_lst(productos_lst):
    """
    Devuelve los nombres de los productos que hay que pedir al proveedor.
    Hay que reponer un producto si su stock está en el mínimo (o por debajo)
    Y además NO tiene ya un pedido pendiente de llegada.
    """
    a_reponer_lst = []

    for producto_dic in productos_lst:
        bajo_bool = producto_dic["stock"] <= producto_dic["minimo"]

        if bajo_bool or not producto_dic["pendiente"]:
            a_reponer_lst.append(producto_dic["nombre"])

    return a_reponer_lst


def fn_RegistrarIncidencia_lst(mensaje_str, historial_lst=[]):
    """
    Añade una incidencia a un historial y lo devuelve.
    Si no se indica ningún historial, se empieza uno nuevo (vacío).
    """
    historial_lst.append(mensaje_str)

    return historial_lst


def fn_CalcularPrecioConIVA_fl(precio_fl):
    """
    Devuelve el precio de venta al público con el IVA incluido.
    """
    return precio_fl * (1 + IVA_fl)


def main():
    print("=== SISTEMA DE GESTIÓN DE INVENTARIO - ALMACÉN ===")

    # Datos de prueba
    inventario_lst = [
        {"nombre": "Teclado",  "categoria": "Periféricos", "precio": 25.0,  "stock": 40, "minimo": 10, "pendiente": False},
        {"nombre": "Ratón",    "categoria": "Periféricos", "precio": 12.5,  "stock": 0,  "minimo": 15, "pendiente": True},
        {"nombre": "Monitor",  "categoria": "Pantallas",   "precio": 150.0, "stock": 0,  "minimo": 5,  "pendiente": False},
        {"nombre": "Webcam",   "categoria": "Periféricos", "precio": 40.0,  "stock": 8,  "minimo": 10, "pendiente": False},
        {"nombre": "Portátil", "categoria": "Equipos",     "precio": 600.0, "stock": 5,  "minimo": 3,  "pendiente": False},
        {"nombre": "Tablet",   "categoria": "Equipos",     "precio": 300.0, "stock": 2,  "minimo": 4,  "pendiente": True},
    ]

    print("\n1. Eliminando productos agotados del inventario...")
    inventario_lst = fn_EliminarAgotados_lst(inventario_lst)
    print(f"   Productos en inventario: {len(inventario_lst)}")
    for producto_dic in inventario_lst:
        estado_str = fn_ClasificarStock_str(producto_dic["stock"], producto_dic["minimo"])
        print(f"   - {producto_dic['nombre']}: stock {producto_dic['stock']} ({estado_str})")

    print("\n2. Valor del inventario por categoría...")
    valores_dic = fn_ValorPorCategoria_dic(inventario_lst)
    for categoria_str, valor_fl in valores_dic.items():
        print(f"   {categoria_str}: {valor_fl:.2f}€")

    print("\n3. Productos a reponer...")
    a_reponer_lst = fn_ProductosAReponer_lst(inventario_lst)
    print(f"   Hay que pedir {len(a_reponer_lst)} producto(s): {', '.join(a_reponer_lst)}")

    print("\n4. Registro de incidencias por almacén...")
    incidencias_norte_lst = fn_RegistrarIncidencia_lst("Palé dañado")
    incidencias_sur_lst = fn_RegistrarIncidencia_lst("Etiqueta ilegible")
    incidencias_norte_lst = fn_RegistrarIncidencia_lst("Retraso del transportista", incidencias_norte_lst)
    print(f"   Incidencias almacén norte: {len(incidencias_norte_lst)}")
    print(f"   Incidencias almacén sur: {len(incidencias_sur_lst)}")

    print("\n5. Precio de venta con IVA...")
    precio_portatil_fl = fn_CalcularPrecioConIVA_fl(600.0)
    print(f"   Portátil: {precio_portatil_fl:.2f}€")


if __name__ == "__main__":
    main()
