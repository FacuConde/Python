"""
-----------------------------------------------------------------------------------------------
Título: "Alas del Sur"
Fecha: 05/10/2023
Autor: Conde Zabulanes Facundo
Descripción: Ejercicio por desarrollar del primer parcial de Algoritmos y Estructuras de Datos 1.
-----------------------------------------------------------------------------------------------
"""
#----------------------------------------------------------------------------------------------
# MÓDULOS IMPORTADOS
#----------------------------------------------------------------------------------------------
import random


#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def cargarHorasDeVuelo(_baseDeAlumnos, _baseDeHoras, _baseDeAviones): 
    tipoDeAlumno = str(input("Desea cargar horas a un nuevo alumno? [S | N] :"))
    tipoDeAlumnoPermitido = ["S", "N", "s", "n"]
    avionesPermitidos = ["SESSNA", "PIPER", "PETREL"]
    while tipoDeAlumno not in tipoDeAlumnoPermitido:
        tipoDeAlumno = input("ERROR, debe ingresar S o N (S = nuevo - N = existente): ")
    if tipoDeAlumno == "S" or tipoDeAlumno == "s":
        nombre = input("Ingrese nombre del nuevo alumno:")
        while nombre.isalpha() == False:
            nombre = input("El nombre debe llevar letras, vuelva a intentarlo:")
        avion = input("Ingrese avión [SESSNA | PIPER | PETREL ] :")
        while avion not in avionesPermitidos:
            print("Avión inexistente, vuelva a intentar!")
            avion = input("Ingrese avión [SESSNA | PIPER | PETREL] :")
        horasDeVuelo = int(input("Ingrese la cantidad de horas de vuelo [Máximo 8 horas] :"))
        while horasDeVuelo > 8 or horasDeVuelo < 1 :
            print("Error, deben ser como máximo 8hs, y mínimo 1.")
            horasDeVuelo = int(input("Ingrese la cantidad de horas de vuelo [Máximo 8 horas] :"))
        _baseDeAlumnos.append(nombre)
        _baseDeAviones.append(avion)
        _baseDeHoras.append(horasDeVuelo)
        print("Ingreso almacenado con éxito!")
        print("")
        
    elif tipoDeAlumno == "N" or tipoDeAlumno == "n":
        alumnoExistente = str(input("Ingrese nombre del alumno:"))
        while alumnoExistente not in _baseDeAlumnos:
            print("El alumno no existe o fue mal ingresado, vuelva a intentar!")
            alumnoExistente = str(input("Ingrese nombre del alumno:"))
        posicionAlumnoExistente = _baseDeAlumnos.index(alumnoExistente)
        horas = int(input("Ingrese la cantidad de horas de vuelo [Máximo 8 horas] :"))
        while horas < 1 or horas > 8:
            horas = int(input("Error, debe ingresar una cantidad de horas válida. (Mínimo 1, máximo 8):"))
        _baseDeAlumnos.append(alumnoExistente)
        _baseDeAviones.append(_baseDeAviones[posicionAlumnoExistente])
        _baseDeHoras.append(horas)
        print("Ingreso almacenado con éxito!")
        print("")

def sortearAlumnoParaExamen(_baseDeAlumnos, _baseDeHoras, _baseDeAviones): # LLAMA A LA FUNCION "alumnoApto" PARA LLENAR LA LISTA "alumnosParaExamen" y verificar si el nombre sorteado reside en esa lista.
    while True:
        posicionSorteo = random.randint(0, (len(_baseDeAlumnos)-1))
        nombreSorteado = _baseDeAlumnos[posicionSorteo]
        avion = _baseDeAviones[posicionSorteo]
        alumnosParaExamen = []
        while len(alumnosParaExamen) < 1:
            alumnoApto(_baseDeAlumnos,_baseDeHoras,nombreSorteado)
        if nombreSorteado in _alumnosParaExamen:
            print("Alumno", nombreSorteado, "listo para el examen de piloto, con", horasTotales ,"horas de vuelo en avión", avion,"." )            
        else:
            print("Alumno", nombreSorteado," no esta apto para el examen de piloto. Ya que cuenta con", totalHoras,".")
            
def alumnoApto(baseDeAlumno, baseDeHora, nombreBuscar): # FUNCIÓN QUE DEBERÍA AGREGAR A LOS ALUMNOS SORTEADOS, QUE SEAN APTOS PARA EL SORTEO A LA LISTA "_alumnosParaExamen"
    horasAcumuladas = []
    _alumnosParaExamen = []
    for i, elemento in enumerate(baseDeAlumno):
        if i == nombreBuscar:
            horasAcumuladas.append(baseDeHora[i])
    totalHoras = sum(horasAcumuladas)
    if totalHoras > 40:
        _alumnosParaExamen.append(nombreBuscar)
    return _alumnosParaExamen

