#modulo que se encarga de la supervicion y coordinacion de los campers mediante los trainers y el coordinador
import os
import json
from typing import List,Dict
import menus as mn
import registro as re 
rute_trainer = "data/trainer.json"
rute_coordinador = "data/coordinador.json"
rute_aspirante = "data/proceso.json"
ruter_camper = "data/estudiantes.json"

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
                        aspirantes = re.read_json(rute_aspirante)
                        if aspirantes:
                            print("Lista de aspirantes:")
                            for id, info in aspirantes.items():
                                print(f"ID: {id}, Nombre: {info['nombre']}, Apellido: {info['apellido']}")
                        else:
                            print("No hay aspirantes registrados.")
                        continue
                    case 2:
                        #agregar nota de aspirante
                        while True:
                            try:
                                clave = input("Ingrese la clave del aspirante al cual quiera añadir la nota: ")
                                date = re.read_json(rute_aspirante)
                                if clave in date:
                                    nota = float(input("Ingrese la nota (0-100): "))
                                    if 0 <= nota <= 100:
                                        date[clave]['nota'] = nota
                                        re.write_json(rute_aspirante, date)
                                        print(f"Nota {nota} agregada al aspirante {date[clave]['nombre']} {date[clave]['apellido']}.")
                                        if nota >= 70:
                                            print("El aspirante ha sido aceptado.")
                                            print("agregando a la vase de datos de campers......")
                                            estudiantes = re.read_json(ruter_camper)
                                            estudiantes[clave] = date[clave]
                                            date.pop(clave)
                                            re.write_json(ruter_camper, estudiantes)
                                            re.write_json(rute_aspirante, date)
                                        else:
                                            print("El aspirante no ha sido aceptado.")
                                            date.pop(clave)
                                            re.write_json(rute_aspirante, date)
                                    else:
                                        print("Error: La nota debe estar entre 0 y 100.")
                                    print("desea agregar otra nota? (s/n): ", end="")
                                    resp = input().lower()
                                    if resp != 's':
                                        break
                                    else:
                                        continue
                                else:
                                    print("Clave no encontrada. Por favor, intente de nuevo.")
                                    continue
                            except ValueError:
                                print("Error: Entrada inválida. Por favor, ingrese un número.")
                            
                    case 3:
                        #campers aceptados
                        aspirantes = re.read_json(ruter_camper)
                        if aspirantes:
                            print("Lista de aspirantes:")
                            for id, info in aspirantes.items():
                                print(f"ID: {id}, Nombre: {info['nombre']}, Apellido: {info['apellido']}")
                        else:
                            print("No hay aspirantes registrados.")
                        continue
                    case 4:
                        #listar trainers
                        aspirantes = re.read_json(rute_trainer)
                        if aspirantes:
                            print("Lista de aspirantes:")
                            for id, info in aspirantes.items():
                                print(f"ID: {id}, Nombre: {info['nombre']}, Apellido: {info['apellido']}")
                        else:
                            print("No hay aspirantes registrados.")
                        continue
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