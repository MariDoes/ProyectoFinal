import os
os.system("cls")

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
    continuar = input("Desea ir a la eleccion de horarios? S/N: ")
        




       
            
          
          


           
        
        
       
        
    

    




