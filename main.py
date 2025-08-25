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

if __name__ == "__main__":
    while True:
        try:
            match mn.crear_menus():
                case 1:
                    match mn.ingresar_menu():
                        case 1:
                            print("Ingresando como camper...")
                            # Aquí iría la lógica para ingresar como camper
                        case 2:
                            print("Ingresando como trainer...")
                            # Aquí iría la lógica para ingresar como trainer
                        case 3:
                            print("Ingresando como coordinador...")
                            # Aquí iría la lógica para ingresar como coordinador
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
