#modulo que se encarga de la supervicion y coordinacion de los campers mediante los trainers y el coordinador
import os
import json
from typing import List,Dict
import modules.menus as mn
import modules.registro as re 
rute_trainer = "data/trainer.json"
rute_coordinador = "data/coordinador.json"

def coordinador(): 
    while True:
        try:
            os.system("cls")
            print("------------BIENVENIDO-----------")
            clave = input("Por favor ingrese su clave: ")
            lectura = re.read_json(rute_coordinador)
            if clave in lectura:
                print(f"Bienvenido {lectura[clave]['nombre']} {lectura[clave]['apellido']}")
                coordiner = mn.menu_coordinador()
                match coordiner:
                    case 1:
                        #Listar aspirantes
                        pass
                    case 2:
                        #agregar nota de aspirante
                        pass
                    case 3:
                        #campers aceptados
                        pass
                    case 4:
                        #listar trainers
                        pass
                    case 5:
                        #ver los campers de bajo rendimiento
                        pass
                    case 6:
                        #listar y ver las rutas de trainers y campers en salon
                        pass
                    case 7:
                        #modulo de la ruta entrenamiendo aprobados y desaprobados
                        pass
                    case 8:
                        print("Saliendo......")
                        break
                    case _:
                        print("opcion invalida, intente otra ves")
            else:
                print("Clave incorrecta, por favor intente de nuevo.")
                input("Presione Enter para continuar...")
                continue
        except ValueError:
            print("a ingresado una opcion invalida por favor intente otra ves")
            os.system("cls")
            continue

def trainer_campus():
    while True:
        try:
            print("------BIENVENIDO-------")
            clave = input("por favor ingrese su clave: ")
            date = re.read_json(rute_trainer)
            if clave in date:
                entrenador = mn.menu_trainer()
                match entrenador:
                    case 1:
                        #ver campers relacionados al trainer
                        pass
                    case 2:
                        #agregar notas a camper
                        pass
                    case 3:
                        #ruta a seguir por el trainer 
                        pass
                    case 4:
                        #ver promedio del grupo
                        pass
                    case 5:
                        #ver campers con bajo rendimiento
                        pass
                    case 6:
                        #ver campers con alto rendimiento
                        pass
                    case 7:
                        print("Saliendo......")
                        break
                    case _:
                        print("opcion invalida intentelo otra ves")
                        continue
            else:
                print("Clave incorrecta, por favor intente de nuevo.")
                input("Presione Enter para continuar...")
                continue
        except ValueError:
            print("a ingresado una opcion invalida por favor intente otra ves")
            os.system("cls")
            continue