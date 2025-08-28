"""
jefferso amarillo
28/agost/25
comando para mejorar la vista de los trainers 
"""

import os
import json
import trainer_cordinador as trainer
import rutas as Ruta
import registro as reg
triner_Rut = 'data/trainer.json '

ruta_trainer= 'data/triner.json'
def triner_Rut():
    while True:
        try:
            clav = int(input("ingrese su clave de acceso para visualizar su ruta, si desea salir ingrese la palabra 'salir': "))
            if clav in trainer.trainer_campus:
                print("usted esta registrado, en unos segundos accedera a su ruta.....")
                print(reg.registro_trainer)
                print(Ruta.rutuaestudios)
                return 
            elif clav == "salir":
                break 
            else:
                print("usted no se encuentra registrado, o ha ingresado una contraseña invalida")
                break

    
    
        except ValueError:
            print("has ingreado datos no validos")     
