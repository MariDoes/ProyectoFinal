import os
os.system("cls")
import math

from funciones import mostrarmenucarreratercio,mostrarmenucarreraquinto,promedio,totaltercio, colegios, menuprincipal,menupostulante, cuotasistemas, cuotaadmi, cuotaarqui, beca18sist, beca18arqui, beca18admi, regresarmenucarrera, regresarmunupostulante
from funciones import notasdavid,notasmariaelena, totalnormal, totalquito, mostrarmenucarerrabeca18, mostrarmenucarreranormal, normaladmi,normalsistemas,normalarqui
# Menu principal
menuprincipal()

# Codificacion de eleccion de menu
while True:
    opcion = int(input("Seleccione una opcion del menu: "))

    # Ingreso de datos del alumno
    if (opcion == 1):
        usuario = input("Ingrese su usuario: ")
        password = input("Ingrese su contraseña: ")
        while True:
            if (usuario == "123" and password == "123"):
                # Opciones para el usilio
                print("Bienvenido alumno David, que desea realizar hoy")
                print("Le recordamos eres de la modalidad de tercio superior")
                print("Selecciona una de las opciones que desea realizar: "
                "\n1.- Numero de veces que llevas en un curso y notas"
                "\n2.- Eleccion de horarios 2020-01")

                
                opcionalum = int(input("Seleccione una opcion del menu usilio: "))
                if opcionalum == 1:
                    notasdavid()
                    x = input("Desea continuar en el menu usilio S/N: ").lower()
                    if x != "s":
                        print("Ha salido existosamente del menu usilio")
                        print("1.- Alumno usilio"
                        "\n2.- Postulante Pregrado"
                        "\n3.- Salir")
                        break

            elif (usuario == "abc" and password == "abc"):
                print("Bienvenido alumna Mariaelena, que desea realizar hoy")
                print("Le recordamos eres de la modalidad de beca 18")
                print("Selecciona una de las opciones que desea realizar: "
                "\n1.- Numero de veces que llevas en un curso"
                "\n2.- Eleccion de horarios 2020-01")

                opcionalum = int(input("Seleccione una opcion del menu usilio: "))
                if opcionalum == 1:
                    notasmariaelena()
                    x = input("Desea continuar en el menu usilio S/N: ").lower()
                    if x != "s":
                        print("Ha salido existosamente del menu usilio")
                        menuprincipal()
                        break
                    
            else:
                print("Ingresa nuevamente sus datos o seleccione otra opcion")


    elif (opcion == 2):
        menupostulante()
        while True:
            modalidad = int(input("Ingrese la modalidad por la que va postular: "))
            if modalidad == 1:
                print ("Bienvenido estás en la modalidad Excelencia academica")
                print("Por favor ingresa tus notas de cada año desde el 1° a 5° de secundaria")
                a = int(input("ingrese promedio de 1° año de secundaria: "))
                b = int(input("ingrese promedio de 2° año de secundaria: "))
                c = int(input("ingrese promedio de 3° año de secundaria: "))
                d = int(input("ingrese promedio de 4° año de secundaria: "))
                e = int(input("ingrese promedio de 5° año de secundaria: "))

                valor = (promedio(a,b,c,d,e))/5
                math.ceil(valor*100)/100

                #YA ESTA LISTO NO TOCAR QUINTO SUPERIOR 
                if 17 <= valor <=20:
                    mostrarmenucarreraquinto()
                    while True:
                        x = int(input("Ingrese la carrera a la que va postular: "))
                        # Si selecciona la carrera de ING YA ESTA
                        if x == 1:
                            print("Usted a elegido la carrera de Ingeniería informática y de sistemas")
                            colegios()
                            while True:
                                a = int(input("Ingrese el colegio en el que estudio: "))
                                if a == 1:
                                    total = totalquito(1600)
                                    descuento = total - 300 
                                    cuotasistemas(total,descuento)
                                    break
                                elif a == 2:
                                    total = totalquito(2300)
                                    descuento = total - 300 
                                    cuotasistemas(total,descuento)
                                    
                                    break
                                elif a == 3:
                                    total = totalquito(1000)
                                    descuento = total - 300 
                                    cuotasistemas(total,descuento)
                                    break
                                elif a == 4:
                                    total = totalquito(1300)
                                    descuento = total - 300 
                                    cuotasistemas(total,descuento)
                                    break
                                else:
                                    print("Opciones inexistente, seleccionar una opcion nuevamente")
                            
                            x = input("Desea continuar en esta sección S/N: ").lower()
                            if x != "s":
                                print("Ha salido existosamente")
                                break
                            else:
                                regresarmenucarrera()

                                

                        # Si selecciona la cararera de ADMI
                        elif x == 2:
                            print("Usted a elegido la carrera de Administración para los negocios")
                            colegios()
                            while True:
                                a = int(input("Ingrese el colegio en el que estudio: "))
                                if a == 1:
                                    total = totalquito(1700)
                                    descuento = total - 300 
                                    cuotaadmi(total,descuento)
                                    break
                                elif a == 2:
                                    total = totalquito(2400)
                                    descuento = total - 300 
                                    cuotaadmi(total,descuento)
                                    break
                                elif a == 3:
                                    total = totalquito(1200)
                                    descuento = total - 300 
                                    cuotaadmi(total,descuento)
                                    break
                                elif a == 4:
                                    total = totalquito(1500)
                                    descuento = total - 300 
                                    cuotaadmi(total,descuento)
                                    break
                                else:
                                    print("Opciones inexistente, seleccionar una opcion nuevamente")

                            x = input("Desea continuar en esta sección S/N: ").lower()
                            if x != "s":
                                print("Ha salido existosamente")
                                break
                            else:
                                regresarmenucarrera()

                        # Si selecciona la carrera de ARQUI
                        elif x == 3:
                            print("Usted a elegido la carrera de Arquitectura")
                            colegios()
                            while True:
                                a = int(input("Ingrese el colegio en el que estudio: "))
                                if a == 1:
                                    total = totalquito(1550)
                                    descuento = total - 300 
                                    cuotaarqui(total,descuento)
                                    break
                                elif a == 2:
                                    total = totalquito(2350)
                                    descuento = total - 300 
                                    cuotaarqui(total,descuento)
                                    break
                                elif a == 3:
                                    total = totalquito(1100)
                                    descuento = total - 300 
                                    cuotaarqui(total,descuento)
                                    break
                                elif a == 4:
                                    total = totalquito(1400)
                                    descuento = total - 300 
                                    cuotaarqui(total,descuento)
                                    break
                                else:
                                    print("Opciones inexistente, seleccionar una opcion nuevamente")

                            x = input("Desea continuar en esta sección S/N: ").lower()
                            if x != "s":
                                print("Ha salido existosamente")
                                break
                            else:
                                regresarmenucarrera()

                        elif x == 4:
                            break

                        else:
                            print("Opciones inexistente, seleccionar una opcion nuevamente")

                    x = input("Desea continuar en el menu postulante S/N: ").lower()
                    if x != "s":
                        print("Ha salido existosamente del menu postulante")
                        menuprincipal()
                        break
                    else:
                        regresarmunupostulante()

                #YA ESTA LISTO NO TOCAR TERCIO SUPERIOR
                elif 15 <= valor < 17:
                    mostrarmenucarreratercio()
                    while True:
                        x = int(input("Ingrese la carrera a la que va postular: "))
                        # Si selecciona la carrera de ING YA ESTA
                        if x == 1:
                            print("Usted a elegido la carrera de Ingeniería informática y de sistemas")
                            colegios()
                            while True:
                                a = int(input("Ingrese el colegio en el que estudio: "))
                                if a == 1:
                                    total = totaltercio(1600)
                                    descuento = total - 300
                                    cuotasistemas(total,descuento)
                                    break
                                elif a == 2:
                                    total = totaltercio(2300)
                                    descuento = total - 300
                                    cuotasistemas(total,descuento)
                                    break
                                elif a == 3:
                                    total = totaltercio(1000)
                                    descuento = total - 300
                                    cuotasistemas(total,descuento)
                                    break
                                elif a == 4:
                                    total = totaltercio(1300)
                                    descuento = total - 300
                                    cuotasistemas(total,descuento)
                                    break
                                else:
                                    print("Opciones inexistente, seleccionar una opcion nuevamente")

                            x = input("Desea continuar en esta sección S/N: ").lower()
                            if x != "s":
                                print("Ha salido existosamente")
                                break
                            else:
                                mostrarmenucarreratercio()
                                

                        # Si selecciona la cararera de ADMI
                        elif x == 2:
                            print("Usted a elegido la carrera de Administración para los negocios")
                            colegios()
                            while True:
                                a = int(input("Ingrese el colegio en el que estudio: "))
                                if a == 1:
                                    total = totaltercio(1700)
                                    descuento = total - 300
                                    cuotaadmi(total,descuento)
                                    break
                                if a == 2:
                                    total = totaltercio(2400)
                                    descuento = total - 300
                                    cuotaadmi(total,descuento)
                                    break
                                if a == 3:
                                    total = totaltercio(1200)
                                    descuento = total - 300
                                    cuotaadmi(total,descuento)
                                    break
                                if a == 4:
                                    total = totaltercio(1500)
                                    descuento = total - 300
                                    cuotaadmi(total,descuento)
                                    break

                                else:
                                    print("Opciones inexistente, seleccionar una opcion nuevamente")
                            
                            
                            x = input("Desea continuar en esta sección S/N: ").lower()
                            if x != "s":
                                print("Ha salido existosamente")
                                break
                            else:
                                mostrarmenucarreratercio()

                        # Si selecciona la carrera de ARQUI
                        elif x == 3:
                            print("Usted a elegido la carrera de Arquitectura")
                            colegios()
                            while True:
                                a = int(input("Ingrese el colegio en el que estudio: "))
                                if a == 1:
                                    total = totaltercio(1550)
                                    descuento = total - 300
                                    cuotaarqui(total,descuento)
                                if a == 2:
                                    total = totaltercio(2350)
                                    descuento = total - 300
                                    cuotaarqui(total,descuento)
                                    break
                                if a == 3:
                                    total = totaltercio(1100)
                                    descuento = total - 300
                                    cuotaarqui(total,descuento)
                                    break
                                if a == 4:
                                    total = totaltercio(1400)
                                    descuento = total - 300
                                    cuotaarqui(total,descuento)
                                    break
                                else:
                                    print("Opciones inexistente, seleccionar una opcion nuevamente")

                            x = input("Desea continuar en esta sección S/N: ").lower()
                            if x != "s":
                                print("Ha salido existosamente")
                                break
                            else:
                                mostrarmenucarreratercio()

                        elif x == 4:
                            break

                        else:
                            print("Opciones inexistente, seleccionar una opcion nuevamente")

                # Esto es una pregunta para regresar al inicio
                    x = input("Desea continuar en el menu postulante S/N: ").lower()
                    if x != "s":
                        print("Ha salido existosamente del menu postulante")
                        menuprincipal()
                        break
                    else:
                        regresarmunupostulante()

                else:
                    print("****No perteneces a ninguno de los rangos para accedeer a una beca****.")
                    x = input("Desea continuar en el menu postulante S/N: ").lower()
                    if x != "s":
                        print("Ha salido existosamente del menu postulante")
                        menuprincipal()
                        break
                    else:
                        regresarmunupostulante()

            # BECA 18
            elif modalidad == 2:
                mostrarmenucarerrabeca18()
                while True:
                    x = int(input("Ingrese la carrera a la que va postular: "))
                    if x == 1:
                        a = 1900
                        beca18sist(a)
                        x = input("Desea continuar en esta sección S/N: ").lower()
                        if x != "s":
                            print("Ha salido existosamente")
                            break
                        else:
                            mostrarmenucarerrabeca18()
                              
                               
                    elif x == 2:
                        print("Usted a elegido la carrera de Administración para los negocios")
                        a = 2000
                        beca18admi(a)
                        x = input("Desea continuar en esta sección S/N: ").lower()
                        if x != "s":
                            print("Ha salido existosamente")
                            break
                        else:
                            mostrarmenucarerrabeca18()
                                        
                        

                    elif x == 3:
                        print("Usted a elegido la carrera de Arquitectura")
                        a = 1850
                        beca18arqui(a)
                        x = input("Desea continuar en esta sección S/N: ").lower()
                        if x != "s":
                            print("Ha salido existosamente")
                            break
                        else:
                            mostrarmenucarerrabeca18()
                    
                    elif x == 4:
                            break

                    else:
                        print("Opción inexistente, seleccionar nuevamente")

                x = input("Desea continuar en el menu postulante S/N: ").lower()
                if x != "s":
                    print("Ha salido existosamente del menu postulante")
                    menuprincipal()
                    break
                else:
                    regresarmunupostulante()


                
            # ADMISION NORMAL
            elif modalidad == 3:
                mostrarmenucarreranormal()
                while True:
                    x = int(input("Ingrese la carrera a la que va postular: "))
                    if x == 1:
                        print("Usted a elegido la carrera de Ingeniería informática y de sistemas")
                        colegios()
                        while True:
                            a = int(input("Ingrese el colegio en el que estudio: "))
                            if a == 1:
                                precio = 1600
                                total = totalnormal(precio)
                                normalsistemas(total,precio)
                                break
                            elif a == 2:
                                precio = 2300
                                total = totalnormal(precio)
                                normalsistemas(total,precio)
                                break
                            elif a == 3:
                                precio = 1000
                                total = totalnormal(precio)
                                normalsistemas(total,precio)
                                break
                            elif a == 4:
                                precio = 1300
                                total = totalnormal(precio)
                                normalsistemas(total,precio)
                                break
                            
                            else:
                                print("Opciones inexistente, seleccionar una opcion nuevamente")
                        x = input("Desea continuar en esta sección S/N: ").lower()
                        if x != "s":
                            print("Ha salido existosamente")
                            break
                        else:
                            regresarmenucarrera()
                         
                                

                    elif x == 2:
                        print("Usted a elegido la carrera de Administración para los negocios")
                        colegios()
                        while True:
                            a = int(input("Ingrese el colegio en el que estudio: "))
                            if a == 1:
                                precio = 1700
                                total = totalnormal(precio)
                                normaladmi(total,precio)
                                break
                            elif a == 2:
                                precio = 2400
                                total = totalnormal(precio)
                                normaladmi(total,precio)
                                break
                            elif a == 3:
                                precio = 1200
                                total = totalnormal(precio)
                                normaladmi(total,precio)
                                break
                            elif a == 4:
                                precio = 1500
                                total = totalnormal(precio)
                                normaladmi(total,precio)
                                break
                            else:
                                print("Opciones inexistente, seleccionar una opcion nuevamente")
                        x = input("Desea continuar en esta sección S/N: ").lower()
                        if x != "s":
                            print("Ha salido existosamente")
                            break 
                        else:
                            regresarmenucarrera()

                    elif x == 3:
                        print("Usted a elegido la carrera de Arquitectura")
                        colegios()
                        while True:
                            a = int(input("Ingrese el colegio en el que estudio: "))
                            if a == 1:
                                precio = 1550
                                total = totalnormal(precio)
                                normalarqui(total,precio)
                                break
                            elif a == 2:
                                precio = 2350
                                total = totalnormal(precio)
                                normalarqui(total,precio)
                                break
                            elif a == 3:
                                precio = 1100
                                total = totalnormal(precio)
                                normalarqui(total,precio)
                                break
                            elif a == 4:
                                precio = 1400
                                total = totalnormal(precio)
                                normalarqui(total,precio)
                                break
                            else:
                                print("Opciones inexistente, seleccionar una opcion nuevamente")
                        x = input("Desea continuar en esta sección S/N: ").lower()
                        if x != "s":
                            print("Ha salido existosamente")
                            break
                        else:
                            regresarmenucarrera()

                    elif x == 4:
                        break

                    else:
                        print("Opción inexistente, seleccione nuevamente")

                x = input("Desea continuar en el menu postulante S/N: ").lower()
                if x != "s":
                    print("Ha salido existosamente del menu postulante")
                    menuprincipal()
                    break
                else:
                    regresarmunupostulante()

            
            elif modalidad == 4:
                print("Ha regresado exitosamente")
                menuprincipal()
                break
            
               

    
    elif opcion == 3:
        print("Termino la aplicacion, muchas gracias")
        break

    else:
        print("Opción inexistente, intente nuevamente")


