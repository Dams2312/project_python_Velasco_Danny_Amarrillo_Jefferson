"""
Nombre: Danny Julian Velasco Olarte, Jefferson Andres Amarillo Rios
Fecha: 2023-10-30
Descripcion: Desarrollo de programa de inscripción y acompañamiento los campers en su proceso de formación
"""

import os
import json
from typing import List, Dict
import modules.menus as mn
import modules.registro as re
import modules.estudiantes as es
import modules.trainer_cordinador as tc
import modules.examen_jefferson_amarillo as ex
from data import trainer as TR

if __name__ == "__main__":
    while True:
        try:
            match mn.crear_menus():
                case 1:
                    match mn.ingresar_menu():
                        case 1:
                            print("Ingresando como camper...")
                            es.ver_notas()
                        case 2:
                            print("Ingresando como trainer...")
                            tc.trainer_campus()
                        case 3:
                            print("Ingresando como coordinador...")
                            tc.coordinador()
                        case 4:
                            continue
                case 2:
                    match mn.registro_menu():
                        case 1:
                            re.registro_camper()
                        case 2:
                            re.registro_trainer()
                        case 3:
                            re.registro_coordinador()
                        case 4:
                            print("saliendo")
                            continue
                case 3:
                    print("Gracias por usar el programa. ¡Hasta luego!")
                    break
                case _:
                    print("opcion invalida intente otra ves.")
                    continue
        except ValueError:
            pass

if ex.triner_Rut in TR:
    print("ested pronto accedera a ud ruta y se le seleccionara un salon en cuanto hayan los suficientes estudiantes ")

else:
    print("usted no esta registrado como trainer o su contraseña es erronea")
