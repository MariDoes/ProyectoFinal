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

# Datos de alumno 
def david():
    print("Bienvenido alumno David, que desea realizar hoy")
    print("Le recordamos eres de la modalidad de tercio superior")
    print("Selecciona una de las opciones que desea realizar: "
    "\n1.- Numero de veces que llevas en un curso y notas"
    "\n2.- Eleccion de horarios 2020-01")
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
    "\n3.- Salir"
    "\n4.- Referencias")
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
    print("Cálculo 2, 4 creditos: "
    "\n1. José Reyes: Lunes de 8 a 10 horas Martes de 10 a 12 horas Jueves de 10 a 12 horas"
    "\n2. Luisa Fernández: Lunes de 8 a 10 horas Miércoles de 10 a 12 horas Viernes de 8 a 10 horas")

def volverfisica():
    print("Elige nuevamente")
    print("Física 2, 3 creditos: "
    "\n1. Iris García: Lunes de 10 a 12 horas Martes de 13 a 15 horas Jueves de 13 a 15 horas"
    "\n2. Richard Guanira: Lunes de 13 a 15 horas Martes de 8 a 10 horas Viernes de 13 a 15 horas")

def volverestadistica():
    print("Elige nuevamente")
    print("Estadística, 3 creditos: "
    "\n1. Pedro Montesino: Miércoles de 8 a 10 horas Jueves de 8 a 10 horas Viernes de 10 a 12 horas"
    "\n2. Omar Rivas: Lunes de 8 a 10 horas Martes de 13 a 15 horas Viernes de 13 a 15 horas")

def volvertaller2():
    print("Elige nuevamente")
    print("Taller 2, 3 creditos:"
    "\n1. María Cordova: Miércoles de 13 a 15 horas Viernes de 15 a 17 horas Sábado de 8 a 10 horas"
    "\n2. Carmen Ramírez: Jueves de 15 a 17 horas Lunes de 19 a 21 horas Sábado de 10 a 12 horas")

def volvereconomia():
    print("Elige nuevamente")
    print("Economía, 3 creditos:"
    "\n1. Cielo Tamariz: Martes de 15 a 17 horas Viernes de 17 a 19 horas Sábado de 15 a 17 horas"
    "\n2. Ricardo Paz: Miércoles de 15 a 17 horas Jueves de 19 a 21 horas Sábado de 13 a 15 horas")

def volveringles6():
    print("Elige nuevamente")
    print("Inglés 6, 3 creditos:"
    "\n1. Mariell Muller: Lunes de 15 a 17 horas Martes de 19 a 21 horas Viernes de 19 a 21 horas"
    "\n2. Rocío Durán: Miércoles de 19 a 21 horas Viernes de 19 a 21 horas Sábado de 19 a 21 horas")

def profcalculodavid():
    print("A continuación se mostrará la lista de profesores de cada curso que puedas llevar:")
    print("Cálculo 2, 4 creditos: "
    "\n1. José Reyes: Lunes de 8 a 10 horas Martes de 10 a 12 horas Jueves de 10 a 12 horas"
    "\n2. Luisa Fernández: Lunes de 8 a 10 horas Miércoles de 10 a 12 horas Viernes de 8 a 10 horas")

def profefisicadavid():
    print("Física 2, 3 creditos: "
    "\n1. Iris García: Lunes de 10 a 12 horas Martes de 13 a 15 horas Jueves de 13 a 15 horas"
    "\n2. Richard Guanira: Lunes de 13 a 15 horas Martes de 8 a 10 horas Viernes de 13 a 15 horas")
def profeestadavid():
    print("Estadística, 3 creditos: "
    "\n1. Pedro Montesino: Miércoles de 8 a 10 horas Jueves de 8 a 10 horas Viernes de 10 a 12 horas"
    "\n2. Omar Rivas: Lunes de 8 a 10 horas Martes de 13 a 15 horas Viernes de 13 a 15 horas")
def profets2david():
    print("Taller 2, 3 creditos:"
    "\n1. María Cordova: Miércoles de 13 a 15 horas Viernes de 15 a 17 horas Sábado de 8 a 10 horas"
    "\n2. Carmen Ramírez: Jueves de 15 a 17 horas Lunes de 19 a 21 horas Sábado de 10 a 12 horas")
def profeecodavid():
    print("Economía, 3 creditos:"
    "\n1. Cielo Tamariz: Martes de 15 a 17 horas Viernes de 17 a 19 horas Sábado de 15 a 17 horas"
    "\n2. Ricardo Paz: Miércoles de 15 a 17 horas Jueves de 19 a 21 horas Sábado de 13 a 15 horas")
def profeingles6():
    print("Inglés 6, 3 creditos:"
    "\n1. Mariell Muller: Lunes de 15 a 17 horas Martes de 19 a 21 horas Viernes de 19 a 21 horas"
    "\n2. Rocío Durán: Miércoles de 19 a 21 horas Viernes de 19 a 21 horas Sábado de 19 a 21 horas")

def volvercalculoI():
    print("Elige nuevamente")
    print("Cálculo 1, 4 creditos: "
    "\n1. Carlos Bravo: Lunes de 8 a 10 horas Martes de 10 a 12 horas Jueves de 10 a 12 horas"
    "\n2. Alex Lenin: Lunes de 8 a 10 horas Miércoles de 10 a 12 horas Viernes de 8 a 10 horas")

def profcalculomari():
    print("A continuación se mostrará la lista de profesores de cada curso que puedas llevar:")
    print("Cálculo 1, 4 creditos: "
    "\n1. Carlos Bravo: Lunes de 8 a 10 horas Martes de 10 a 12 horas Jueves de 10 a 12 horas"
    "\n2. Alex Lenin: Lunes de 8 a 10 horas Miércoles de 10 a 12 horas Viernes de 8 a 10 horas")