#modulo encargado de gestionar las notas de los estudiantes

def registrar_nota():
    print("""
    -------------------------------------------------
                    REGISTRO DE NOTA 
    -------------------------------------------------
    Por favor, ingrese los siguientes datos:     
    Nombre del estudiante: """, end="")
    nombre_estudiante = input()
    print("Asignatura: ", end="")
    asignatura = input()
    print("Nota: ", end="")
    nota = float(input())
    
    print(f"""
    -------------------------------------------------
                    REGISTRO EXITOSO 
    -------------------------------------------------
    La nota de {nombre_estudiante} en {asignatura} ha sido registrada exitosamente.
    """)

    