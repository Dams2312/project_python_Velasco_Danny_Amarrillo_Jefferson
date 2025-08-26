#modulo encargado de gestionar la ruta de estudio de cada camper
import os
import json
from typing import List, Dict
#enlace con los archivos de registro json

def rutuaestudios():
    ruta = {
    'nodeJs': ['Introduccion a nodeJs', 'Manejo de paquetes con npm', 'Creacion de servidores con Express'],
    'java': ['Introduccion a Java', 'Programacion orientada a objetos', 'Manejo de excepciones'],
    'Netcore': ['Introduccion a .NetCore', 'Desarrollo de aplicaciones web con ASP.NET Core', 'Seguridad y autenticacion'],
    'fundamentos de programacion': ['introduccion al algoritmo', 'Pseint', 'python'],
    'programacion web': ['HTML', 'CSS', 'JavaScript'],
    'programacion formal': ['java','javaScript','C#'],
    'bases de datos': ['Mysql', 'MongoDB', 'PostgreSQL'],
    'Backend':['netcore','Spring BOOt','nodeJs','Express']
    }
    rutes = {}
    for rutas, modulos in ruta.items():
        rutes[rutas] = {modulo : [] for modulo in modulos}
    return rutes
    
def ver_ruta():
    rutas = rutuaestudios()
    print("""
    -------------------------------------------------
                RUTAS DE ESTUDIO 
    -------------------------------------------------
    Las rutas de estudio disponibles son:
    """)
    for ruta, modulos in rutas.items():
        print(f"- {ruta}:")
        for modulo in modulos:
            print(f"  - {modulo}")
    print("-------------------------------------------------")