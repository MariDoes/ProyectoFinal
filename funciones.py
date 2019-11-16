# Menu carrera
def mostrarmenucarreraquinto():
    print("Felicitaciones estás apto para acceder a la Beca quinto superior")
    print("Por favor ingresa ingresa la carrera a la que vas a postular")
    print("1 - Ingeniería informátiva y de sistemas")
    print("2 - Administración para los negocios")
    print("3 - Arquitectura")
    print("4 - Regresar atras")

def mostrarmenucarreratercio():
    print("Felicitaciones estás apto para acceder a la Beca tercio superior")
    print("Por favor ingresa ingresa la carrera a la que vas a postular")
    print("1 - Ingeniería informátiva y de sistemas")
    print("2 - Administración para los negocios")
    print("3 - Arquitectura")
    print("4 - Regresar atras")

def mostrarmenucarerrabeca18():
    print("Bienvenido estás en la modalidad Beca 18")
    print("Por favor ingresa ingresa la carrera a la que vas a postular")
    print("1 - Ingeniería informátiva y de sistemas")
    print("2 - Administración para los negocios")
    print("3 - Arquitectura")
    print("4 - Regresar atras")

def mostrarmenucarreranormal():
    print("Bienvenido estás en la modalidad adimisión normal")
    print("Por favor ingresa ingresa la carrera a la que vas a postular")
    print("1 - Ingeniería informátiva y de sistemas")
    print("2 - Administración para los negocios")
    print("3 - Arquitectura")
    print("4 - Regresar atras")


# Menu colegio

def colegios():
    print("1 - Inova School / Tricel / Pamer / Saco Oliveros"
    "\n2 - Markham / Raimondi / Franklin Delano Roosevelt "
    "\n3 - Mariano Melgar / Augusto Salazar Bondy"
    "\n4 - Otros")

# Menu principal y secundarios
def menuprincipal():
    print("Bienvenidos a nuestro sistema matricula"
    "\ndonde aca le ayudaremos a darle informacion si eres postulante"
    "\no estudiante actual en nuestra universidad")
    print("Selecciona una de las opciones de su preferencia")
    print("1.- Alumno usilio"
    "\n2.- Postulante Pregrado"
    "\n3.- Salir")
def menupostulante():
    print("Has pulsado la opción postulante")
    print ("\t1 - Excelencia Académica")
    print ("\t2 - Beca 18")
    print ("\t3 - Admisión normal")
    print ("\t4 - Regresar")

# Boleta de couta
def cuotasistemas(total, descuento):
    print("*****Aqui esta su boleta de matricula******")
    print("Carrera: Ing de Sistemas, pagaras en su primera cuota:", total, "luego pagará cada una de las demás cuotas:",descuento)
    print("Si desea continuar con el proceso, venga a nuestros establecimiento, gracias.")

def cuotaadmi(total, descuento):
    print("*****Aqui esta su boleta de matricula******")
    print("Carrera: Administración para los negocios, pagaras en su primera cuota:", total, "luego pagará cada una de las demás cuotas:",descuento)
    print("Si desea continuar con el proceso, venga a nuestros establecimiento, gracias.")

def cuotaarqui(total, descuento):
    print("*****Aqui esta su boleta de matricula******")
    print("Carrera: Arquitectura, pagaras en su primera cuota:", total, "luego pagará cada una de las demás cuotas:",descuento)
    print("Si desea continuar con el proceso, venga a nuestros establecimiento, gracias.")

# Boleta beca 18
def beca18sist(a):
    print("usted a elegido la carrera de Ingeniería informática y de sistemas")
    print("*****Aqui esta su boleta de matricula******")
    print("Como usted pertenece a beca 18, entonces se cubrirá las siguiente cantidad de gastos ", a)
    print("Si desea continuar con el proceso, venga a nuestros establecimiento, gracias.")

def beca18admi(a):
    print("Usted a elegido la carrera de Administración para los negocios")
    print("*****Aqui esta su boleta de matricula******")
    print("Como usted pertenece a beca 18, entonces se cubrirá las siguiente cantidad de gastos ", a)
    print("Si desea continuar con el proceso, venga a nuestros establecimiento, gracias.")

def beca18arqui(a):
    print("Usted a elegido la carrera de Arquitecta")
    print("*****Aqui esta su boleta de matricula******")
    print("Como usted pertenece a beca 18, entonces se cubrirá las siguiente cantidad de gastos ", a)
    print("Si desea continuar con el proceso, venga a nuestros establecimiento, gracias.")

