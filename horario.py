import os
os.system("cls")
#a=[]
#h=[[1,1000],[2,221]]
#a.append(h[0])
#print(a)

#calculo2, fisica2, inferencia estadistica, taller 2, economia, ingles 6

 #                   print("En Calculo I lo has pasado con 15, pasaste a la 1era " )
            #        print("En Fisica I lo has pasado con 14, pasaste a la 1era ")
           #         print("En Poo lo has pasado con 17, pasaste a la 1era")
          #          print("En Taller lo has pasado con 18, pasaste a la 1era")
         #           print("En Marketing lo has pasado con 14, pasaste a la 1era")
        #            print("En Intro lo has pasado con 17, pasaste a la 1era")
       #             print("Esta disponible a llevar los cursos siguientes")



      #              print("En Calculo I no lo has pasado, nota 10, lo llevaras por 2da vez " )
     #               print("En Estadistica lo has pasado con 14, pasaste a la 1era ")
    #                print("En Poo lo has pasado con 17, pasaste a la 1era")
   #                 print("En Taller lo has pasado con 13, pasaste a la 1era")
  #                  print("En ADD lo has pasado con 14, pasaste a la 1era")
 #                   print("En Fisica general lo has pasado con 17, pasaste a la 1era")
#                  print("Esta disponible a llevar los cursos siguientes pero no de Calculo II")

from funciones import volvercalculo2,volvereconomia,volverestadistica,volverfisica,volveringles6,volvertaller2
from funciones import profcalculodavid,profeecodavid,profeestadavid,profefisicadavid,profeingles6,profets2david, profcalculomari, volvercalculoI

cursos=["c1","f1","poo","t","m","intro"]
cursos2020=["Calculo 2","Fisica 2","Estadistica", "Taller 2", "Economia", "Ingles 6"]
diasSemana=["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado"]


