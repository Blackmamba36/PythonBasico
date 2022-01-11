import random 

usuario = ["Andrés", "Felipe", "Luis", "Allison", "Pedro", "Sofía", "Macarena", "Elon", "Job", "Matías"]
cuentas = []

def creacionCuenta(usuarios):



    for u in usuarios:
        cuenta={}
        cuenta["Nombre"] = u
        cuenta["Passsword"]= generarPassword()
        cuenta["N contacto"]= str(ingresarNumeroContacto(u))
        cuenta.append(cuenta)


def generarPassword():

    numeros = "0123456789"
    minusculas = "qwertyuipoñlkjhgfdsazxcvbnm"
    matusculas = "QWERTYUIOPÑLKJHGFDSAZXCVBNM"
    password = ""

    for i in range(3):
        password+=str(random.choice(numeros)) + str(random.choice(mayusculas)) + str(random.choice(minusculas))
    
    return password


def ingresarNumeroContacto(usu):

    while True : 
        n = int(input("Debe ingresar un numero de contacto para " + str(usu) + "de 8 digitos : "))
        if len(str(n))==8:
            break
        else:
            print("Número incorrecto")
        
    return n 


def mostrarCuentas():
    for cuenta in cuentas:
        print("Nombre: ", cuenta["Nombre"], "Password: ", cuenta["Password"],"N de contacto: ", cuenta["N contacto"])

print("Sistema de cuentas de usuarios")

creacionCuenta(usuario)
mostrarCuentas()