#modulo encargado de gestionar las notas de los estudiantes

# funcion para corregir con ciclos while y exeptions de try y execpts
import os
import json
from typing import List, Dict
import modules.registro as re
import modules.menus as mn
rute = "data/estudiantes.json"
def nota_practica():          
    while True:
        try:
            clave = input("Ingrese la clave del estudiane al cual quiera añadir la nota: ")
            date = re.read_json(rute)
            if clave in date:
                menu = mn.ruta_seguir()
                match menu:
                    case 1:
                        menu_N = mn.notas()
                        match menu_N:
                            case 1:
                                nota = float(input("Ingrese la nota (0-100): "))
                                if 0 <= nota <= 100:
                                    pract = nota * 0.6

                                else:
                                    print("Error: La nota debe estar entre 0 y 100.")
                            case 2:
                                teoria = float(input("Ingrese la nota (0-100): "))
                                teorica = teoria * 0.3
                            case 3:
                                quiz = float(input("Ingrese la nota (0-100): "))
                                quices = quiz * 0.1
                            case 4:
                                print("Saliendo del módulo de notas.")
                                break
                            case _:
                                print("Opción inválida, intente otra vez.")



        except ValueError:
            print("Error: Entrada inválida. Por favor, ingrese un número.")