while True:
    opcionalum = int(input("Seleccione una opcion del menu usilio: "))
    if opcionalum ==2:
        notas=[]
        notas.append(15.0)
        notas.append(14.0)
        notas.append(17.0)
        notas.append(18.0)
        notas.append(14.0)
        notas.append(17.0)
    
        for i in range(6):
            print("Puedes llevar los siguientes cursos "+cursos2020[i])
        continuar = input("Desea ir a la eleccion de horarios? S/N: ").lower()
        if continuar != "s":
            print("Espere un momento, regresará al menú principal")
            break
        else:
            profcalculodavid()
            credical = 4
            while True:
                a=int(input("Escoja el profesor con el que desea llevar el curso:"))
                hCalculo2=[]
                hReyes=[[1,28800],[2,36000],[4,36000]]
                hFernandez=[[1,28800],[3,36000],[5,28800]]
                if a==1:
                    for i in range(3):
                        hCalculo2.append(hReyes[i])
                    break
                elif a == 2:
                    for i in range(3):
                        hCalculo2.append(hFernandez[i])
                    break
                else:
                    volvercalculo2()

                
        
            profefisicadavid()
            credifi = 3
            while True:
                b=int(input("Escoja el profesor con el que desea llevar el curso:"))
                hFisica2=[]
                hGarcía=[[1,36000],[2,46800],[4,46800]]
                hGuanira=[[1,46800],[2,28800],[5,46800]]
                if b == 1:
                    while True:
                        for i in range(3):
                            if hGarcía[i]!=hCalculo2[i]:
                                hFisica2.append(hGarcía[i])
                            else:
                                print("Se ha detectado un cruce de horarios. Por favor, escoja otro horario")
                        break
                    break
                
                elif b == 2:
                    while True:
                        for i in range(3):
                            if hGuanira[i]!=hCalculo2[i]:
                                hFisica2.append(hGuanira[i])
                            else:
                                print("Se ha detectado un cruce de horarios. Por favor, escoja otro horario")
                        break
                    break
                else:
                    volverfisica()
            
            profeestadavid()
            crediesta = 3
            while True:    
                hEstadistica=[]
                hMontesino=[[3,28800],[4,28800],[5,36000]]
                hRivas=[[1,28800],[2,46800],[5,46800]]
                c=int(input("Escoja el profesor con el que desea llevar el curso:"))
                if c==1:
                    while True:
                        for i in range(3):
                            if hMontesino[i] != hFisica2[i]:
                                hEstadistica.append(hMontesino[i])
                            else:
                                print("Se ha detectado un cruce de horarios. Por favor, escoja otro horario")
                                volverestadistica()
                        break
                    break
                # Rivas aca tiene cruce
                elif c == 2:
                    while True:
                        for i in range(3):
                            if hRivas[0]!=hCalculo2[0] and hRivas[1]!=hFisica2[1] and hRivas[0]!=hFernandez[0] and hRivas[2]!=hGuanira[2]:
                                hEstadistica.append(hRivas[i])
                            else:
                                print("*************ALERTA************")
                                print("Se ha detectado un cruce de horarios. Por favor, escoja otro horario")
                                volverestadistica()
                            break
                        break
                        
                else:
                    volverestadistica()

            profets2david()
            credits2 = 3
            while True:

                d=int(input("Escoja el profesor con el que desea llevar el curso:"))
                hTaller2=[]
                hCordova=[[3,46800],[5,54000],[6,28800]]
                hRamirez=[[4,54000],[1,68400],[6,36000]]
                if d==1:
                    while True:
                        for i in range(3):
                            if hCordova[i]!=hCalculo2[i] or hCordova[i]!=hFisica2[i] or hCordova[i]!=hEstadistica[i]:
                                hTaller2.append(hCordova[i])
                            else:
                                print("Se ha detectado un cruce de horarios. Por favor, escoja otro horario")
                                volvertaller2()
                        break
                    break
                elif d == 2:
                    while True:
                        for i in range(3):
                            if  hRamirez[i]!=hCalculo2[i] and hRamirez[i]!=hFisica2[i] and hRamirez[i]!=hEstadistica[i]:
                                hTaller2.append(hRamirez[i])
                            else:
                                print("Se ha detectado un cruce de horarios. Por favor, escoja otro horario")
                                volvertaller2()
                        break
                    break
                else:
                    volvertaller2()
                

            profeecodavid()
            credieco = 3
            while True:
                e=int(input("Escoja el profesor con el que desea llevar el curso:"))
                hEconomia=[]
                hTamariz=[[2,54000],[5,61200],[6,54000]]
                hPaz=[[3,54000],[4,68400],[6,46800]]
                if e==1:
                    while True:
                        for i in range(3):
                            if hTamariz[i]!=hCalculo2[i] and hTamariz[i]!=hFisica2[i] and hTamariz[i]!=hEstadistica[i] and hTamariz[i]!=hTaller2[i] :
                                hEconomia.append(hTamariz[i])
                            else:
                                print("Se ha detectado un cruce de horarios. Por favor, escoja otro horario")
                        break
                    break
                elif e == 2:
                    while True:
                        for i in range(3):
                            if hPaz[i]!=hCalculo2[i] and hPaz[i]!=hEstadistica[i] and hPaz[i]!=hFisica2[i] and hPaz[i]!=hTaller2:
                                hEconomia.append(hPaz[i])
                            else:
                                print("Se ha detectado un cruce de horarios. Por favor, escoja otro horario")
                        break
                    break
                else:
                    volvereconomia()

            profeingles6()
            crediingles = 3
            while True:
                f=int(input("Escoja el profesor con el que desea llevar el curso:"))
                hIngles=[]
                hMuller=[[1,54000],[2,68400],[5,68400]]
                hDuran=[[3,68400],[5,68400],[6,68400]]
                if f==1:
                    while True:
                        for i in range(3):
                            if hMuller[i]!=hCalculo2[i] and hMuller[i]!=hFisica2[i] and hMuller[i]!=hEstadistica[i] and hMuller[i]!=hTaller2[i] or hMuller[i]==hEconomia[i]:
                                hIngles.append(hMuller[i])
                            else:
                                print("Se ha detectado un cruce de horarios. Por favor, escoja otro horario")
                        break
                    break
                elif f==2:
                    while True:
                        for i in range(3):
                            if  hDuran[i]!=hCalculo2[i] and hDuran[i]!=hFisica2[i] and hDuran[i]!=hEstadistica[i] and hDuran[i]!=hTaller2[i] or hDuran[i]==hEconomia[i]:
                                hIngles.append(hDuran[i])
                            else:
                                print("Se ha detectado un cruce de horarios. Por favor, escoja otro horario")
                        break
                    break
                else:
                    volveringles6()

            diasCalculo=[]  ## Arreglo donde se guarda las primeras componentes del contenido del arreglo hCalculo2
            dCalculo=[] ## Arreglo donde se guarda a que día corresponde cada componente del arreglo diasCalculo
            horarioCalculo=[] ## Arreglo donde se guarda las segundas componentes del contenido del arreglo hCalculo2
            tiempoInicialCalculo=[] ## Arreglo donde se guarda la hora inicial de la clase
            tiempoFinCalculo=[] ## Arreglo donde se guarda la hora final de la clase
            
            
            for i in range(3):
                diasCalculo.append(hCalculo2[i][0])
            
            for i in range(3):
                if diasCalculo[i]==1:
                    dCalculo.append('Lunes')
                if diasCalculo[i]==2:
                    dCalculo.append('Martes')
                if diasCalculo[i]==3:
                    dCalculo.append('Miércoles')
                if diasCalculo[i]==4:
                    dCalculo.append('Jueves')
                if diasCalculo[i]==5:
                    dCalculo.append('Viernes')
                if diasCalculo[i]==6:
                    dCalculo.append('Sábado')
            for i in range(3):
                horarioCalculo.append(hCalculo2[i][1])
            for i in range(3):
                tiempoInicialCalculo.append(horarioCalculo[i]//3600)
                tiempoFinCalculo.append((horarioCalculo[i]//3600)+2)


            print("Usted tiene Cálculo 2, los siguientes días:")
            for i in range(3):
                print(dCalculo[i],"de",tiempoInicialCalculo[i],"a",tiempoFinCalculo[i],"horas")


            diasFisica=[]  ## Arreglo donde se guarda las primeras componentes del contenido del arreglo hFisica2
            dFisica=[] ## Arreglo donde se guarda a que día corresponde cada componente del arreglo diasFisica
            horarioFisica=[] ## Arreglo donde se guarda las segundas componentes del contenido del arreglo hFisica2
            tiempoInicialFisica=[] ## Arreglo donde se guarda la hora inicial de la clase
            tiempoFinFisica=[] ## Arreglo donde se guarda la hora final de la clase
            
            
            for i in range(3):
                diasFisica.append(hFisica2[i][0])
            
            for i in range(3):
                if diasFisica[i]==1:
                    dFisica.append('Lunes')
                if diasFisica[i]==2:
                    dFisica.append('Martes')
                if diasFisica[i]==3:
                    dFisica.append('Miércoles')
                if diasFisica[i]==4:
                    dFisica.append('Jueves')
                if diasFisica[i]==5:
                    dFisica.append('Viernes')
                if diasFisica[i]==6:
                    dFisica.append('Sábado')
            for i in range(3):
                horarioFisica.append(hFisica2[i][1])
            for i in range(3):
                tiempoInicialFisica.append(horarioFisica[i]//3600)
                tiempoFinFisica.append((horarioFisica[i]//3600)+2)


            print("Usted tiene Física 2, los siguientes días:")
            for i in range(3):
                print(dFisica[i],"de",tiempoInicialFisica[i],"a",tiempoFinFisica[i],"horas")


            diasEstadistica=[]  ## Arreglo donde se guarda las primeras componentes del contenido del arreglo hEstadistica
            dEstadistica=[] ## Arreglo donde se guarda a que día corresponde cada componente del arreglo diasEstadistica
            horarioEstadistica=[] ## Arreglo donde se guarda las segundas componentes del contenido del arreglo hEstadistica
            tiempoInicialEstadistica=[] ## Arreglo donde se guarda la hora inicial de la clase
            tiempoFinEstadistica=[] ## Arreglo donde se guarda la hora final de la clase
            
            
            for i in range(3):
                diasEstadistica.append(hEstadistica[i][0])
            
            for i in range(3):
                if diasEstadistica[i]==1:
                    dEstadistica.append('Lunes')
                if diasEstadistica[i]==2:
                    dEstadistica.append('Martes')
                if diasEstadistica[i]==3:
                    dEstadistica.append('Miércoles')
                if diasEstadistica[i]==4:
                    dEstadistica.append('Jueves')
                if diasEstadistica[i]==5:
                    dEstadistica.append('Viernes')
                if diasEstadistica[i]==6:
                    dEstadistica.append('Sábado')
            for i in range(3):
                horarioEstadistica.append(hEstadistica[i][1])
            for i in range(3):
                tiempoInicialEstadistica.append(horarioEstadistica[i]//3600)
                tiempoFinEstadistica.append((horarioEstadistica[i]//3600)+2)


            print("Usted tiene Estadística, los siguientes días:")
            for i in range(3):
                print(dEstadistica[i],"de",tiempoInicialEstadistica[i],"a",tiempoFinEstadistica[i],"horas")
            


            diasTaller=[]  ## Arreglo donde se guarda las primeras componentes del contenido del arreglo hTaller2
            dTaller=[] ## Arreglo donde se guarda a que día corresponde cada componente del arreglo diasTaller
            horarioTaller=[] ## Arreglo donde se guarda las segundas componentes del contenido del arreglo hTaller2
            tiempoInicialTaller=[] ## Arreglo donde se guarda la hora inicial de la clase
            tiempoFinTaller=[] ## Arreglo donde se guarda la hora final de la clase
            
            
            for i in range(3):
                diasTaller.append(hTaller2[i][0])
            
            for i in range(3):
                if diasTaller[i]==1:
                    dTaller.append('Lunes')
                if diasTaller[i]==2:
                    dTaller.append('Martes')
                if diasTaller[i]==3:
                    dTaller.append('Miércoles')
                if diasTaller[i]==4:
                    dTaller.append('Jueves')
                if diasTaller[i]==5:
                    dTaller.append('Viernes')
                if diasTaller[i]==6:
                    dTaller.append('Sábado')
            for i in range(3):
                horarioTaller.append(hTaller2[i][1])
            for i in range(3):
                tiempoInicialTaller.append(horarioTaller[i]//3600)
                tiempoFinTaller.append((horarioTaller[i]//3600)+2)


            print("Usted tiene Taller 2, los siguientes días:")
            for i in range(3):
                print(dTaller[i],"de",tiempoInicialTaller[i],"a",tiempoFinTaller[i],"horas")


            diasEconomia=[]  ## Arreglo donde se guarda las primeras componentes del contenido del arreglo hEconomia
            dEconomia=[] ## Arreglo donde se guarda a que día corresponde cada componente del arreglo diasEconomia
            horarioEconomia=[] ## Arreglo donde se guarda las segundas componentes del contenido del arreglo hEconomia
            tiempoInicialEconomia=[] ## Arreglo donde se guarda la hora inicial de la clase
            tiempoFinEconomia=[] ## Arreglo donde se guarda la hora final de la clase
            
            
            for i in range(3):
                diasEconomia.append(hEconomia[i][0])
            
            for i in range(3):
                if diasEconomia[i]==1:
                    dEconomia.append('Lunes')
                if diasEconomia[i]==2:
                    dEconomia.append('Martes')
                if diasEconomia[i]==3:
                    dEconomia.append('Miércoles')
                if diasEconomia[i]==4:
                    dEconomia.append('Jueves')
                if diasEconomia[i]==5:
                    dEconomia.append('Viernes')
                if diasEconomia[i]==6:
                    dEconomia.append('Sábado')
            for i in range(3):
                horarioEconomia.append(hEconomia[i][1])
            for i in range(3):
                tiempoInicialEconomia.append(horarioEconomia[i]//3600)
                tiempoFinEconomia.append((horarioEconomia[i]//3600)+2)


            print("Usted tiene Economía, los siguientes días:")
            for i in range(3):
                print(dEconomia[i],"de",tiempoInicialEconomia[i],"a",tiempoFinEconomia[i],"horas")


            diasIngles=[]  ## Arreglo donde se guarda las primeras componentes del contenido del arreglo hIngles
            dIngles=[] ## Arreglo donde se guarda a que día corresponde cada componente del arreglo diasIngles
            horarioIngles=[] ## Arreglo donde se guarda las segundas componentes del contenido del arreglo hIngles
            tiempoInicialIngles=[] ## Arreglo donde se guarda la hora inicial de la clase
            tiempoFinIngles=[] ## Arreglo donde se guarda la hora final de la clase
            
            
            for i in range(3):
                diasIngles.append(hIngles[i][0])
            
            for i in range(3):
                if diasIngles[i]==1:
                    dIngles.append('Lunes')
                if diasIngles[i]==2:
                    dIngles.append('Martes')
                if diasIngles[i]==3:
                    dIngles.append('Miércoles')
                if diasIngles[i]==4:
                    dIngles.append('Jueves')
                if diasIngles[i]==5:
                    dIngles.append('Viernes')
                if diasIngles[i]==6:
                    dIngles.append('Sábado')
            for i in range(3):
                horarioIngles.append(hIngles[i][1])
            for i in range(3):
                tiempoInicialIngles.append(horarioIngles[i]//3600)
                tiempoFinIngles.append((horarioIngles[i]//3600)+2)


            print("Usted tiene Inglés 6, los siguientes días:")
            for i in range(3):
                print(dIngles[i],"de",tiempoInicialIngles[i],"a",tiempoFinIngles[i],"horas")
            sumacreditos = credical+credieco+crediesta+credifi+crediingles+credits2
            print("Creditos totales: ", sumacreditos)
        break       

        
            
    elif opcionalum == 3:
        notas1=[]
        notas1.append(10.0)
        notas1.append(14.0)
        notas1.append(17.0)
        notas1.append(13.0)
        notas1.append(14.0)
        notas1.append(17.0)
        i=0
        while (i<6):
            if notas1[0] >= 10.5:
                cursos = print("Puedes llevar los siguientes cursos "+cursos2020[0])
            else:
                nopuedes = print("No puedes llevar el siguiente curso " + cursos2020[0])
            if notas1[1] >= 10.5:
                cursos = print("Puedes llevar los siguientes cursos "+cursos2020[1])
            if notas1[2] >= 10.5:
                cursos = print("Puedes llevar los siguientes cursos "+cursos2020[2])
            if notas1[3] >= 10.5:
                cursos = print("Puedes llevar los siguientes cursos "+cursos2020[3])
            if notas1[4] >= 10.5:
                cursos = print("Puedes llevar los siguientes cursos "+cursos2020[4])
            if notas1[5] >= 10.5:
                cursos = print("Puedes llevar los siguientes cursos "+cursos2020[5])
            break
        
        continuar = input("Desea ir a la eleccion de horarios? S/N: ").lower()
        if continuar != "s":
            print("Espere un momento, regresará al menú principal")
        else:
            pregunta = input("Antes de empezar, va desea llevar el curso de calculo I este ciclo? S/N: ").lower()
            if pregunta == "s":
                profcalculomari()
                credical = 4
                while True:
                    a=int(input("Escoja el profesor con el que desea llevar el curso:"))
                    hCalculo1=[]
                    hBravo=[[1,28800],[2,36000],[4,36000]]
                    hLenin=[[1,28800],[3,36000],[5,28800]]
                    if a==1:
                        for i in range(3):
                            hCalculo1.append(hBravo[i])
                        break
                    elif a == 2:
                        for i in range(3):
                            hCalculo1.append(hLenin[i])
                        break
                    else:
                        volvercalculoI()

                    
            
                profefisicadavid()
                credifi = 3
                while True:
                    b=int(input("Escoja el profesor con el que desea llevar el curso:"))
                    hFisica2=[]
                    hGarcía=[[1,36000],[2,46800],[4,46800]]
                    hGuanira=[[1,46800],[2,28800],[5,46800]]
                    if b == 1:
                        while True:
                            for i in range(3):
                                if hGarcía[i]!=hCalculo1[i]:
                                    hFisica2.append(hGarcía[i])
                                else:
                                    print("Se ha detectado un cruce de horarios. Por favor, escoja otro horario")
                            break
                        break
                    
                    elif b == 2:
                        while True:
                            for i in range(3):
                                if hGuanira[i]!=hCalculo1[i]:
                                    hFisica2.append(hGuanira[i])
                                else:
                                    print("Se ha detectado un cruce de horarios. Por favor, escoja otro horario")
                            break
                        break
                    else:
                        volverfisica()
                
                profeestadavid()
                crediesta = 3
                while True:    
                    hEstadistica=[]
                    hMontesino=[[3,28800],[4,28800],[5,36000]]
                    hRivas=[[1,28800],[2,46800],[5,46800]]
                    c=int(input("Escoja el profesor con el que desea llevar el curso:"))
                    if c==1:
                        while True:
                            for i in range(3):
                                if hMontesino[i] != hFisica2[i]:
                                    hEstadistica.append(hMontesino[i])
                                else:
                                    print("Se ha detectado un cruce de horarios. Por favor, escoja otro horario")
                                    volverestadistica()
                            break
                        break
                    # Rivas aca tiene cruce
                    elif c == 2:
                        while True:
                            for i in range(3):
                                if hRivas[0]!=hCalculo1[0] and hRivas[1]!=hFisica2[1] and hRivas[0]!=hFernandez[0] and hRivas[2]!=hGuanira[2]:
                                    hEstadistica.append(hRivas[i])
                                else:
                                    print("*************ALERTA************")
                                    print("Se ha detectado un cruce de horarios. Por favor, escoja otro horario")
                                    volverestadistica()
                                break
                            break
                            
                    else:
                        volverestadistica()

                profets2david()
                credits2 = 3
                while True:

                    d=int(input("Escoja el profesor con el que desea llevar el curso:"))
                    hTaller2=[]
                    hCordova=[[3,46800],[5,54000],[6,28800]]
                    hRamirez=[[4,54000],[1,68400],[6,36000]]
                    if d==1:
                        while True:
                            for i in range(3):
                                if hCordova[i]!=hCalculo1[i] and hCordova[i]!=hFisica2[i] and hCordova[i]!=hEstadistica[i]:
                                    hTaller2.append(hCordova[i])
                                else:
                                    print("Se ha detectado un cruce de horarios. Por favor, escoja otro horario")
                                    volvertaller2()
                            break
                        break
                    elif d == 2:
                        while True:
                            for i in range(3):
                                if  hRamirez[i]!=hCalculo1[i] and hRamirez[i]!=hFisica2[i] and hRamirez[i]!=hEstadistica[i]:
                                    hTaller2.append(hRamirez[i])
                                else:
                                    print("Se ha detectado un cruce de horarios. Por favor, escoja otro horario")
                                    volvertaller2()
                            break
                        break
                    else:
                        volvertaller2()
                    

                profeecodavid()
                credieco = 3
                while True:
                    e=int(input("Escoja el profesor con el que desea llevar el curso:"))
                    hEconomia=[]
                    hTamariz=[[2,54000],[5,61200],[6,54000]]
                    hPaz=[[3,54000],[4,68400],[6,46800]]
                    if e==1:
                        while True:
                            for i in range(3):
                                if hTamariz[i]!=hCalculo1[i] and hTamariz[i]!=hFisica2[i] and hTamariz[i]!=hEstadistica[i] and hTamariz[i]!=hTaller2[i] :
                                    hEconomia.append(hTamariz[i])
                                else:
                                    print("Se ha detectado un cruce de horarios. Por favor, escoja otro horario")
                            break
                        break
                    elif e == 2:
                        while True:
                            for i in range(3):
                                if hPaz[i]!=hCalculo1[i] and hPaz[i]!=hEstadistica[i] and hPaz[i]!=hFisica2[i] and hPaz[i]!=hTaller2:
                                    hEconomia.append(hPaz[i])
                                else:
                                    print("Se ha detectado un cruce de horarios. Por favor, escoja otro horario")
                            break
                        break
                    else:
                        volvereconomia()

                profeingles6()
                crediingles = 3
                while True:
                    f=int(input("Escoja el profesor con el que desea llevar el curso:"))
                    hIngles=[]
                    hMuller=[[1,54000],[2,68400],[5,68400]]
                    hDuran=[[3,68400],[5,68400],[6,68400]]
                    if f==1:
                        while True:
                            for i in range(3):
                                if hMuller[i]!=hCalculo1[i] and hMuller[i]!=hFisica2[i] and hMuller[i]!=hEstadistica[i] and hMuller[i]!=hTaller2[i] or hMuller[i]==hEconomia[i]:
                                    hIngles.append(hMuller[i])
                                else:
                                    print("Se ha detectado un cruce de horarios. Por favor, escoja otro horario")
                            break
                        break
                    elif f==2:
                        while True:
                            for i in range(3):
                                if  hDuran[i]!=hCalculo1[i] and hDuran[i]!=hFisica2[i] and hDuran[i]!=hEstadistica[i] and hDuran[i]!=hTaller2[i] or hDuran[i]==hEconomia[i]:
                                    hIngles.append(hDuran[i])
                                else:
                                    print("Se ha detectado un cruce de horarios. Por favor, escoja otro horario")
                            break
                        break
                    else:
                        volveringles6()

                diasCalculo=[]  ## Arreglo donde se guarda las primeras componentes del contenido del arreglo hCalculo2
                dCalculo=[] ## Arreglo donde se guarda a que día corresponde cada componente del arreglo diasCalculo
                horarioCalculo=[] ## Arreglo donde se guarda las segundas componentes del contenido del arreglo hCalculo2
                tiempoInicialCalculo=[] ## Arreglo donde se guarda la hora inicial de la clase
                tiempoFinCalculo=[] ## Arreglo donde se guarda la hora final de la clase
                
                
                for i in range(3):
                    diasCalculo.append(hCalculo1[i][0])
                
                for i in range(3):
                    if diasCalculo[i]==1:
                        dCalculo.append('Lunes')
                    if diasCalculo[i]==2:
                        dCalculo.append('Martes')
                    if diasCalculo[i]==3:
                        dCalculo.append('Miércoles')
                    if diasCalculo[i]==4:
                        dCalculo.append('Jueves')
                    if diasCalculo[i]==5:
                        dCalculo.append('Viernes')
                    if diasCalculo[i]==6:
                        dCalculo.append('Sábado')
                for i in range(3):
                    horarioCalculo.append(hCalculo1[i][1])
                for i in range(3):
                    tiempoInicialCalculo.append(horarioCalculo[i]//3600)
                    tiempoFinCalculo.append((horarioCalculo[i]//3600)+2)


                print("Usted tiene Cálculo 1, los siguientes días:")
                for i in range(3):
                    print(dCalculo[i],"de",tiempoInicialCalculo[i],"a",tiempoFinCalculo[i],"horas")


                diasFisica=[]  ## Arreglo donde se guarda las primeras componentes del contenido del arreglo hFisica2
                dFisica=[] ## Arreglo donde se guarda a que día corresponde cada componente del arreglo diasFisica
                horarioFisica=[] ## Arreglo donde se guarda las segundas componentes del contenido del arreglo hFisica2
                tiempoInicialFisica=[] ## Arreglo donde se guarda la hora inicial de la clase
                tiempoFinFisica=[] ## Arreglo donde se guarda la hora final de la clase
                
                
                for i in range(3):
                    diasFisica.append(hFisica2[i][0])
                
                for i in range(3):
                    if diasFisica[i]==1:
                        dFisica.append('Lunes')
                    if diasFisica[i]==2:
                        dFisica.append('Martes')
                    if diasFisica[i]==3:
                        dFisica.append('Miércoles')
                    if diasFisica[i]==4:
                        dFisica.append('Jueves')
                    if diasFisica[i]==5:
                        dFisica.append('Viernes')
                    if diasFisica[i]==6:
                        dFisica.append('Sábado')
                for i in range(3):
                    horarioFisica.append(hFisica2[i][1])
                for i in range(3):
                    tiempoInicialFisica.append(horarioFisica[i]//3600)
                    tiempoFinFisica.append((horarioFisica[i]//3600)+2)


                print("Usted tiene Física 2, los siguientes días:")
                for i in range(3):
                    print(dFisica[i],"de",tiempoInicialFisica[i],"a",tiempoFinFisica[i],"horas")


                diasEstadistica=[]  ## Arreglo donde se guarda las primeras componentes del contenido del arreglo hEstadistica
                dEstadistica=[] ## Arreglo donde se guarda a que día corresponde cada componente del arreglo diasEstadistica
                horarioEstadistica=[] ## Arreglo donde se guarda las segundas componentes del contenido del arreglo hEstadistica
                tiempoInicialEstadistica=[] ## Arreglo donde se guarda la hora inicial de la clase
                tiempoFinEstadistica=[] ## Arreglo donde se guarda la hora final de la clase
                
                
                for i in range(3):
                    diasEstadistica.append(hEstadistica[i][0])
                
                for i in range(3):
                    if diasEstadistica[i]==1:
                        dEstadistica.append('Lunes')
                    if diasEstadistica[i]==2:
                        dEstadistica.append('Martes')
                    if diasEstadistica[i]==3:
                        dEstadistica.append('Miércoles')
                    if diasEstadistica[i]==4:
                        dEstadistica.append('Jueves')
                    if diasEstadistica[i]==5:
                        dEstadistica.append('Viernes')
                    if diasEstadistica[i]==6:
                        dEstadistica.append('Sábado')
                for i in range(3):
                    horarioEstadistica.append(hEstadistica[i][1])
                for i in range(3):
                    tiempoInicialEstadistica.append(horarioEstadistica[i]//3600)
                    tiempoFinEstadistica.append((horarioEstadistica[i]//3600)+2)


                print("Usted tiene Estadística, los siguientes días:")
                for i in range(3):
                    print(dEstadistica[i],"de",tiempoInicialEstadistica[i],"a",tiempoFinEstadistica[i],"horas")
                


                diasTaller=[]  ## Arreglo donde se guarda las primeras componentes del contenido del arreglo hTaller2
                dTaller=[] ## Arreglo donde se guarda a que día corresponde cada componente del arreglo diasTaller
                horarioTaller=[] ## Arreglo donde se guarda las segundas componentes del contenido del arreglo hTaller2
                tiempoInicialTaller=[] ## Arreglo donde se guarda la hora inicial de la clase
                tiempoFinTaller=[] ## Arreglo donde se guarda la hora final de la clase
                
                
                for i in range(3):
                    diasTaller.append(hTaller2[i][0])
                
                for i in range(3):
                    if diasTaller[i]==1:
                        dTaller.append('Lunes')
                    if diasTaller[i]==2:
                        dTaller.append('Martes')
                    if diasTaller[i]==3:
                        dTaller.append('Miércoles')
                    if diasTaller[i]==4:
                        dTaller.append('Jueves')
                    if diasTaller[i]==5:
                        dTaller.append('Viernes')
                    if diasTaller[i]==6:
                        dTaller.append('Sábado')
                for i in range(3):
                    horarioTaller.append(hTaller2[i][1])
                for i in range(3):
                    tiempoInicialTaller.append(horarioTaller[i]//3600)
                    tiempoFinTaller.append((horarioTaller[i]//3600)+2)


                print("Usted tiene Taller 2, los siguientes días:")
                for i in range(3):
                    print(dTaller[i],"de",tiempoInicialTaller[i],"a",tiempoFinTaller[i],"horas")


                diasEconomia=[]  ## Arreglo donde se guarda las primeras componentes del contenido del arreglo hEconomia
                dEconomia=[] ## Arreglo donde se guarda a que día corresponde cada componente del arreglo diasEconomia
                horarioEconomia=[] ## Arreglo donde se guarda las segundas componentes del contenido del arreglo hEconomia
                tiempoInicialEconomia=[] ## Arreglo donde se guarda la hora inicial de la clase
                tiempoFinEconomia=[] ## Arreglo donde se guarda la hora final de la clase
                
                
                for i in range(3):
                    diasEconomia.append(hEconomia[i][0])
                
                for i in range(3):
                    if diasEconomia[i]==1:
                        dEconomia.append('Lunes')
                    if diasEconomia[i]==2:
                        dEconomia.append('Martes')
                    if diasEconomia[i]==3:
                        dEconomia.append('Miércoles')
                    if diasEconomia[i]==4:
                        dEconomia.append('Jueves')
                    if diasEconomia[i]==5:
                        dEconomia.append('Viernes')
                    if diasEconomia[i]==6:
                        dEconomia.append('Sábado')
                for i in range(3):
                    horarioEconomia.append(hEconomia[i][1])
                for i in range(3):
                    tiempoInicialEconomia.append(horarioEconomia[i]//3600)
                    tiempoFinEconomia.append((horarioEconomia[i]//3600)+2)


                print("Usted tiene Economía, los siguientes días:")
                for i in range(3):
                    print(dEconomia[i],"de",tiempoInicialEconomia[i],"a",tiempoFinEconomia[i],"horas")


                diasIngles=[]  ## Arreglo donde se guarda las primeras componentes del contenido del arreglo hIngles
                dIngles=[] ## Arreglo donde se guarda a que día corresponde cada componente del arreglo diasIngles
                horarioIngles=[] ## Arreglo donde se guarda las segundas componentes del contenido del arreglo hIngles
                tiempoInicialIngles=[] ## Arreglo donde se guarda la hora inicial de la clase
                tiempoFinIngles=[] ## Arreglo donde se guarda la hora final de la clase
                
                
                for i in range(3):
                    diasIngles.append(hIngles[i][0])
                
                for i in range(3):
                    if diasIngles[i]==1:
                        dIngles.append('Lunes')
                    if diasIngles[i]==2:
                        dIngles.append('Martes')
                    if diasIngles[i]==3:
                        dIngles.append('Miércoles')
                    if diasIngles[i]==4:
                        dIngles.append('Jueves')
                    if diasIngles[i]==5:
                        dIngles.append('Viernes')
                    if diasIngles[i]==6:
                        dIngles.append('Sábado')
                for i in range(3):
                    horarioIngles.append(hIngles[i][1])
                for i in range(3):
                    tiempoInicialIngles.append(horarioIngles[i]//3600)
                    tiempoFinIngles.append((horarioIngles[i]//3600)+2)


                print("Usted tiene Inglés 6, los siguientes días:")
                for i in range(3):
                    print(dIngles[i],"de",tiempoInicialIngles[i],"a",tiempoFinIngles[i],"horas")
                sumacreditos = credical+credieco+crediesta+credifi+crediingles+credits2
                print("Creditos totales: ", sumacreditos)
                break

            # SI ES QUE SELECCIONA NO QUIERE LLEVAR CALCULO    
            else:
                profefisicadavid()
                credifi = 3
                while True:
                    b=int(input("Escoja el profesor con el que desea llevar el curso:"))
                    hFisica2=[]
                    hGarcía=[[1,36000],[2,46800],[4,46800]]
                    hGuanira=[[1,46800],[2,28800],[5,46800]]
                    if b == 1:
                        for i in range(3):
                            hFisica2.append(hGarcía[i])
                        break
                    
                    elif b == 2:
                        for i in range(3):
                                hFisica2.append(hGuanira[i])
                        break
                    else:
                        volverfisica()
                
                profeestadavid()
                crediesta = 3
                while True:    
                    hEstadistica=[]
                    hMontesino=[[3,28800],[4,28800],[5,36000]]
                    hRivas=[[1,28800],[2,46800],[5,46800]]
                    c=int(input("Escoja el profesor con el que desea llevar el curso:"))
                    if c==1:
                        while True:
                            for i in range(3):
                                if hMontesino[i] != hFisica2[i]:
                                    hEstadistica.append(hMontesino[i])
                                else:
                                    print("Se ha detectado un cruce de horarios. Por favor, escoja otro horario")
                                    volverestadistica()
                            break
                        break
                    # Rivas aca tiene cruce
                    elif c == 2:
                        while True:
                            for i in range(3):
                                if hRivas[1]!=hFisica2[1] and hRivas[2]!=hGuanira[2]:
                                    hEstadistica.append(hRivas[i])
                                else:
                                    print("*************ALERTA************")
                                    print("Se ha detectado un cruce de horarios. Por favor, escoja otro horario")
                                    volverestadistica()
                                break
                            break
                            
                    else:
                        volverestadistica()

                profets2david()
                credits2 = 3
                while True:

                    d=int(input("Escoja el profesor con el que desea llevar el curso:"))
                    hTaller2=[]
                    hCordova=[[3,46800],[5,54000],[6,28800]]
                    hRamirez=[[4,54000],[1,68400],[6,36000]]
                    if d==1:
                        while True:
                            for i in range(3):
                                if hCordova[i]!=hFisica2[i] and hCordova[i]!=hEstadistica[i]:
                                    hTaller2.append(hCordova[i])
                                else:
                                    print("Se ha detectado un cruce de horarios. Por favor, escoja otro horario")
                                    volvertaller2()
                            break
                        break
                    elif d == 2:
                        while True:
                            for i in range(3):
                                if  hRamirez[i]!=hFisica2[i] and hRamirez[i]!=hEstadistica[i]:
                                    hTaller2.append(hRamirez[i])
                                else:
                                    print("Se ha detectado un cruce de horarios. Por favor, escoja otro horario")
                                    volvertaller2()
                            break
                        break
                    else:
                        volvertaller2()
                    

                profeecodavid()
                credieco = 3
                while True:
                    e=int(input("Escoja el profesor con el que desea llevar el curso:"))
                    hEconomia=[]
                    hTamariz=[[2,54000],[5,61200],[6,54000]]
                    hPaz=[[3,54000],[4,68400],[6,46800]]
                    if e==1:
                        while True:
                            for i in range(3):
                                if hTamariz[i]!=hFisica2[i] and hTamariz[i]!=hEstadistica[i] and hTamariz[i]!=hTaller2[i] :
                                    hEconomia.append(hTamariz[i])
                                else:
                                    print("Se ha detectado un cruce de horarios. Por favor, escoja otro horario")
                            break
                        break
                    elif e == 2:
                        while True:
                            for i in range(3):
                                if hPaz[i]!=hEstadistica[i] and hPaz[i]!=hFisica2[i] and hPaz[i]!=hTaller2:
                                    hEconomia.append(hPaz[i])
                                else:
                                    print("Se ha detectado un cruce de horarios. Por favor, escoja otro horario")
                            break
                        break
                    else:
                        volvereconomia()

                profeingles6()
                crediingles = 3
                while True:
                    f=int(input("Escoja el profesor con el que desea llevar el curso:"))
                    hIngles=[]
                    hMuller=[[1,54000],[2,68400],[5,68400]]
                    hDuran=[[3,68400],[5,68400],[6,68400]]
                    if f==1:
                        while True:
                            for i in range(3):
                                if hMuller[i]!=hFisica2[i] and hMuller[i]!=hEstadistica[i] and hMuller[i]!=hTaller2[i] or hMuller[i]==hEconomia[i]:
                                    hIngles.append(hMuller[i])
                                else:
                                    print("Se ha detectado un cruce de horarios. Por favor, escoja otro horario")
                            break
                        break
                    elif f==2:
                        while True:
                            for i in range(3):
                                if  hDuran[i]!=hFisica2[i] and hDuran[i]!=hEstadistica[i] and hDuran[i]!=hTaller2[i] or hDuran[i]==hEconomia[i]:
                                    hIngles.append(hDuran[i])
                                else:
                                    print("Se ha detectado un cruce de horarios. Por favor, escoja otro horario")
                            break
                        break
                    else:
                        volveringles6()
                diasFisica=[]  ## Arreglo donde se guarda las primeras componentes del contenido del arreglo hFisica2
                dFisica=[] ## Arreglo donde se guarda a que día corresponde cada componente del arreglo diasFisica
                horarioFisica=[] ## Arreglo donde se guarda las segundas componentes del contenido del arreglo hFisica2
                tiempoInicialFisica=[] ## Arreglo donde se guarda la hora inicial de la clase
                tiempoFinFisica=[] ## Arreglo donde se guarda la hora final de la clase
                
                
                for i in range(3):
                    diasFisica.append(hFisica2[i][0])
                
                for i in range(3):
                    if diasFisica[i]==1:
                        dFisica.append('Lunes')
                    if diasFisica[i]==2:
                        dFisica.append('Martes')
                    if diasFisica[i]==3:
                        dFisica.append('Miércoles')
                    if diasFisica[i]==4:
                        dFisica.append('Jueves')
                    if diasFisica[i]==5:
                        dFisica.append('Viernes')
                    if diasFisica[i]==6:
                        dFisica.append('Sábado')
                for i in range(3):
                    horarioFisica.append(hFisica2[i][1])
                for i in range(3):
                    tiempoInicialFisica.append(horarioFisica[i]//3600)
                    tiempoFinFisica.append((horarioFisica[i]//3600)+2)


                print("Usted tiene Física 2, los siguientes días:")
                for i in range(3):
                    print(dFisica[i],"de",tiempoInicialFisica[i],"a",tiempoFinFisica[i],"horas")


                diasEstadistica=[]  ## Arreglo donde se guarda las primeras componentes del contenido del arreglo hEstadistica
                dEstadistica=[] ## Arreglo donde se guarda a que día corresponde cada componente del arreglo diasEstadistica
                horarioEstadistica=[] ## Arreglo donde se guarda las segundas componentes del contenido del arreglo hEstadistica
                tiempoInicialEstadistica=[] ## Arreglo donde se guarda la hora inicial de la clase
                tiempoFinEstadistica=[] ## Arreglo donde se guarda la hora final de la clase
                
                
                for i in range(3):
                    diasEstadistica.append(hEstadistica[i][0])
                
                for i in range(3):
                    if diasEstadistica[i]==1:
                        dEstadistica.append('Lunes')
                    if diasEstadistica[i]==2:
                        dEstadistica.append('Martes')
                    if diasEstadistica[i]==3:
                        dEstadistica.append('Miércoles')
                    if diasEstadistica[i]==4:
                        dEstadistica.append('Jueves')
                    if diasEstadistica[i]==5:
                        dEstadistica.append('Viernes')
                    if diasEstadistica[i]==6:
                        dEstadistica.append('Sábado')
                for i in range(3):
                    horarioEstadistica.append(hEstadistica[i][1])
                for i in range(3):
                    tiempoInicialEstadistica.append(horarioEstadistica[i]//3600)
                    tiempoFinEstadistica.append((horarioEstadistica[i]//3600)+2)


                print("Usted tiene Estadística, los siguientes días:")
                for i in range(3):
                    print(dEstadistica[i],"de",tiempoInicialEstadistica[i],"a",tiempoFinEstadistica[i],"horas")
                


                diasTaller=[]  ## Arreglo donde se guarda las primeras componentes del contenido del arreglo hTaller2
                dTaller=[] ## Arreglo donde se guarda a que día corresponde cada componente del arreglo diasTaller
                horarioTaller=[] ## Arreglo donde se guarda las segundas componentes del contenido del arreglo hTaller2
                tiempoInicialTaller=[] ## Arreglo donde se guarda la hora inicial de la clase
                tiempoFinTaller=[] ## Arreglo donde se guarda la hora final de la clase
                
                
                for i in range(3):
                    diasTaller.append(hTaller2[i][0])
                
                for i in range(3):
                    if diasTaller[i]==1:
                        dTaller.append('Lunes')
                    if diasTaller[i]==2:
                        dTaller.append('Martes')
                    if diasTaller[i]==3:
                        dTaller.append('Miércoles')
                    if diasTaller[i]==4:
                        dTaller.append('Jueves')
                    if diasTaller[i]==5:
                        dTaller.append('Viernes')
                    if diasTaller[i]==6:
                        dTaller.append('Sábado')
                for i in range(3):
                    horarioTaller.append(hTaller2[i][1])
                for i in range(3):
                    tiempoInicialTaller.append(horarioTaller[i]//3600)
                    tiempoFinTaller.append((horarioTaller[i]//3600)+2)


                print("Usted tiene Taller 2, los siguientes días:")
                for i in range(3):
                    print(dTaller[i],"de",tiempoInicialTaller[i],"a",tiempoFinTaller[i],"horas")


                diasEconomia=[]  ## Arreglo donde se guarda las primeras componentes del contenido del arreglo hEconomia
                dEconomia=[] ## Arreglo donde se guarda a que día corresponde cada componente del arreglo diasEconomia
                horarioEconomia=[] ## Arreglo donde se guarda las segundas componentes del contenido del arreglo hEconomia
                tiempoInicialEconomia=[] ## Arreglo donde se guarda la hora inicial de la clase
                tiempoFinEconomia=[] ## Arreglo donde se guarda la hora final de la clase
                
                
                for i in range(3):
                    diasEconomia.append(hEconomia[i][0])
                
                for i in range(3):
                    if diasEconomia[i]==1:
                        dEconomia.append('Lunes')
                    if diasEconomia[i]==2:
                        dEconomia.append('Martes')
                    if diasEconomia[i]==3:
                        dEconomia.append('Miércoles')
                    if diasEconomia[i]==4:
                        dEconomia.append('Jueves')
                    if diasEconomia[i]==5:
                        dEconomia.append('Viernes')
                    if diasEconomia[i]==6:
                        dEconomia.append('Sábado')
                for i in range(3):
                    horarioEconomia.append(hEconomia[i][1])
                for i in range(3):
                    tiempoInicialEconomia.append(horarioEconomia[i]//3600)
                    tiempoFinEconomia.append((horarioEconomia[i]//3600)+2)


                print("Usted tiene Economía, los siguientes días:")
                for i in range(3):
                    print(dEconomia[i],"de",tiempoInicialEconomia[i],"a",tiempoFinEconomia[i],"horas")


                diasIngles=[]  ## Arreglo donde se guarda las primeras componentes del contenido del arreglo hIngles
                dIngles=[] ## Arreglo donde se guarda a que día corresponde cada componente del arreglo diasIngles
                horarioIngles=[] ## Arreglo donde se guarda las segundas componentes del contenido del arreglo hIngles
                tiempoInicialIngles=[] ## Arreglo donde se guarda la hora inicial de la clase
                tiempoFinIngles=[] ## Arreglo donde se guarda la hora final de la clase
                
                
                for i in range(3):
                    diasIngles.append(hIngles[i][0])
                
                for i in range(3):
                    if diasIngles[i]==1:
                        dIngles.append('Lunes')
                    if diasIngles[i]==2:
                        dIngles.append('Martes')
                    if diasIngles[i]==3:
                        dIngles.append('Miércoles')
                    if diasIngles[i]==4:
                        dIngles.append('Jueves')
                    if diasIngles[i]==5:
                        dIngles.append('Viernes')
                    if diasIngles[i]==6:
                        dIngles.append('Sábado')
                for i in range(3):
                    horarioIngles.append(hIngles[i][1])
                for i in range(3):
                    tiempoInicialIngles.append(horarioIngles[i]//3600)
                    tiempoFinIngles.append((horarioIngles[i]//3600)+2)


                print("Usted tiene Inglés 6, los siguientes días:")
                for i in range(3):
                    print(dIngles[i],"de",tiempoInicialIngles[i],"a",tiempoFinIngles[i],"horas")
                sumacreditos = credieco+crediesta+credifi+crediingles+credits2
                print("Creditos totales: ", sumacreditos)
                break
        break

    else:
        print("Opción inexistente, seleccione nuevamente")       
        




       
            
          
          


           
        
        
       
        
    

    





