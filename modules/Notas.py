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
            clave = input("Ingrese la cédula del estudiante: ")
            date = re.read_json(rute)

            if clave in date:
                estudiante = date[clave]
                rutas = estudiante.get("ruta_estudio")

                if not rutas:
                    print(" El estudiante no tiene ruta asignada.")
                    continue

                # Accede al nombre de la ruta (solo hay una)
                nombre_ruta = list(rutas.keys())[0]
                modulos = rutas[nombre_ruta]
                lista_modulos = list(modulos.keys())

                # Mostrar menú para seleccionar módulo
                print("\nSeleccione el módulo:")
                for i, modulo in enumerate(lista_modulos, 1):
                    print(f"{i}. {modulo}")
                print("0. Salir")
                opcion_modulo = int(input("Opción: "))

                if opcion_modulo == 0 or opcion_modulo > len(lista_modulos):
                    print("Saliendo...")
                    break

                modulo_elegido = lista_modulos[opcion_modulo - 1]

                # Mostrar menú de notas
                menu_N = mn.notas()
                match menu_N:
                    case 1:
                        nota = float(input("Ingrese la nota práctica (0-100): "))
                        if 0 <= nota <= 100:
                            nota_calc = nota * 0.6
                            modulos[modulo_elegido].append(("práctica", nota_calc))
                        else:
                            print("Error: La nota debe estar entre 0 y 100.")

                    case 2:
                        nota = float(input("Ingrese la nota teórica (0-100): "))
                        if 0 <= nota <= 100:
                            nota_calc = nota * 0.3
                            modulos[modulo_elegido].append(("teórica", nota_calc))
                        else:
                            print("Error: La nota debe estar entre 0 y 100.")

                    case 3:
                        nota = float(input("Ingrese la nota del quiz (0-100): "))
                        if 0 <= nota <= 100:
                            nota_calc = nota * 0.1
                            modulos[modulo_elegido].append(("quiz", nota_calc))
                        else:
                            print("Error: La nota debe estar entre 0 y 100.")

                    case 4:
                        print("Saliendo del módulo de notas.")
                        break
                    case _:
                        print("Opción inválida, intente otra vez.")
                        continue

                # Calcular nota final sumando solo las ponderadas
                notas_del_modulo = modulos[modulo_elegido]
                suma_total = sum(n[1] for n in notas_del_modulo if isinstance(n[1], float))
                
                # Añadir o reemplazar nota final
                notas_del_modulo = [n for n in notas_del_modulo if n[0] != "final"]
                notas_del_modulo.append(("final", round(suma_total, 2)))
                modulos[modulo_elegido] = notas_del_modulo

                # Guardar los cambios
                re.write_json(rute, date)
                print(" Nota registrada con éxito.\n")

            else:
                print(" No existe un estudiante con esa cédula.")

        except ValueError:
            print("Error: Entrada inválida. Por favor, ingrese un número.")

