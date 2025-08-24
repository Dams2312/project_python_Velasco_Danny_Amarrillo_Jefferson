#modulo que se encarga de la supervicion y coordinacion de los campers mediante los trainers y el coordinador
import os
import json
from typing import list,Dict
import modules.menus as mn
import modules.registro as re 
rute_train_cord = "data/traeiner_cordinador.json"
def trainer(): 
    while True:
        os.system("cls")
        clave = input("Por favor ingrese su clave: ")
        lectura = re.read_json(rute_train_cord)
        if clave in lectura:
            print(f"Bienvenido {lectura[clave]['nombre']} {lectura[clave]['apellido']}")
            mn.menu_trainer()
        else:
            print("Clave incorrecta, por favor intente de nuevo.")
            input("Presione Enter para continuar...")
            continue