# Boleta Admisión normal
def normalsistemas(total ,precio):
    print("*****Aqui esta su boleta de matricula******")
    print("Carrera: Ing de Sistemas, pagaras en su primera cuota:", total, "luego pagará cada una de las demás cuotas:", precio)
    print("Si desea continuar con el proceso, venga a nuestros establecimiento, gracias.")

def normaladmi(total,precio):
    print("*****Aqui esta su boleta de matricula******")
    print("Carrera: Administración para los negocios, pagaras en su primera cuota:", total, "luego pagará cada una de las demás cuotas:", precio)
    print("Si desea continuar con el proceso, venga a nuestros establecimiento, gracias.")

def normalarqui(total,precio):
    print("*****Aqui esta su boleta de matricula******")
    print("Carrera: Arquitectura, pagaras en su primera cuota:", total, "luego pagará cada una de las demás cuotas:", precio)
    print("Si desea continuar con el proceso, venga a nuestros establecimiento, gracias.")

# Metodo para regresar a menus
def regresarmenucarrera():
    print("Por favor ingresa ingresa la carrera a la que vas a postular")
    print("1 - Ingeniería informátiva y de sistemas")
    print("2 - Administración para los negocios")
    print("3 - Arquitectura")
    print("4 - Regresar atras")

def regresarmunupostulante():
    print("Seleccione una de las opciones del menu de Postulante nuevamente")
    print ("\t1 - Excelencia Académica")
    print ("\t2 - Beca 18")
    print ("\t3 - Admisión normal")
    print ("\t4 - Regresar atras")



# Calculos
def totalnormal(precio):
    return precio + 300

def totaltercio(precio):
    return precio*0.7 + 300

def totalquito(precio):
    return precio*0.5 + 300

def promedio(a,b,c,d,e):
    return (a+b+c+d+e)

# Reporte de notas 
def notasdavid():
    print("Reporte de cursos: ")
    print("En Calculo I lo has pasado con 15, pasaste a la 1era " )
    print("En Fisica I lo has pasado con 14, pasaste a la 1era ")
    print("En Poo lo has pasado con 17, pasaste a la 1era")
    print("En Taller lo has pasado con 18, pasaste a la 1era")
    print("En Marketing lo has pasado con 14, pasaste a la 1era")
    print("En Intro lo has pasado con 17, pasaste a la 1era")
    print("Esta disponible a llevar los cursos siguientes")
def notasmariaelena():
    print("Reporte de cursos: ")
    print("En Calculo I no lo has pasado, nota 10, lo llevaras por 2da vez " )
    print("En Estadistica lo has pasado con 14, pasaste a la 1era ")
    print("En Poo lo has pasado con 17, pasaste a la 1era")
    print("En Taller lo has pasado con 13, pasaste a la 1era")
    print("En ADD lo has pasado con 14, pasaste a la 1era")
    print("En Fisica general lo has pasado con 17, pasaste a la 1era")
    print("Esta disponible a llevar los cursos siguientes pero no de Calculo II")


# Para el horario
def volvercalculo2():
    print("Elige nuevamente")
    print("Cálculo 2: "
    "\n1. José Reyes"
    "\n2. Luisa Fernández")

def volverfisica():
    print("Elige nuevamente")
    print("Física 2: "
    "\n1. Iris García"
    "\n2. Richard Guanira")

def volverestadistica():
    print("Elige nuevamente")
    print("Estadística: "
    "\n1. Pedro Montesino"
    "\n2. Omar Rivas")

def volvertaller2():
    print("Elige nuevamente")
    print("Taller 2:"
    "\n1. María Cordova"
    "\n2. Carmen Ramírez")

def volvereconomia():
    print("Elige nuevamente")
    print("Economía:"
    "\n1. Cielo Tamariz"
    "\n2. Ricardo Paz")

def volveringles6():
    print("Elige nuevamente")
    print("Inglés 6:"
    "\n1. Mariell Muller"
    "\n2. Rocío Durán")

def estadistica():
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
                        volverestadistica()
                break
            break
        elif c == 2:
            while True:
                for i in range(3):
                    if hRivas[i]!=hCalculo2[i] and hRivas[i]!=hFisica2[i]:
                        hEstadistica.append(hRivas[i])
                    else:
                        print("Se ha detectado un cruce de horarios. Por favor, escoja otro horario")
                        x = input("Presione s para volver: ")
                        if x == "s":
                            volverestadistica()
                            break
                        break
                break
            break
        else:
            volverestadistica()