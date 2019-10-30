# Menu principal
print("Bienvenidos a nuestro sistema matricula"
"\ndonde aca le ayudaremos a darle informacion si eres postulante"
"\no estudiante actual en nuestra universidad")
print("Selecciona una de las opciones de su preferencia")
print("1.- Alumno usilio"
"\n2.- Postulante Pregrado"
"\n3.- Salir")

# Codificacion de eleccion de menu
while True:
    opcion = int(input("Seleccione una opcion del menu: "))

    # Ingreso de datos del alumno
    if (opcion == 1):
        usuario = input("Ingrese su usuario: ")
        password = input("Ingrese su contraseña: ")
        if (usuario == "123" and password == "123"):
                # Opciones para el usilio
                print("Bienvenido alumno David, que desea realizar hoy")
                print("Le recordamos eres de la modalidad de tercio superior")
                print("Selecciona una de las opciones que desea realizar: "
                "\n1.- Numero de veces que llevas en un curso y notas"
                "\n2.- Eleccion de horarios 2020-01")

                
                opcionalum = int(input("Seleccione una opcion del menu usilio: "))
                if opcionalum == 1:
                    print("Reporte de cursos: ")
                    print("En Calculo I lo has pasado con 15, pasaste a la 1era " )
                    print("En Fisica I lo has pasado con 14, pasaste a la 1era ")
                    print("En Poo lo has pasado con 17, pasaste a la 1era")
                    print("En Taller lo has pasado con 18, pasaste a la 1era")
                    print("En Marketing lo has pasado con 14, pasaste a la 1era")
                    print("En Intro lo has pasado con 17, pasaste a la 1era")
                    print("Esta disponible a llevar los cursos siguientes")

        elif (usuario == "abc" and password == "abc"):
                print("Bienvenido alumna Mariaelena, que desea realizar hoy")
                print("Le recordamos eres de la modalidad de beca 18")
                print("Selecciona una de las opciones que desea realizar: "
                "\n1.- Numero de veces que llevas en un curso"
                "\n2.- Eleccion de horarios 2020-01")

                opcionalum = int(input("Seleccione una opcion del menu usilio: "))
                if opcionalum == 1:
                    print("Reporte de cursos: ")
                    print("En Calculo I no lo has pasado, nota 10, lo llevaras por 2da vez " )
                    print("En Estadistica lo has pasado con 14, pasaste a la 1era ")
                    print("En Poo lo has pasado con 17, pasaste a la 1era")
                    print("En Taller lo has pasado con 13, pasaste a la 1era")
                    print("En ADD lo has pasado con 14, pasaste a la 1era")
                    print("En Fisica general lo has pasado con 17, pasaste a la 1era")
                    print("Esta disponible a llevar los cursos siguientes pero no de Calculo II")
                    
        else:
            print("Ingresa nuevamente sus datos o seleccione otra opcion")

    
    if opcion == 3:
        print("Termino la aplicacion, muchas gracias")
        break


