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

opcionalum = int(input("Seleccione una opcion del menu usilio: "))
cursos=["c1","f1","poo","t","m","intro"]
cursos2020=["Calculo 2","Fisica 2","Estadistica", "Taller 2", "Economia", "Ingles 6"]
diasSemana=["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado"]


while True:
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
        else:
            print("A continuación se mostrará la lista de profesores de cada curso que puedas llevar:")
            print("Cálculo 2: "
            "\n1. José Reyes"
            "\n2. Luisa Fernández")
            a=int(input("Escoja el profesor con el que desea llevar el curso:"))
            hCalculo2=[]
            hReyes=[[1,28800],[2,36000],[4,36000]]
            hFernandez=[[2,36000],[3,36000],[5,28800]]
            if a==1:
                for i in range(3):
                    hCalculo2.append(hReyes[i])
            else:
                for i in range(3):
                    hCalculo2.append(hFernandez[i])
                
            
            print("Física 2: "
            "\n1. Iris García"
            "\n2. Richard Guanira")
            while True:
                b=int(input("Escoja el profesor con el que desea llevar el curso:"))
                hFisica2=[]
                hGarcía=[[1,36000],[2,46800],[4,46800]]
                hGuanira=[[1,46800],[2,28800],[5,36000]]
                if b==1:
                    while True:
                        for i in range(3):
                            if hGarcía[i]!=hCalculo2[i]:
                                hFisica2.append(hGarcía[i])
                                
                                
                            else:
                                print("Se ha detectado un cruce de horarios. Por favor, escoja otro horario")
                                
                                
                        break

                
                else:
                    while True:
                        for i in range(3):
                            if hGuanira[i]==hCalculo2[i]:
                                print("Se ha detectado un cruce de horarios. Por favor, escoja otro horario")
                                
                            else:
                                hFisica2.append(hGuanira[i])
                                
                        break
                break
            



            print("Estadística: "
            "\n1. Pedro Montesino"
            "\n2. Omar Rivas")
            while True:    
                c=int(input("Escoja el profesor con el que desea llevar el curso:"))
                hEstadistica=[]
                hMontesino=[[3,28800],[4,28800],[5,36000]]
                hRivas=[[1,28800],[2,46800],[5,46800]]
                if c==1:
                    while True:
                        for i in range(3):
                            if hMontesino[i]!=hCalculo2[i] or hMontesino[i]!=hFisica2[i]:
                                hEstadistica.append(hMontesino[i])
                                
                            else:
                                print("Se ha detectado un cruce de horarios. Por favor, escoja otro horario")
                                
                        break
                else:
                    while True:
                        for i in range(3):
                            if hRivas[i]!=hCalculo2[i] or hRivas[i]!=hFisica2[i]:
                                hEstadistica.append(hRivas[i])
                                
                            else:
                                print("Se ha detectado un cruce de horarios. Por favor, escoja otro horario")
                                
                        break
                break

                                


            print("Taller 2:"
            "\n1. María Cordova"
            "\n2. Carmen Ramírez")
            while True:

                d=int(input("Escoja el profesor con el que desea llevar el curso:"))
                hTaller2=[]
                hCordova=[[3,46800],[5,28800],[6,28800]]
                hRamirez=[[4,28800],[1,36000],[6,36000]]
                if d==1:
                    while True:
                        for i in range(3):
                            if hCordova[i]==hCalculo2[i] or hCordova[i]==hFisica2[i] or hCordova[i]==hEstadistica[i] :
                                print("Se ha detectado un cruce de horarios. Por favor, escoja otro horario")
                            else:
                                hTaller2.append(hCordova[i])
                        break
                else:
                    while True:
                        for i in range(3):
                            if hRamirez[i]==hCalculo2[i] or hRamirez[i]==hFisica2[i] or hRamirez[i]==hEstadistica[i]:
                                print("Se ha detectado un cruce de horarios. Por favor, escoja otro horario")
                            else:
                                hTaller2.append(hRamirez[i])
                        break
                break


            print("Economía:"
            "\n1. Cielo Tamariz"
            "\n2. Ricardo Paz")
            while True:
                e=int(input("Escoja el profesor con el que desea llevar el curso:"))
                hEconomia=[]
                hTamariz=[[2,28800],[5,46800],[6,36000]]
                hPaz=[[3,28800],[4,36000],[6,46800]]
                if e==1:
                    while True:
                        for i in range(3):
                            if hTamariz[i]==hCalculo2[i] or hTamariz[i]==hFisica2[i] or hTamariz[i]==hEstadistica[i] or hTamariz[i]==hTaller2[i] :
                                print("Se ha detectado un cruce de horarios. Por favor, escoja otro horario")
                            else:
                                hEconomia.append(hTamariz[i])
                        break
                else:
                    while True:
                        for i in range(3):
                            if hPaz[i]==hCalculo2[i] or hPaz[i]==hFisica2[i] or hPaz[i]==hEstadistica[i] or hPaz[i]==hTaller2[i]:
                                print("Se ha detectado un cruce de horarios. Por favor, escoja otro horario")
                            else:
                                hEconomia.append(hPaz[i])
                        break
                break

            print("Inglés 6:"
            "\n1. Mariell Muller"
            "\n2. Rocío Durán")
            while True:

                f=int(input("Escoja el profesor con el que desea llevar el curso:"))
                hIngles=[]
                hMuller=[[1,46800],[3,36000],[6,46800]]
                hDuran=[[3,46800],[4,46800],[6,28800]]
                if f==1:
                    while True:
                        for i in range(3):
                            if hMuller[i]==hCalculo2[i] or hMuller[i]==hFisica2[i] or hMuller[i]==hEstadistica[i] or hMuller[i]==hTaller2[i] or hMuller[i]==hEconomia[i]:
                                print("Se ha detectado un cruce de horarios. Por favor, escoja otro horario")
                            else:
                                hIngles.append(hMuller[i])
                        break
                else:
                    while True:
                        for i in range(3):
                            if hDuran[i]==hCalculo2[i] or hDuran[i]==hFisica2[i] or hDuran[i]==hEstadistica[i] or hDuran[i]==hTaller2[i] or hDuran[i]==hEconomia[i]:
                                print("Se ha detectado un cruce de horarios. Por favor, escoja otro horario")
                            else:
                                hIngles.append(hDuran[i])
                        break
                break


        








if opcionalum == 3:
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
        




       
            
          
          


           
        
        
       
        
    

    





