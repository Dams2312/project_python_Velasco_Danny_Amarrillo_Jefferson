#crea los menus que sean necesarios para el programa
def crear_menus():
    print(""" 
    -------------------------------------------------
                    WELCOME TO CAMPUS 
    -------------------------------------------------
    1.ingresar 
    2.registrarse
    3.salir
    -------------------------------------------------
    Elija una opcion:
    """
    ,end="")
    opcion = int(input())
    return opcion


def ingresar_menu():
    print("""
    -------------------------------------------------
                    INGRESAR 
    -------------------------------------------------
    1.ingresar como camper
    2.ingresar como traienr
    3.ingresar como coordinador
    4.salir
    -------------------------------------------------
    Elija una opcion:
    """
    ,end="")
    opcion = int(input())
    return opcion

def registro_menu():
    print("""
    -------------------------------------------------
                    REGISTRO 
    -------------------------------------------------
    1.registro camper
    2.registro trainer
    3.registro coordinador
    4.salir
    -------------------------------------------------
    Elija una opcion:
    """
    ,end="")
    opcion = int(input())
    return opcion


def menu_coordinador():
    print("""
    -------------------------------------------------
                BIENVENIDO OTRA VES
    -------------------------------------------------
    1.Ver aspirantes
    2.Agregar nota a aspirantes
    3.Campers aceptados
    4.Ver trainers
    5.Ver campers con bajo rendimiento
    6.Ver rutas 
    7.modulo de la ruta
    8.salir
    -------------------------------------------------
    Elija una opcion:   
    """
    ,end="")
    opcion = int(input())
    return opcion

def menu_trainer():
    print("""
    -------------------------------------------------
                BIENVENIDO OTRA VES
    -------------------------------------------------
    1.Ver campers
    2.Agregar notas a camper
    3.Ruta a seguir
    4.Ver promedio del grupo
    5.Ver campers con bajo rendimiento
    6.Ver campers con alto rendimiento
    7.salir
    -------------------------------------------------
    Elija una opcion:   
    """
    ,end="")
    opcion = int(input())
    return opcion

def menu_camper():
    print("""
    -------------------------------------------------
                BIENVENIDO OTRA VES
    -------------------------------------------------
    1.Ver notas
    2.Ver promedio
    3.Ver ruta 
    4.Ver trainer asignado
    5.ver promedio del grupo
    6.ver mi estado
    7.salir
    -------------------------------------------------
    Elija una opcion:   
    """
    ,end="")
    opcion = int(input())
    return opcion
def notas ():
    print("""
    -------------------------------------------------
                MODULO DE NOTAS
    -------------------------------------------------
    1.Registrar nota practica
    2.registrar nota teorica
    3.registrar nota quices
    4.Salir
    -------------------------------------------------
    Elija una opcion:   
    """
    ,end="")
    opcion = int(input())
    return opcion

def ruta_seguir():
    print("""
    -------------------------------------------------
                AGREGAR NOTA AL MODULO
    -------------------------------------------------
    1.modulo 1.
    2.modulo 2.
    3.modulo 3.
    4.salir
    -------------------------------------------------
    Elija una opcion:   
    """
    ,end="")
    opcion = int(input())
    return opcion