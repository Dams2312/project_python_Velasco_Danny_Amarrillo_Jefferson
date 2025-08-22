#modulo encargado de aser el registro de los campers
import os
import json
from typing import Dict

#enlace con los archivos de registro json
procesos = "modules/procesos.json"
rute_train_cord = "modules/trainer_coordinador.json"
#LIBRERIAS PARA EL REGISTRO DE CAMPERS
proceso_estudent = {}
registro_camper = {}

#LIBRERIAS PARA EL REGISTRO DE TRAINERS Y COORDINADORES
proceso_trainer = {}
registro_trainer = {}

# Funciones para el registro de campers
def registro_camper(proceso_estudent:Dict , registro_camper: Dict)-> None:
    os.system("cls")
    print("""
    -------------------------------------------------
                    REGISTRO CAMPER 
    -------------------------------------------------
    Por favor, ingrese los siguientes datos:     
    Nombre: """, end="")
    nombre = input()
    print("Apellido: ", end="")
    apellido = input()
    print("Edad: ", end="")
    edad = int(input())
    print("Correo electrónico: ", end="")
    correo = input()
    print("Teléfono: ", end="")
    telefono = input()
    print("direccion ", end="")
    direccion = input()
    print ("acudiente: ",end="")
    acudiente = input()
    print("numero de identificacion: ", end="")
    identificacion = input()
    
    print(f"""
    -------------------------------------------------
                    REGISTRO EXITOSO 
    -------------------------------------------------
    Bienvenido {nombre} {apellido}, tu registro ha sido exitoso.
    """)

# Funciones para el registro de trainers 
# registrar los demas argumentos que se necesiten
def registro_trainer():
    os.system("cls")
    print("""
    -------------------------------------------------
                    REGISTRO TRAINER 
    -------------------------------------------------
    Por favor, ingrese los siguientes datos:     
    Nombre: """, end="")
    nombre = input()
    print("Apellido: ", end="")
    apellido = input()
    print("Edad: ", end="")
    edad = int(input())
    print("Correo electrónico: ", end="")
    correo = input()
    print("Teléfono: ", end="")
    telefono = input()
    print("numero de identificacion: ", end="")
    identificacion = input()
    print ("experiencia (en meses): ", end="")
    experiencia = int(input())
    
    
    print(f"""
    -------------------------------------------------
                    REGISTRO EXITOSO 
    ------º-------------------------------------------
    Bienvenido {nombre} {apellido}, tu registro ha sido exitoso.
    """)

#registrar los demas argumentos que se necesitan
# Funciones para el registro de coordinadores
def registro_coordinador():
    os.system("cls")
    print("""
    -------------------------------------------------
                    REGISTRO COORDINADOR 
    -------------------------------------------------
    Por favor, ingrese los siguientes datos:     
    Nombre: """, end="")
    nombre = input()
    print("Apellido: ", end="")
    apellido = input()
    print("Edad: ", end="")
    edad = int(input())
    print("Correo electrónico: ", end="")
    correo = input()
    print("Teléfono: ", end="")
    telefono = input()
    print("numero de identificacion: ", end="")
    identificacion = input()
    print ("experiencia (en meses): ", end="")
    experiencia = int(input())  


    print(f"""
    -------------------------------------------------
                    REGISTRO EXITOSO 
    -------------------------------------------------
    Bienvenido {nombre} {apellido}, tu registro ha sido exitoso.
    """)


# FUNCIONES DE LECTURA DE ARCHIVOS
def read_json(file_path : str) -> Dict:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        return {}

# funcion para escribir en un archivo json
def write_json(file_path : str, data : Dict) -> None:
    try
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        print(f"Error al escribir en el archivo {file_path}: {e}")

