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
    
    # aqui es donde pedimos los datos del camper y para poder hacer su registro con datos "basicos" para saber quien es 
    
    print(f"""
    -------------------------------------------------
                    REGISTRO EXITOSO 
    -------------------------------------------------
    Bienvenido {nombre} {apellido}, tu registro ha sido exitoso.
    """)