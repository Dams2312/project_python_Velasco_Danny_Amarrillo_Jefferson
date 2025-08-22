"""
Nombre: Danny Julian Velasco Olarte, Jefferson Andres Amarillo Rios
Fecha: 2023-10-30
Descripcion: Desarrollo de programa de inscripción y acompañamiento los campers en su proceso de formación
"""

import os
import json
from typing import List, Dict
import modules.menus as mn

while True:
    try:
        match mn.crear_menus():
        case 1:
            try:
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
            except ValueError:
                print("Opción inválida. Por favor, intente de nuevo.")
        case 2:
            try:
                match mn.registro_menu():
                case 1:
                    print("Registrando camper...")
                    # Aquí iría la lógica para registrar camper
                case 2:
                    print("Registrando trainer...")
                    # Aquí iría la lógica para registrar trainer
                case 3:
                    print("Registrando coordinador...")
                    # Aquí iría la lógica para registrar coordinador
                case 4:
                    continue
            except ValueError:
                print("Opción inválida. Por favor, intente de nuevo.")

        case 3:
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
        
    except ValueError:
        pass
