while True:
    opcion = int(input("Seleccione una opcion: "))

    if (opcion == 2):
        print("Has pulsado la opción postulante")
        print ("Seleccione una opción: ")
        print ("\t1 - Excelencia Académica")
        print ("\t2 - Beca 18")
        print ("\t3 - Admisión normal")
        print ("\t4 - regresar")
        
        
        while True:
            modalidad = int(input("ingrese la modalidad por la que va postular: "))
            if modalidad == 1:
                print ("Bienvenido estás en la modalidad Excelencia academica")
                print("Por favor ingresa tus notas de cada año desde el 1° a 5° de secundaria")
                a = int(input("ingrese promedio de 1° año de secundaria: "))
                b = int(input("ingrese promedio de 2° año de secundaria: "))
                c = int(input("ingrese promedio de 3° año de secundaria: "))
                d = int(input("ingrese promedio de 4° año de secundaria: "))
                e = int(input("ingrese promedio de 5° año de secundaria: "))
                suma = (a+b+c+d+e)
                promedio = suma/5
                print("Por favor ingresa ingresa la carrera a la que vas a postular")
                print("1 - Ingeniería informátiva y de sistemas")
                print("2 - Administración para los negocios")
                print("3 - Arquitectura")
                
                x = int(input("Ingrese la carrera a la que va postular: "))
                print("Ingrese el colegio en el que estudio")
                print("1 - Innova School"
                "\n2 - Markham"
                "\n3 - Franklin Delano Roosevelt"
                "\n4 - Raimondi"
                "\n5 - Pamer"
                "\n6 - Trilce"
                "\n7 - Augusto Salazar Bondy"
                "\n8 - Saco Oliveros"
                "\n9 - Mariano Melgar"
                "\n10 - Otros")
                #4 2 y 3 va ser caros
                #5 6 y 1 8 medios
                #7 y 9 nacional
                #10 precio general
                if x == 1:
                    print("Usted a elegido la carrera de Ingeniería informática y de sistemas")
                    

                if x == 2:
                    print("Usted a elegido la carrera de Administración para los negocios")
                    
                if x == 3:
                    print("Usted a elegido la carrera de Arquitectura")

                if 17 <= promedio <=20:
                    print("Felicitaciones estás apto para acceder a la Beca quinto superior")
                    
                if 15 <=promedio < 17:
                    print("Felicitaciones estás apto para acceder a la Beca tercio superior")
                    
                else:
                    print("no perteneces a ninguno de los rangos para accedeer a una beca.") 
                break
            
            if modalidad == 2:
                print("Bienvenido estás en la modalidad Beca 18")
                print("Por favor ingresa ingresa la carrera a la que vas a postular")
                print("1 - Ingeniería informátiva y de sistemas")
                print("2 - Administración para los negocios")
                print("3 - Arquitectura")
                x = int(input("Ingrese la carrera a la que va postular: "))
                if x == 1:
                    print("usted a elegido la carrera de Ingeniería informática y de sistemas")
                if x == 2:
                    print("Usted a elegido la carrera de Administración para los negocios")
                if x == 3:
                    print("Usted a elegido la carrera de Arquitectura")

            if modalidad == 3:
                print ("Bienvenido estás en la modalidad admisón normal")
                print("Por favor ingresa ingresa la carrera a la que vas a postular")
                print("1 - Ingeniería informátiva y de sistemas")
                print("2 - Administración para los negocios")
                print("3 - Arquitectura")
                x = int(input("Ingrese la carrera a la que va postular: "))
                if x == 1:
                    print("Usted a elegido la carrera de Ingeniería informática y de sistemas")
                if x == 2:
                    print("Usted a elegido la carrera de Administración para los negocios")
                if x == 3:
                    print("Usted a elegido la carrera de Arquitectura")
                break
            