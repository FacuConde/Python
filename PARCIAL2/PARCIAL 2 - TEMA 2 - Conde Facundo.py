"""
-----------------------------------------------------------------------------------------------
Título: 2do PARCIAL - TEMA 2
Fecha: 23/11/2023
Autor: Conde Zabulanes Facundo
Descripción: Parcial 2 de la materia Algoritmos y Estructuras de Datos II.
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS IMPORTADOS
#----------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def diasEnElMes(_mes): 
    ##### FUNCION DADA. NO MODIFICAR #####
    # Esta función que ya está programada y devuelve la cantidad de días en el mes
    if _mes in(4,6,9,11):
        _dias = 30
    elif _mes == 2:
        _dias = 28
    else:
        _dias = 31 
    return _dias
    ##### FUNCION DADA. NO MODIFICAR #####


def pedirEntero(_mensajeInput, _mensajeError):
    # Esta función sirve para pedir un valor y validar si es un múmero entero utilizando excepciones
    # Si no se ingresa nada o si se ingresa un valor que no se pueda convertir a un entero entonces
    # se debe mostrar el mensaje de error y volver a pedir el valor
    ##### DESARROLLA DESDE AQUI #####
    while True:
        try:
            valor = int(input(_mensajeInput))
            break
        except ValueError:
            print(_mensajeError)
    return valor


def mostrarGuias(_pathGuias):
    # Esta función sirve simplemente para mostrar el listado de guías de turismo
    # Será llamada desde dentro de otras funciones justo antes que se solicite la selección de un guía
    # Mostrará el listado de guías de turismo para ayudar a la posterior carga de códigos
    ##### DESARROLLA DESDE AQUI #####
    try:
        archivoG = open(_pathGuias , mode = "r" , encoding= 'utf-8')
        print("GUÍAS DE TURISMO ---------")
        for linea in archivoG:
            print(linea)

    except (FileNotFoundError, OSError) as detalle:
        print("Error al abrir el archivo:", detalle)
    
    finally:
        try:
            archivoG.close()
        except:
            pass

def reservarDestino(_pathReservas, _pathGuias, _destinosTuristicos):
    # Esta función permite agregar reservas de destinos al archivo de texto (delimitado por tabulación)
    #
    # La estructura de registro en el archivo es la siguiente:
    # nombreTurista TAB diaReserva TAB mesReserva TAB destinoTuristico TAB codigoDeGuia
    # A saber:
    #   
    #   - nombreTurista : Es un string
    #   - diaReserva: Es un entero (utilizar pedirEntero), además validar aquí que no sea un número que se haya almacenado en diasOcupados
    #   - mesReserva: Es un entero (utilizar pedirEntero), además validar aquí que esté entre 1 y 12
    #   - destinoTuristico: Es un string
    #   - codigoDeGuia: Es un entero (utilizar pedirEntero)

    cadenaCaracter = "" # En esta cadena se concatenará el texto a cargar en el archivo
    mensajeInput = ""   # Variable modificable para utilizar como mensaje de entrada cada vez que se tenga que llamar a la función pedirEntero
    mensajeError = "Error! Código inválido, vuelva a intentar."   # Variable modificable para utilizar como mensaje de error cada vez que se tenga que llamar a la función pedirEntero
    diasOcupados = []   # Lista en donde almacenar los días con reserva asignada tomando los datos desde el archivo y para el mes ingresado 
    ##### DESARROLLA DESDE AQUI #####

    mostrarGuias(_pathGuias)
    codigosPermitidos = [100, 200, 300, 400, 500]
    mensajeInput = "Ingrese el codigo de Guía de Turismo [100 a 500]:"
    codigoGuia = pedirEntero(mensajeInput, mensajeError)
    while codigoGuia not in codigosPermitidos:
        print("Error! Código invalido, vuelva a intentar.")
        codigoGuia = pedirEntero(mensajeInput, mensajeError)
    

    mensajeInput = "Ingrese el mes de reserva:"
    mensajeError = "Error! Mes invalido, vuelva a intentar."
    mesReserva = pedirEntero(mensajeInput, mensajeError)
    while mesReserva > 12 or mesReserva < 1:
        print("Ingrese un mes válido!")
        mesReserva = pedirEntero(mensajeInput, mensajeError)

    try:
        archivoR = open(_pathReservas , mode = "r" , encoding = 'utf-8')
        for linea in archivoR:
            listaCampos = linea.strip('\n').split("\t")
            if int(listaCampos[4]) == codigoGuia and int(listaCampos[2]) == mesReserva:
                diasOcupados.append(int(listaCampos[1]))

    except (FileNotFoundError, OSError) as detalle:
        print("Error al abrir el archivo:", detalle)

    finally:
        try:
            archivoR.close()
        except:
            pass

    
    print()
    print("DÍAS OCUPADOS ---------")
    diasOcupados.sort()                     # MEJORA OPCIONAL, PARA LEER COMODAMENTE LOS DIAS OCUPADOS
    print(diasOcupados)
    print()

    mensajeInput = ("Ingrese el dia de reserva:")
    mensajeError = ("Error, día invalido o ya reservado, vuelva a intentar.")

    diasValidos = diasEnElMes(mesReserva)
    diaReserva = pedirEntero(mensajeInput, mensajeError)
    while diaReserva > diasValidos or diaReserva < 1 or diaReserva in diasOcupados:
        print(mensajeError)
        diaReserva = pedirEntero(mensajeInput, mensajeError)


    destino = input("Ingrese el destino turístico [ALTURAS, RIOS, SALINA, QUEBRADA]:").upper()
    while destino not in _destinosTuristicos:
        print("Error! Destino inválido, vuelva a intentar.")
        destino = input("Ingrese el destino turístico [ALTURAS, RIOS, SALINA, QUEBRADA]:").upper()
    
    nombreTurista = input("Ingrese el nombre del Turista:").upper()
    try:
        archivoR = open(_pathReservas, mode = "a" , encoding = 'utf-8')
        d = "\t"
        cadenaString = str(nombreTurista) + d + str(diaReserva) + d + str(mesReserva) + d + str(destino) + d + str(codigoGuia)
        archivoR.write(cadenaString + '\n')        

    except (FileNotFoundError, OSError) as detalle:
        print("Error al abrir el archivo:", detalle)

    finally:
        try:
            archivoR.close()
        except:
            pass

    print()
    print("Reserva cargada con éxito!")
    
        



    

def mostrarTuristasSegunGuia(_pathReservas, _pathGuias):
    ## Esta función muestra todos los turistas según un guía turístico ingresado

    turistas = set()  # AYUDA! Conjunto vacío preparado para cargar los turistas del guía seleccionado
    ##### DESARROLLA DESDE AQUI #####


    mensajeError = "Error! Código inválido, vuelva a intentar."
    mostrarGuias(_pathGuias)
    codigosPermitidos = [100, 200, 300, 400, 500]
    mensajeInput = "Ingrese el codigo de Guía de Turismo [100 a 500]:"
    codigoGuia = pedirEntero(mensajeInput, mensajeError)
    while codigoGuia not in codigosPermitidos:
        print("Error! Código invalido, vuelva a intentar.")
        codigoGuia = pedirEntero(mensajeInput, mensajeError)


    try:
        archivoR = open(_pathReservas , mode = "r" , encoding = 'utf-8')
        
        for linea in archivoR:
            campos = linea.strip('\n').split("\t")
            if int(campos[4]) == codigoGuia:
                turistas.add(campos[0])
            else:
                pass
        else:
            pass


    except (FileNotFoundError, OSError) as detalle:
        print("Error al abrir el archivo:", detalle)

    finally:
        try:
            archivoR.close()
        except:
            pass


    print()
    print("LISTADO DE TURISTAS ------------")
    print()
    for i in turistas:
        print(i , '\n' )


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
#-------------------------------------------------
# Inicialización de variables
#-------------------------------------------------
pathReservas = "T:/reservas.txt"  # IMPORTANTE!!!!! usa esta variable string para el path completo del archivo base de reservas
pathGuias = "T:/guias.txt"  # IMPORTANTE!!!!! usa esta variable string para el path completo del archivo base de guías turísticos
destinosTuristicos = ["ALTURAS", "RIOS", "SALINA", "QUEBRADA"]

#-------------------------------------------------
# Bloque de menú
#-------------------------------------------------
while True:
    while True:
        try:
            print()
            print("-------------------------------------------")
            print("MENÚ DEL SISTEMA")
            print("-------------------------------------------")
            print("[1] Reservar un Destino")
            print("[2] Mostrar Turistas según Guía")
            print("-------------------------------------------")
            print("[0] Salir")
            print("-------------------------------------------")
            print()
            opcion = input("Seleccione una opción: ")
            if opcion in ["0","1","2"]: # Sólo continua si se elije una opcion de menú válida
                break
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
        except ValueError:
            input("Opción inválida. Presione ENTER para volver a seleccionar.")

    if opcion == "0":
        exit()

    elif opcion == "1":  
        reservarDestino(pathReservas , pathGuias , destinosTuristicos)
        
    elif opcion == "2":   
        mostrarTuristasSegunGuia(pathReservas, pathGuias)

    print()
    input("Presione ENTER para volver al menú.")

    # ANOTACIÓN PARA DOCUMENTAR ÚLTIMA ACTUALIZACIÓN: 18:06 - 23/11/2023 - FACUNDO CONDE ZABULANES