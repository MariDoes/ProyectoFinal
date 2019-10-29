while True:
    opcion = int(input("Seleccione una opcion: "))

    if (opcion == 2):
        print("Has pulsado la opción postulante")
        modalidad = int(input("ingrese la modalidad por la que va postular"))
        
        while True:
            if modalidad == 1:
                print ("Seleccione una opción: ")
                print ("\t1 - Excelencia Académica")
                print ("\t2 - Beca 18")
                print ("\t3 - Admisión normal")
                print ("\t4 - regresar")