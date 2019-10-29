print("Bienvenidos a nuestro sistema matricula"
"\ndonde aca le ayudaremos a darle informacion si eres postulante"
"\no estudiante actual en nuestra universidad")
print("Selecciona una de las opciones de su preferencia")
print("1.- Alumno usilio"
"\n2.- Postulante Pregrado"
"\n3.- Salir")
while True:
    opcion = int(input("Seleccione una opcion: "))

    if (opcion == 1):
        usuario = input("Ingrese su usuario: ")
        password = input("Ingrese su contraseña: ")
        if (usuario == "123" and password == "123"):
                print("Bienvenido alumno David, que desea realizar hoy")
                print("Le recordamos eres de la modalidad de tercio superior")
                print("Selecciona una de las opciones que desea realizar: "
                "\n1.- Numero de veces que llevas en un curso"
                "\n2.- Eleccion de horarios 2020-01")
                opcionalum = input("Seleccione una opcion: ")
                if opcionalum == 1:
                    CalculoI = 1
                    FisicaI = 1
                    Poo = 1
                    Taller = 1
                    Marketing = 1
                    Intro = 1
                    print("Reporte universitario: "
                    print("En Calculo I lo esta llevando por ", CalculoI)
                    print("En Fisica I uno lo esta llevando por ", FisicaI)
                    print("En Poo lo esta llevando por ", Poo)
                    print("En Taller lo esta llevando por ", Taller)
                    print("En Marketing lo esta llevando por ", Marketing)
                    print("En Intro lo esta llevando por ", Intro)







    if opcion == 3:
        break



