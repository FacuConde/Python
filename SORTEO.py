"""
-----------------------------------------------------------------------------------------------
Título:
Fecha:
Autor:
Descripción:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS IMPORTADOS
#----------------------------------------------------------------------------------------------
import random

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def cargarAmigos(amigos,apuestas):
    amigo="e"
    while True:
        amigo = input("Ingrese el nombre del nuevo participante:")
        while amigo.isalpha() == False:
            amigo = input("Error, ingrese letras para el nombre:")
        if amigo == "fin" or amigo == "FIN" or amigo == "Fin":
            break
        monto = int(input("Ingrese el monto que desea agregar a la apuesta:"))
        while monto <= 0:
            monto = int(input("El requisito para participar es agregar algo de dinero. Vuelve a intentarlo:"))
        amigos.append(amigo)
        apuestas.append(monto)

def sortear(amigos,apuestas):
    if len(amigos) < 4:
        print("Para realizar el sorteo debe haber como mínimo 4 participantes.")
    else:
        pozoAcumulado = sum(apuestas)
        premio1 = pozoAcumulado * 0.5
        premio2 = pozoAcumulado * 0.3
        premio3 = pozoAcumulado * 0.2
        print("El pozo acumulado es de: $", pozoAcumulado)
        for i in range(3):
            ganador = random.randint(0,(len(amigos)-1))
            if i == 0:
                print(amigos[ganador], "ganó el primer premio: $", premio1)
            elif i == 1:
                print(amigos[ganador], "ganó el segundo premio: $", premio2)
            else:
                print(amigos[ganador], "ganó el tercer premio: $", premio3)
            del amigos[ganador]
        amigos.clear()
        apuestas.clear()

def bajaAmigo(amigos, apuestas):
    if len(amigos) < 1:
        print("Error, la lista debe tener como mínimo un participante. (ENTER para continuar)")
    else:
        contador = 0
        for elemento in amigos:
            print(elemento,"pusó $", apuestas[contador],". Y está en la posición: [",contador,"].")
            contador += 1
        print("Tener en cuenta que al eliminar al jugador, tambien se elimina el monto agregado...")
        eliminado = int(input("Posición de la persona que quiere expulsar de la lista:"))
        while eliminado > (len(amigos)-1):
            eliminado = int(input("Error, debe ingresar una posición valida:"))     
        del amigos[eliminado]
        del apuestas[eliminado]

def subirApuesta(amigos, apuestas):
    if len(amigos) < 1:
        print("Error, la lista debe tener como mínimo un participante. (ENTER para continuar)")    
    else:
        contador = 0
        for elemento in amigos:
            print(elemento,"pusó $", apuestas[contador],". Y está en la posición: [",contador,"].")
            contador += 1   
        nuevaApuesta = int(input("Ingrese la posición de la persona que quiere modificar su apuesta:"))
        while nuevaApuesta > (len(amigos)-1):
            nuevaApuesta = int(input("Error, debe ingresar una posición valida:"))    
        montoNuevo = int(input("Ingrese el monto nuevo que desea agregar:"))
        while montoNuevo <= 0:
            montoNuevo = int(input("El monto mínimo para participar debe ser mayor a 0:"))
        apuestas[nuevaApuesta] = montoNuevo
          
#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
# Declaración de variables
#----------------------------------------------------------------------------------------------

_listaDeAmigos = []
_listaDeApuestas = []

# Bloque de menú
#----------------------------------------------------------------------------------------------
while True:
    while True:
        print()
        print("---------------------------")
        print("MENÚ DEL SISTEMA           ")
        print("---------------------------")
        print("[1] Cargar amigos al sorteo")
        print("[2] Sortear!")
        print("[3] Dar de baja un amigo")
        print("[4] Subir la apuesta!")
        print("[0] Salir del programa")
        print()
        ultimoItemMenu = 4
        opcion = int(input("Seleccione una opción: "))
        if opcion in range(0,ultimoItemMenu + 1): # Sólo continua si se elije una opcion de menú válida
            break
        else:
            input("Opción inválida. Presione ENTER para volver a seleccionar.")

    if opcion == 0: # Opción salir del programa
        exit()

    elif opcion == 1:   # Opción Cargar Amigos al sorteo
        cargarAmigos(_listaDeAmigos, _listaDeApuestas)
    elif opcion == 2:   # Sortear!
        sortear(_listaDeAmigos,_listaDeApuestas)
    elif opcion == 3:   # Dar de baja un amigo
        bajaAmigo(_listaDeAmigos,_listaDeApuestas)
    elif opcion == 4:   # Subir la apuesta!
        subirApuesta(_listaDeAmigos,_listaDeApuestas)

    print()
    input("Presione ENTER para continuar.")
