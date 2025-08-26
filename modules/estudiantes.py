#parte donde el estudiante puede ver sus notas y el promedio de las mismas

import os
import json
from typing import List, Dict
import modules.registro as re

rute = "data/estudiantes.json"

#funcion para ver las notas del estudiante
def ver_notas() -> None:
    while True:
        try:
            os.system("cls")
            registros = re.read_json(rute)
            estudiante = input("Ingrese su número de identificación para ver sus notas: ")
    
            if not estudiante or 'notas' not in estudiante:
                print("No se encontraron notas para este estudiante.")
        
    
            notas = estudiante['notas']
            print(f"""
            -------------------------------------------------
                        NOTAS DEL ESTUDIANTE 
            -------------------------------------------------
            Notas de {estudiante['nombre']} {estudiante['apellido']}:
            """)
    
            total = 0
            for asignatura, nota in notas.items():
                print(f"- {asignatura}: {nota}")
                total += nota
    
                promedio = total / len(notas) if notas else 0
                print(f"Promedio: {promedio:.2f}")
                print("-------------------------------------------------")
            print("desea mirarar notas de otro estudiante? (s/n): ", end="")
            resp = input().lower()
            if resp != 's':
                break
        except ValueError:
            print("Error: Entrada inválida. Por favor, ingrese un número.")

