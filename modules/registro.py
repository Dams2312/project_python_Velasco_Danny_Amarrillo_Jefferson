#modulo encargado de aser el registro de los campers
def registro_camper():
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

def registro_trainer():
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


def registro_coordinador():
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