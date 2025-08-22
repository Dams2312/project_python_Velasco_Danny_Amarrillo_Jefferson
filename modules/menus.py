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