#----------------------------------------------------------------------------------------------
# "CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
# Declaración de variables
#----------------------------------------------------------------------------------------------
baseDeAlumnos = ["ROBERTO" , "MARIA" , "JORGE" , "SOLEDAD" , "ANDRES" , "JUAN" , "ROBERTO" , "MARIA" , "JORGE" , "SOLEDAD" , "ROBERTO" , "MARIA" , "JORGE" , "SOLEDAD" , "ANDRES" , "JUAN" , "ROBERTO" , "MARIA" , "JORGE" , "SOLEDAD" , "ROBERTO" , "MARIA" , "JORGE" , "SOLEDAD" , "ANDRES" , "JUAN" , "ROBERTO" , "MARIA" , "JORGE" , "SOLEDAD" , "ROBERTO" , "MARIA" , "JORGE" , "JORGE" , "JORGE" , "MARIA" , "MARIA" , "ROBERTO" , "ROBERTO", "MARIA" , "ROBERTO"]
baseDeHoras = [3 , 5 , 6 , 4 , 5 , 4 , 3 , 4 , 4 , 4 , 6 , 4 , 4 , 5 , 3 , 4 , 5 , 7 , 4 , 4 , 3 , 6 , 4 , 4 , 6 , 3 , 5 , 3 , 5 , 6 , 6 , 3 , 4 , 5 , 5 , 7 , 5 , 3 , 4 , 5 , 5]
baseDeAviones = ["SESSNA" , "PETREL" , "PIPER" , "PIPER" , "SESSNA" , "PETREL" , "SESSNA" , "PETREL" , "PIPER" , "PIPER" , "SESSNA" , "PETREL" , "PIPER" , "PIPER" , "SESSNA" , "PETREL" , "SESSNA" , "PETREL" , "PIPER" , "PIPER" , "SESSNA" , "PETREL" , "PIPER" , "PIPER" , "SESSNA" , "PETREL" , "SESSNA" , "PETREL" , "PIPER" , "PIPER" , "SESSNA" , "PETREL" , "PIPER" , "PIPER" , "PIPER" , "PETREL" , "PETREL" , "SESSNA" , "SESSNA", "PETREL" , "SESSNA"]
alumnosParaExamen = ['Alumno SUSANA listo para examen de piloto, con 44 horas de vuelo en avión CESSNA']


# Bloque de menú
#----------------------------------------------------------------------------------------------
while True:
    while True:
        print()
        print("---------------------------")
        print("MENÚ DEL SISTEMA           ")
        print("---------------------------")
        print("[1] Cargar horas de vuelo")
        print("[2] Sortear alumno para examen de piloto")
        print("[3] Consultar cantidad de vuelos realizados")
        print("[4] Consultar alumnos para examen de piloto")
        print("[0] Salir del programa")
        print()
        opcion = input("Seleccione una opción: ")
        if opcion in ("0","1","2","3","4"): # Sólo continua si se elije una opcion de menú válida
            break
        else:
            input("Opción inválida. Presione ENTER para volver a seleccionar.")
            
        
    if opcion == "0": # Opción salir del programa
        exit()

    elif opcion == "1":   # Cargar horas de vuelo
        cargarHorasDeVuelo(baseDeAlumnos , baseDeHoras , baseDeAviones)
        
    elif opcion == "2":   # Sortear alumno para examen de piloto
        
        sortearAlumnoParaExamen(baseDeAlumnos, baseDeHoras, baseDeAviones)
        
    elif opcion == "3":   # Consultar cantidad de vuelos realizados
        alumnosSinRepetir(baseDeAlumnos)
        # Este código va como ayuda para mostrar los alumnos que hay en la base -----------
        print("\nAlumnos sin sortear:")
        alumnosSinRepetir=[]
        [alumnosSinRepetir.append(e) for e in baseDeAlumnos if e not in alumnosSinRepetir]
        alumnosSinRepetir.sort()
        for alumno in alumnosSinRepetir:
            print(alumno)
        # Fin del código de ayuda ---------------------------------------------------------

        ...
        
    elif opcion == "4":   # Consultar alumnos para examen de piloto
        ...
        

    print()
    input("Presione ENTER para continuar.")


