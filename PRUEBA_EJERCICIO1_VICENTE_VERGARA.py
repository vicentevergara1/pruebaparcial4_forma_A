# PRUEBA EJERCICIO 1

usuarios = [
    {
        "Nombre" : "Pepito777",
        "Sexo" : "M",
        "Contraseña" : "Duoc2024"
    }
]

def menu():
    while True:
        print("----- MENU USUARIOS ----")
        print("1.- Ingresar usuario")
        print("2.- Buscar usuario")
        print("3.- Eliminar usuario")
        print("4.- Salir")
        try:
            op = int(input("Ingresa una opcion:"))
        except ValueError:
            print("Error, solo numeros enteros validos")
            continue

        def ingresar():
                agregar_nombre = input("Ingresa el nombre de usuario:")
                encontrado = False
                for usuario in usuarios:
                    if agregar_nombre == usuario['Nombre']:
                        print("Usuario ya registrado!!!")
                        encontrado = True
                        continue
                    else:
                        sexo = input("Ingresa el genero (M/F) (M:Masculino/F:Femenino):")
                        if sexo == "M" or sexo == "F":
                            
                            contrasena = input("Ingrese una contraseña (Minimo 8 Caracteres, minimo 1 numero y 1 letra ¡Sin espacios!):")
                            agregar_usuario = [
                                {
                                    "Nombre": agregar_nombre,
                                    "Sexo" : sexo,
                                    "Contraseña" : contrasena
                                }
                            ]
                            usuarios.extend(agregar_usuario)
                            print("Usuario agregado exitosamente")
                            return
                        else:
                            print("Debe ingresar M o F solamente, reintente de nuevo")
                            continue
                            
                    

        def buscar():
            buscar_usuario = input("Ingresa el nombre:")
            encontrado = False
            for usuario in usuarios:
                if buscar_usuario == usuario['Nombre']:
                    print(f"Nombre: {usuario['Nombre']}")
                    print(f"Sexo: {usuario['Sexo']}")
                    print(f"Contraseña: {usuario['Contraseña']}")
                    encontrado = True
                    
            if not encontrado:
                print("Usuario no encontrado")

        def eliminar():
            nombre = input("Ingresa el nombre:")
            encontrado = False
            for usuario in usuarios:
                if nombre == usuario['Nombre']:
                    usuarios.remove(usuario)
                    print("Usuario eliminado exitosamente")
                    encontrado = True
                    
            if not encontrado:
                print("No se pudo eliminar usuario!")

        #def mostrar():
            #print(f"{usuarios}")


        if op == 1:
            ingresar()

        elif op == 2:
            buscar()
        
        elif op == 3:
            eliminar()
        
        #elif op == 4:
            #mostrar()

        elif op == 4:
            print("Programa terminado...")
            break

        else:
            print("Debe ingresar una opcion valida!!")

menu()