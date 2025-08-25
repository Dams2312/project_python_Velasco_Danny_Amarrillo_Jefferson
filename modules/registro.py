#modulo encargado de aser el registro de los campers
import os
import json
from typing import Dict

#enlace con los archivos de registro json
procesos = "data/procesos.json"
rute_train = "data/trainer.json"
rute_coordinador = "data/coordinador"

# Funciones para el registro de campers
def registro_camper()-> None:
    while True:
        try:
            #LIBRERIAS PARA EL REGISTRO DE CAMPERS
            proceso_estudent = {}
            Registro_camper = {}
            
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
            
            registrar_camper = read_json(procesos)
            
            if identificacion in registrar_camper:
                print("El camper con esta identificación ya está registrado.")
                continue
            else:
                Registro_camper.update({str(identificacion): proceso_estudent})
                proceso_estudent = {
                "nombre": nombre,
                "apellido": apellido,
                "edad": edad,
                "correo": correo,
                "telefono": telefono,
                "direccion": direccion,
                "acudiente": acudiente,
                "identificacion": identificacion
            }
                write_json(procesos, Registro_camper)
            
            print(f"""
            -------------------------------------------------
                            REGISTRO EXITOSO 
            -------------------------------------------------
            Bienvenido {nombre} {apellido}, tu registro ha sido exitoso.
            """)
            print("Desea registrar otro camper? (s/n): ", end="")
            if input().lower() == 's':
                continue
            elif input().lower() == 'n':
                break
            else:
                print("Opción invalida. saliendo al menu principal...")
                break
            
        except ValueError:
            print("Error en el ingreso de datos. Por favor, intente de nuevo.")

# Funciones para el registro de trainers 
def registro_trainer()-> None:
    while True:
        try:
            #LIBRERIAS PARA EL REGISTRO DE TRAINERS Y COORDINADORES
            proceso_trainer = {}
            Registro_trainer = {}
            
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
            
            leer_trainer = read_json(rute_train)
            
            if identificacion in leer_trainer:
                print("El trainer con esta identificación ya está registrado.")
                continue
            else:
                Registro_trainer.update({str(identificacion): proceso_trainer})
                proceso_trainer = {
                "nombre": nombre,
                "apellido": apellido,
                "edad": edad,
                "correo": correo,
                "telefono": telefono,
                "identificacion": identificacion,
                "experiencia": experiencia
            }
                write_json(rute_train, Registro_trainer)
            
            print(f"""
            -------------------------------------------------
                            REGISTRO EXITOSO 
            ------º-------------------------------------------
            Bienvenido {nombre} {apellido}, tu registro ha sido exitoso.
            """)
            print("Desea registrar otro trainer? (s/n): ", end="")
            if input().lower() == 's':
                continue
            elif input().lower() == 'n':
                break
            else:
                print("Opción invalida. saliendo al menu principal...")
                break
            
        except ValueError:
            print("Error en el ingreso de datos. Por favor, intente de nuevo.")

#registrar los demas argumentos que se necesitan
def registro_coordinador()-> None:
    while True:
        try:
            #LIBRERIAS PARA EL REGISTRO DE TRAINERS Y COORDINADORES
            proceso_coordinador = {}
            Registro_coordinador = {}
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
            
            coordinador = read_json(rute_coordinador)
            
            if identificacion in coordinador:
                print("El coordinador con esta identificación ya está registrado.")
                continue
            else:
                Registro_coordinador.update({str(identificacion): proceso_coordinador})
                proceso_coordinador = {
                "nombre": nombre,
                "apellido": apellido,
                "edad": edad,
                "correo": correo,
                "telefono": telefono,
                "identificacion": identificacion,
                "experiencia": experiencia
            }
                write_json(rute_coordinador, Registro_coordinador)
    
            print(f"""
            -------------------------------------------------
                            REGISTRO EXITOSO 
            -------------------------------------------------
            Bienvenido {nombre} {apellido}, tu registro ha sido exitoso.
            """)
            print("Desea registrar otro coordinador? (s/n): ", end="")
            if input().lower() == 's':  
                continue
            elif input().lower() == 'n':
                break
            else:
                print("Opción invalida. saliendo al menu principal...")
                break
        except ValueError:
            print("Error en el ingreso de datos. Por favor, intente de nuevo.")


# FUNCIONES DE LECTURA DE ARCHIVOS
def read_json(file_path : str) -> Dict:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
            
    except FileNotFoundError:
        return {}

# funcion para escribir en un archivo json
def write_json(file_path : str, data : Dict) -> None:
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        print(f"Error al escribir en el archivo {file_path}: {e}")

