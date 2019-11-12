import os
os.system("cls")
while True:
    try:
        opcion = int(input("Seleccione una opcion: "))
    except ValueError:
        print("introduce una de las opciones mostradas")
        opcion = int(input("Seleccione una opcion: "))
    pass

    if (opcion == 2):
        print("Has pulsado la opción postulante")
        print ("Seleccione una opción: ")
        print ("\t1 - Excelencia Académica")
        print ("\t2 - Beca 18")
        print ("\t3 - Admisión normal")
        print ("\t4 - regresar")
        
        
        while True:
            try:
                modalidad = int(input("Ingrese la modalidad por la que va postular: "))
            except ValueError:
                print("ingrese una de las opciones mostradas")
                modalidad = int(input("Ingrese la modalidad por la que va postular: "))
            if modalidad == 1:
                print ("Bienvenido estás en la modalidad Excelencia academica")
                print("Por favor ingresa tus notas de cada año desde el 1° a 5° de secundaria")
                try:
                    a = int(input("ingrese promedio de 1° año de secundaria: "))
                    b = int(input("ingrese promedio de 2° año de secundaria: "))
                    c = int(input("ingrese promedio de 3° año de secundaria: "))
                    d = int(input("ingrese promedio de 4° año de secundaria: "))
                    e = int(input("ingrese promedio de 5° año de secundaria: "))
                except ValueError:
                    print("ingrese una de las notas del colegio")
                    a = int(input("ingrese promedio de 1° año de secundaria: "))
                    b = int(input("ingrese promedio de 2° año de secundaria: "))
                    c = int(input("ingrese promedio de 3° año de secundaria: "))
                    d = int(input("ingrese promedio de 4° año de secundaria: "))
                    e = int(input("ingrese promedio de 5° año de secundaria: "))
                suma = (a+b+c+d+e)
                promedio = suma/5

                #YA ESTA LISTO NO TOCAR QUINTO SUPERIOR 
                if 17 <= promedio <=20:
                    print("Felicitaciones estás apto para acceder a la Beca quinto superior")
                    print("Por favor ingresa ingresa la carrera a la que vas a postular")
                    print("1 - Ingeniería informátiva y de sistemas")
                    print("2 - Administración para los negocios")
                    print("3 - Arquitectura")
                    x = int(input("Ingrese la carrera a la que va postular: "))
                    # Si selecciona la carrera de ING YA ESTA
                    if x == 1:
                        print("Usted a elegido la carrera de Ingeniería informática y de sistemas")
                        print("1 - Innova School / Tricel / Pamer / Saco Oliveros"
                        "\n2 - Markham / Raimondi / Franklin Delano Roosevelt "
                        "\n3 - Mariano Melgar / Augusto Salazar Bondy"
                        "\n4 - Otros")
                        while True:
                            try:
                                a = int(input("Ingrese el colegio en el que estudio: "))
                            except ValueError:
                                print("ingrese una de las opciones mostradas")
                                a = int(input("Ingrese el colegio en el que estudio: "))
                            if a == 1:
                                matricula = 300
                                precio = 1600 
                                descuento = precio*0.5
                                total = descuento + matricula
                                print("*****Aqui esta su boleta de matricula******")
                                print("Carrera: Ing de Sistemas, pagaras en su primera cuota:", total, "luego pagará cada una de las demás cuotas:",descuento)
                                print("Si desea continuar con el proceso, venga a nuestros establecimiento, gracias.")
                                break
                            if a == 2:
                                matricula = 300
                                precio = 2300
                                descuento = precio*0.5
                                total = descuento + matricula
                                print("*****Aqui esta su boleta de matricula******")
                                print("Carrera: Ing de Sistemas, pagaras en su primera cuota:", total, "luego pagará cada una de las demás cuotas:",descuento)
                                print("Si desea continuar con el proceso, venga a nuestros establecimiento, gracias.")
                                break
                            if a == 3:
                                matricula = 300
                                precio = 1000
                                descuento = precio*0.5
                                total = descuento + matricula
                                print("*****Aqui esta su boleta de matricula******")
                                print("Carrea: Ing de Sistemas, pagaras en su primera cuota:", total, "luego pagará cada una de las demás cuotas:",descuento)
                                print("Si desea continuar con el proceso, venga a nuestros establecimiento, gracias.")
                                break
                            if a == 4:
                                matricula = 300
                                precio = 1300
                                descuento = precio*0.5
                                total = descuento + matricula
                                print("*****Aqui esta su boleta de matricula******")
                                print("Carrera: Ing de Sistemas, pagaras en su primera cuota:", total, "luego pagará cada una de las demás cuotas:",descuento)
                                print("Si desea continuar con el proceso, venga a nuestros establecimiento, gracias.")
                                break
                            else:
                                print("Opciones inexistente, seleccionar una opcion nuevamente")

                            

                    # Si selecciona la cararera de ADMI
                    if x == 2:
                        print("Usted a elegido la carrera de Administración para los negocios")
                        print("Usted a elegido la carrera de Ingeniería informática y de sistemas")
                        print("1 - Innova School / Tricel / Pamer / Saco Oliveros"
                        "\n2 - Markham / Raimondi / Franklin Delano Roosevelt "
                        "\n3 - Mariano Melgar / Augusto Salazar Bondy"
                        "\n4 - Otros")
                        while True:
                            a = int(input("Ingrese el colegio en el que estudio: "))
                            if a == 1:
                                matricula = 300
                                precio = 1700
                                descuento = precio*0.5
                                total = descuento + matricula
                                print("*****Aqui esta su boleta de matricula******")
                                print("Carrera: Administración para los negocios, pagaras en su primera cuota:", total, "luego pagará cada una de las demás cuotas:",descuento)
                                print("Si desea continuar con el proceso, venga a nuestros establecimiento, gracias.")
                                break
                            if a == 2:
                                matricula = 300
                                precio = 2400
                                descuento = precio*0.5
                                total = descuento + matricula
                                print("*****Aqui esta su boleta de matricula******")
                                print("Carrera: Administración para los negocios, pagaras en su primera cuota:", total, "luego pagará cada una de las demás cuotas:",descuento)
                                print("Si desea continuar con el proceso, venga a nuestros establecimiento, gracias.")
                                break
                            if a == 3:
                                matricula = 300
                                precio = 1200
                                descuento = precio*0.5
                                total = descuento + matricula
                                print("*****Aqui esta su boleta de matricula******")
                                print("Carrera: Administración para los negocios, pagaras en su primera cuota:", total, "luego pagará cada una de las demás cuotas:",descuento)
                                print("Si desea continuar con el proceso, venga a nuestros establecimiento, gracias.")
                                break
                            if a == 4:
                                matricula = 300
                                precio = 1500
                                descuento = precio*0.5
                                total = descuento + matricula
                                print("*****Aqui esta su boleta de matricula******")
                                print("Carrera: Administración para los negocios, pagaras en su primera cuota:", total, "luego pagará cada una de las demás cuotas:",descuento)
                                print("Si desea continuar con el proceso, venga a nuestros establecimiento, gracias.")
                                break
                            else:
                                print("Opciones inexistente, seleccionar una opcion nuevamente")

                    # Si selecciona la carrera de ARQUI
                    if x == 3:
                        print("Usted a elegido la carrera de Arquitectura")
                        print("Usted a elegido la carrera de Ingeniería informática y de sistemas")
                        print("1 - Innova School / Tricel / Pamer / Saco Oliveros"
                        "\n2 - Markham / Raimondi / Franklin Delano Roosevelt "
                        "\n3 - Mariano Melgar / Augusto Salazar Bondy"
                        "\n4 - Otros")
                        while True:
                            a = int(input("Ingrese el colegio en el que estudio: "))
                            if a == 1:
                                matricula = 300
                                precio = 1550
                                descuento = precio*0.5
                                total = descuento + matricula
                                print("*****Aqui esta su boleta de matricula******")
                                print("Carrera: Arquitectura, pagaras en su primera cuota:", total, "luego pagará cada una de las demás cuotas:",descuento)
                                print("Si desea continuar con el proceso, venga a nuestros establecimiento, gracias.")
                                break
                            if a == 2:
                                matricula = 300
                                precio = 2350
                                descuento = precio*0.5
                                total = descuento + matricula
                                print("*****Aqui esta su boleta de matricula******")
                                print("Carrera: Arquitectura, pagaras en su primera cuota:", total, "luego pagará cada una de las demás cuotas:",descuento)
                                print("Si desea continuar con el proceso, venga a nuestros establecimiento, gracias.")
                                break
                            if a == 3:
                                matricula = 300
                                precio = 1100
                                descuento = precio*0.5
                                total = descuento + matricula
                                print("*****Aqui esta su boleta de matricula******")
                                print("Carrera: Arquitectura, pagaras en su primera cuota:", total, "luego pagará cada una de las demás cuotas:",descuento)
                                print("Si desea continuar con el proceso, venga a nuestros establecimiento, gracias.")
                                break
                            if a == 4:
                                matricula = 300
                                precio = 1400
                                descuento = precio*0.5
                                total = descuento + matricula
                                print("*****Aqui esta su boleta de matricula******")
                                print("Carrera: Arquitectura, pagaras en su primera cuota:", total, "luego pagará cada una de las demás cuotas:",descuento)
                                print("Si desea continuar con el proceso, venga a nuestros establecimiento, gracias.")
                                break
                            else:
                                print("Opciones inexistente, seleccionar una opcion nuevamente")

                #YA ESTA LISTO NO TOCAR TERCIO SUPERIOR
                elif 15 <=promedio < 17:
                    print("Felicitaciones estás apto para acceder a la Beca tercio superior")
                    print("Por favor ingresa la carrera a la que vas a postular")
                    print("1 - Ingeniería informátiva y de sistemas")
                    print("2 - Administración para los negocios")
                    print("3 - Arquitectura")
                    x = int(input("Ingrese la carrera a la que va postular: "))
                    # Si selecciona la carrera de ING YA ESTA
                    if x == 1:
                        print("Usted a elegido la carrera de Ingeniería informática y de sistemas")
                        print("1 - Innova School / Tricel / Pamer / Saco Oliveros"
                        "\n2 - Markham / Raimondi / Franklin Delano Roosevelt "
                        "\n3 - Mariano Melgar / Augusto Salazar Bondy"
                        "\n4 - Otros")
                        while True:
                            a = int(input("Ingrese el colegio en el que estudio: "))
                            if a == 1:
                                matricula = 300
                                precio = 1600
                                descuento = precio*0.7
                                total = descuento + matricula
                                print("*****Aqui esta su boleta de matricula******")
                                print("Carrera: Ing de Sistemas, pagaras en su primera cuota:", total, "luego pagará cada una de las demás cuotas:",descuento)
                                print("Si desea continuar con el proceso, venga a nuestros establecimiento, gracias.")
                                break
                            if a == 2:
                                matricula = 300
                                precio = 2300
                                descuento = precio*0.7
                                total = descuento + matricula
                                print("*****Aqui esta su boleta de matricula******")
                                print("Carrera: Ing de Sistemas, pagaras en su primera cuota:", total, "luego pagará cada una de las demás cuotas:",descuento)
                                print("Si desea continuar con el proceso, venga a nuestros establecimiento, gracias.")
                                break
                            if a == 3:
                                matricula = 300
                                precio = 1000
                                descuento = precio*0.7
                                total = descuento + matricula
                                print("*****Aqui esta su boleta de matricula******")
                                print("Carrera: Ing de Sistemas, pagaras en su primera cuota:", total, "luego pagará cada una de las demás cuotas:",descuento)
                                print("Si desea continuar con el proceso, venga a nuestros establecimiento, gracias.")
                                break
                            if a == 4:
                                matricula = 300
                                precio = 1300
                                descuento = precio*0.7
                                total = descuento + matricula
                                print("*****Aqui esta su boleta de matricula******")
                                print("Carrera: Ing de Sistemas, pagaras en su primera cuota:", total, "luego pagará cada una de las demás cuotas:",descuento)
                                print("Si desea continuar con el proceso, venga a nuestros establecimiento, gracias.")
                                break
                            else:
                                print("Opciones inexistente, seleccionar una opcion nuevamente")

                            

                    # Si selecciona la cararera de ADMI
                    if x == 2:
                        print("Usted a elegido la carrera de Administración para los negocios")
                        print("1 - Innova School / Tricel / Pamer / Saco Oliveros"
                        "\n2 - Markham / Raimondi / Franklin Delano Roosevelt "
                        "\n3 - Mariano Melgar / Augusto Salazar Bondy"
                        "\n4 - Otros")
                        while True:
                            a = int(input("Ingrese el colegio en el que estudio: "))
                            if a == 1:
                                matricula = 300
                                precio = 1700
                                descuento = precio*0.7
                                total = precio*0.7 + matricula
                                print("*****Aqui esta su boleta de matricula******")
                                print("Carrera: Administración para los negocios, pagaras en su primera cuota:", total, "luego pagará cada una de las demás cuotas:",descuento)
                                print("Si desea continuar con el proceso, venga a nuestros establecimiento, gracias.")
                                break
                            if a == 2:
                                matricula = 300
                                precio = 2400
                                descuento = precio*0.7
                                total = precio*0.7 + matricula
                                print("*****Aqui esta su boleta de matricula******")
                                print("Carrera: Administración para los negocios, pagaras en su primera cuota:", total, "luego pagará cada una de las demás cuotas:",descuento)
                                print("Si desea continuar con el proceso, venga a nuestros establecimiento, gracias.")
                                break
                            if a == 3:
                                matricula = 300
                                precio = 1200
                                descuento = precio*0.7
                                total = precio*0.7 + matricula
                                print("*****Aqui esta su boleta de matricula******")
                                print("Carrera: Administración para los negocios, pagaras en su primera cuota:", total, "luego pagará cada una de las demás cuotas:",descuento)
                                print("Si desea continuar con el proceso, venga a nuestros establecimiento, gracias.")
                                break
                            if a == 4:
                                matricula = 300
                                precio = 1500
                                descuento = precio*0.7
                                total = descuento + matricula
                                print("*****Aqui esta su boleta de matricula******")
                                print("Carrera: Administración para los negocios, pagaras en su primera cuota:", total, "luego pagará cada una de las demás cuotas:",descuento)
                                print("Si desea continuar con el proceso, venga a nuestros establecimiento, gracias.")
                                break
                            else:
                                print("Opciones inexistente, seleccionar una opcion nuevamente")

                    # Si selecciona la carrera de ARQUI
                    if x == 3:
                        print("Usted a elegido la carrera de Arquitectura")
                        print("1 - Innova School / Tricel / Pamer / Saco Oliveros"
                        "\n2 - Markham / Raimondi / Franklin Delano Roosevelt "
                        "\n3 - Mariano Melgar / Augusto Salazar Bondy"
                        "\n4 - Otros")
                        while True:
                            a = int(input("Ingrese el colegio en el que estudio: "))
                            if a == 1:
                                matricula = 300
                                precio = 1550
                                descuento = precio*0.7 
                                total = descuento + matricula
                                print("*****Aqui esta su boleta de matricula******")
                                print("Carrera: Arquitectura, pagaras en su primera cuota:", total, "luego pagará cada una de las demás cuotas:",descuento)
                                print("Si desea continuar con el proceso, venga a nuestros establecimiento, gracias.")
                            if a == 2:
                                matricula = 300
                                precio = 2350
                                descuento = precio*0.7 
                                total = descuento + matricula
                                print("*****Aqui esta su boleta de matricula******")
                                print("Carrera: Arquitectura, pagaras en su primera cuota:", total, "luego pagará cada una de las demás cuotas:",descuento)
                                print("Si desea continuar con el proceso, venga a nuestros establecimiento, gracias.")
                                break
                            if a == 3:
                                matricula = 300
                                precio = 1100
                                descuento = precio*0.7 
                                total = descuento + matricula
                                print("*****Aqui esta su boleta de matricula******")
                                print("Carrera: Arquitectura, pagaras en su primera cuota:", total, "luego pagará cada una de las demás cuotas:",descuento)
                                print("Si desea continuar con el proceso, venga a nuestros establecimiento, gracias.")
                                break
                            if a == 4:
                                matricula = 300
                                precio = 1400
                                descuento = precio*0.7 
                                total = descuento + matricula
                                print("*****Aqui esta su boleta de matricula******")
                                print("Carrera: Arquitectura, pagaras en su primera cuota:", total, "luego pagará cada una de las demás cuotas:",descuento)
                                print("Si desea continuar con el proceso, venga a nuestros establecimiento, gracias.")
                                break
                            else:
                                print("Opciones inexistente, seleccionar una opcion nuevamente")
                    
                else:
                    print("no perteneces a ninguno de los rangos para accedeer a una beca.")
                    print("Seleccione una de las opciones del menu de Postulante nuevamente")
                    print ("\t1 - Excelencia Académica")
                    print ("\t2 - Beca 18")
                    print ("\t3 - Admisión normal")
                    print ("\t4 - regresar") 

            # BECA 18
            if modalidad == 2:
                print("Bienvenido estás en la modalidad Beca 18")
                print("Por favor ingresa ingresa la carrera a la que vas a postular")
                print("1 - Ingeniería informátiva y de sistemas")
                print("2 - Administración para los negocios")
                print("3 - Arquitectura")
                x = int(input("Ingrese la carrera a la que va postular: "))
                if x == 1:
                    a = 1900
                    print("usted a elegido la carrera de Ingeniería informática y de sistemas")
                    print("*****Aqui esta su boleta de matricula******")
                    print("Como usted pertenece a beca 18, entonces se cubrirá las siguiente cantidad de gastos ", a)
                    print("Si desea continuar con el proceso, venga a nuestros establecimiento, gracias.")          
                if x == 2:
                    print("Usted a elegido la carrera de Administración para los negocios")
                    a = 2000
                    print("*****Aqui esta su boleta de matricula******")
                    print("Como usted pertenece a beca 18, entonces se cubrirá las siguiente cantidad de gastos ", a)
                    print("Si desea continuar con el proceso, venga a nuestros establecimiento, gracias.")
                    

                if x == 3:
                    print("Usted a elegido la carrera de Arquitectura")
                    a = 1850
                    print("*****Aqui esta su boleta de matricula******")
                    print("Como usted pertenece a beca 18, entonces se cubrirá las siguiente cantidad de gastos ", a)
                    print("Si desea continuar con el proceso, venga a nuestros establecimiento, gracias.")
                
            # ADMISION NORMAL
            if modalidad == 3:
                print ("Bienvenido estás en la modalidad admisón normal")
                print("Por favor ingresa ingresa la carrera a la que vas a postular")
                print("1 - Ingeniería informátiva y de sistemas")
                print("2 - Administración para los negocios")
                print("3 - Arquitectura")
                x = int(input("Ingrese la carrera a la que va postular: "))
                if x == 1:
                    print("Usted a elegido la carrera de Ingeniería informática y de sistemas")
                    print("1 - Innova School / Tricel / Pamer / Saco Oliveros"
                    "\n2 - Markham / Raimondi / Franklin Delano Roosevelt "
                    "\n3 - Mariano Melgar / Augusto Salazar Bondy"
                    "\n4 - Otros")
                    while True:
                        a = int(input("Ingrese el colegio en el que estudio: "))
                        if a == 1:
                            matricula = 300
                            precio = 1600
                            total = precio+ matricula
                            print("*****Aqui esta su boleta de matricula******")
                            print("Carrera: Ing de Sistemas, pagaras en su primera cuota:", total, "luego pagará cada una de las demás cuotas:", precio)
                            print("Si desea continuar con el proceso, venga a nuestros establecimiento, gracias.")
                            break
                        if a == 2:
                            matricula = 300
                            precio = 2300
                            total = precio+ matricula
                            print("*****Aqui esta su boleta de matricula******")
                            print("Carrera: Ing de Sistemas, pagaras en su primera cuota:", total, "luego pagará cada una de las demás cuotas:", precio)
                            print("Si desea continuar con el proceso, venga a nuestros establecimiento, gracias.")
                            break
                        if a == 3:
                            matricula = 300
                            precio = 1000
                            total = precio+ matricula
                            print("*****Aqui esta su boleta de matricula******")
                            print("Carrera: Ing de Sistemas, pagaras en su primera cuota:", total, "luego pagará cada una de las demás cuotas:", precio)
                            print("Si desea continuar con el proceso, venga a nuestros establecimiento, gracias.")
                            break
                        if a == 4:
                            matricula = 300
                            precio = 1300
                            total = precio+ matricula
                            print("*****Aqui esta su boleta de matricula******")
                            print("Carrera: Ing de Sistemas, pagaras en su primera cuota:", total, "luego pagará cada una de las demás cuotas:", precio)
                            print("Si desea continuar con el proceso, venga a nuestros establecimiento, gracias.")
                            break
                        else:
                            print("Opciones inexistente, seleccionar una opcion nuevamente")
                            

                if x == 2:
                    print("Usted a elegido la carrera de Administración para los negocios")
                    print("1 - Innova School / Tricel / Pamer / Saco Oliveros"
                    "\n2 - Markham / Raimondi / Franklin Delano Roosevelt "
                    "\n3 - Mariano Melgar / Augusto Salazar Bondy"
                    "\n4 - Otros")
                    while True:
                        a = int(input("Ingrese el colegio en el que estudio: "))
                        if a == 1:
                            matricula = 300
                            precio = 1700
                            total = precio + matricula
                            print("*****Aqui esta su boleta de matricula******")
                            print("Carrera: Administración para los negocios, pagaras en su primera cuota:", total, "luego pagará cada una de las demás cuotas:", precio)
                            print("Si desea continuar con el proceso, venga a nuestros establecimiento, gracias.")
                            break
                        if a == 2:
                            matricula = 300
                            precio = 2400
                            total = precio + matricula
                            print("*****Aqui esta su boleta de matricula******")
                            print("Carrera: Administración para los negocios, pagaras en su primera cuota:", total, "luego pagará cada una de las demás cuotas:", precio)
                            print("Si desea continuar con el proceso, venga a nuestros establecimiento, gracias.")
                            break
                        if a == 3:
                            matricula = 300
                            precio = 1200
                            total = precio+ matricula
                            print("*****Aqui esta su boleta de matricula******")
                            print("Carrera: Administración para los negocios, pagaras en su primera cuota:", total, "luego pagará cada una de las demás cuotas:", precio)
                            print("Si desea continuar con el proceso, venga a nuestros establecimiento, gracias.")
                            break
                        if a == 4:
                            matricula = 300
                            precio = 1500
                            total = precio+ matricula
                            print("*****Aqui esta su boleta de matricula******")
                            print("Carrera: Administración para los negocios, pagaras en su primera cuota:", total, "luego pagará cada una de las demás cuotas:", precio)
                            print("Si desea continuar con el proceso, venga a nuestros establecimiento, gracias.")
                            break
                        else:
                            print("Opciones inexistente, seleccionar una opcion nuevamente")
                if x == 3:
                    print("Usted a elegido la carrera de Arquitectura")
                    print("1 - Innova School / Tricel / Pamer / Saco Oliveros"
                    "\n2 - Markham / Raimondi / Franklin Delano Roosevelt "
                    "\n3 - Mariano Melgar / Augusto Salazar Bondy"
                    "\n4 - Otros")
                    while True:
                        a = int(input("Ingrese el colegio en el que estudio: "))
                        if a == 1:
                            matricula = 300
                            precio = 1550
                            total = precio+ matricula
                            print("*****Aqui esta su boleta de matricula******")
                            print("Carrera: Arquitectura, pagaras en su primera cuota:", total, "luego pagará cada una de las demás cuotas:", precio)
                            print("Si desea continuar con el proceso, venga a nuestros establecimiento, gracias.")
                            break
                        if a == 2:
                            matricula = 300
                            precio = 2350
                            total = precio+ matricula
                            print("*****Aqui esta su boleta de matricula******")
                            print("Carrera: Arquitectura, pagaras en su primera cuota:", total, "luego pagará cada una de las demás cuotas:", precio)
                            print("Si desea continuar con el proceso, venga a nuestros establecimiento, gracias.")
                            break
                        if a == 3:
                            matricula = 300
                            precio = 1100
                            total = precio + matricula
                            print("*****Aqui esta su boleta de matricula******")
                            print("Carrera: Arquitectura, pagaras en su primera cuota:", total, "luego pagará cada una de las demás cuotas:", precio)
                            print("Si desea continuar con el proceso, venga a nuestros establecimiento, gracias.")
                            break
                        if a == 4:
                            matricula = 300
                            precio = 1400
                            total = precio + matricula
                            print("*****Aqui esta su boleta de matricula******")
                            print("Carrera: Arquitectura, pagaras en su primera cuota:", total, "luego pagará cada una de las demás cuotas:", precio)
                            print("Si desea continuar con el proceso, venga a nuestros establecimiento, gracias.")
                            break
                        else:
                            print("Opciones inexistente, seleccionar una opcion nuevamente")
                break
            
            if modalidad == 4:
                print("Ha regresado exitosamente")
                break
            