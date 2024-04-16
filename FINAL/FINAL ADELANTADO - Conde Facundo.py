"""
-----------------------------------------------------------------------------------------------
Título: FINAL ADELANTADO - Conde Facundo
Fecha: 07/12/2023
Autor: Conde Zabulanes Facundo
Descripción: Final adelantado de la materia: "Algoritmos y Estructuras de Datos I" del alumno Facundo Conde Zabulanes, estudiante de la carrera Licenciatura en Gestión de las Tecnologías de la Información
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS IMPORTADOS
#----------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def pedirEntero(_mensajeInput, _mensajeError):
    # Esta función sirve para pedir un valor y validar si es un múmero entero utilizando excepciones
    # Si no se ingresa nada o si se ingresa un valor que no se pueda convertir a un entero entonces
    # se debe mostrar el mensaje de error y volver a pedir el valor

    ##### DESARROLLA DESDE AQUI #####
    while True:
        try:
            valor = int(input(_mensajeInput))
            break
        except:
            print(_mensajeError)
    return valor

def nuevoPokemonCapturado(_path1, _path2):
    # Desarrollar una función que pida un número entero (a validar con pedirEntero) y que luego dentro de la función valide esté entre 1 y 151
    # Luego abrir el archivo llamado pokedex para capturar la linea con los datos de dicho pokemon y almacenarlo en cadenaCaracter
    # Finalmente abrir el archivo de capturados para agregar al final el nuevo pokemon capturado
    
    cadenaCaracter = "" # En esta cadena se concatenará el texto a cargar en el archivo
    mensajeInput = ""   # Variable modificable para utilizar como mensaje de entrada cada vez que se tenga que llamar a la función pedirEntero
    mensajeError = ""   # Variable modificable para utilizar como mensaje de error cada vez que se tenga que llamar a la función pedirEntero

    ##### DESARROLLA DESDE AQUI #####
    
    mensajeInput = "Ingresa el numero de pokedex del pokemon capturado:"
    mensajeError = "Error! El valor no es entero."
    signal = True

    while signal == True:
        nPokemon = pedirEntero(mensajeInput, mensajeError)
        while nPokemon > 151 or nPokemon < 1:
            print("Debes ingresar un número de Pokedex valido! [Primera generacion 1-151]")
            nPokemon = pedirEntero(mensajeInput, mensajeError)
            
        try:
            archivoC = open(_path2, mode = "r" , encoding = 'utf-8')
            
            capturado = 0
            for linea in archivoC:
                campos = linea.strip("\n").split(";")
                if campos[0] == str(nPokemon):
                    print("El pokemon", campos[1], "ya ha sido capturado!")        
                    capturado = 1
                    break
            
            if capturado == 0:
                signal = False
                
            
        except (FileNotFoundError, OSError) as detalle:
                print("Error al abrir el archivo:", detalle)

        finally:
            try:
                    archivoC.close()
            except:
                pass

    try:
        archivoP = open(_path1, mode = "r" , encoding = 'utf-8')
        
        for lineaP in archivoP:
            camposP = lineaP.strip("\n").split(";")
            if camposP[0] == str(nPokemon):
                cadenaCaracter = lineaP
                
    except (FileNotFoundError, OSError) as detalle:
        print("Error al abrir el archivo:", detalle)

    finally:
        try:
            archivoP.close()
        except:
            pass

    
    try:
        archivoC = open(_path2, mode = "a" , encoding = 'utf-8')
        archivoC.write(cadenaCaracter)
        print("Pokemon capturado!")

    except (FileNotFoundError, OSError) as detalle:
        print("Error al abrir el archivo:", detalle)    

    finally:
        try:
            archivoC.close()
        except:
            pass



def pokemonCapturadosPorTipo(_path2, _elementos):
    # Usar el archivo de capturados y la lista de elementos para, primero imprimir la lista de elementos, pedirle al usuario que escriba alguno de dichos elementos
    # Debe validarse que esté dentro de dicha lista y sino volver a pedirlo hasta que esté en la lista
    # Abrir el archivo de capturados para imprimir los nombres de los pokemon que sean de dicho elemento 
    
    ##### DESARROLLA DESDE AQUI #####
    for i in _elementos:
        print(i)

    print(" ")

    elemento = input("Elige un elemento:").capitalize()
    while elemento not in _elementos:
        print("Elige un elemento de la lista.")
        elemento = input("Elige un elemento:").capitalize()
        
    print(" ")
    
    try:
        archivoC = open(_path2, mode= "r" , encoding = 'utf-')
        for linea in archivoC:
            campos = linea.strip("\n").split(";")
            if campos[2] == elemento or campos[3] == elemento:
                print(campos[1])
                
    except (FileNotFoundError, OSError) as detalle:
        print("Error al abrir el archivo", detalle)
    
    finally:
        try:
            archivoC.close()
        except:
            pass

def pokemonCapturadosPorColor(_path2, _colores):
    # Usar el archivo de capturados y la lista de elementos para, primero imprimir la lista de colores, pedirle al usuario que escriba alguno de dichos colores
    # Debe validarse que esté dentro de dicha lista y sino volver a pedirlo hasta que esté en la lista
    # Abrir el archivo de capturados para imprimir los nombres de los pokemon que sean de dicho color 
    
    ##### DESARROLLA DESDE AQUI #####
    for i in _colores:
        print(i)
        
    print(" ")
    
    color = input("Elige un color:").capitalize()
    while color not in _colores:
        print("Elige un color de la lista.")
        color = input("Elige un color:").capitalize()
        
    print(" ")
    try:
        archivoC = open(_path2, mode= "r" , encoding = 'utf-')
        for linea in archivoC:
            campos = linea.strip("\n").split(";")
            if campos[4] == color:
                print(campos[1])
                
    except (FileNotFoundError, OSError) as detalle:
        print("Error al abrir el archivo", detalle)
        
    finally:
        try:
            archivoC.close()
        except:
            pass

def pokemonPorCapturar(_path1, _path2, _path3):
    # Deberás trabajar con los 3 archivos para conseguir que el archivo sinCapturar.txt contenga justamente los pokemon no capturados
    
    ##### DESARROLLA DESDE AQUI #####
    try:
        archivoP = open(_path1, mode = "r", encoding = 'utf-8')
        archivoC = open(_path2, mode = "r", encoding = 'utf-8')
        archivoN = open(_path3, mode = "w", encoding = 'utf-8')
        
        for lineaP in archivoP:            # Recorre la pokedex, comparando una linea con cada una del archivo de pokemon capturados.
            signal = 0                           # Determinando si ya esta en el archivo de capturados o no, para agregar la linea tal cual esta al archivo de no capturados.
            archivoC.seek(0)                 # Por cada cambio de linea de la pokedex, se reinicia el puntero del archivo de capturados para no dejarlo estático en el final del archivo.
            for lineaC in archivoC:
                if lineaP == lineaC:
                    signal = 1
                    break
                
            if signal == 0:
                camposN = lineaP
                archivoN.write(camposN)
                
    except (FileNotFoundError, OSError) as detalle:
        print("Error al abrir el archivo", detalle)
        
    finally:
        try:
            archivoP.close()
            archivoC.close()
            archivoN.close()
        except:
            pass
    
    

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
#-------------------------------------------------
# Inicialización de variables
#-------------------------------------------------
path1 = "pokedex.txt"  # IMPORTANTE!!!!! El path 1 debe enlazar con el archivo de la pokedex que NO modificaremos
path2 = "capturados.txt"  # IMPORTANTE!!!!! El path 2 contiene los pokemon que capturamos
path3 = "sinCapturar.txt"  # IMPORTANTE!!!!! El path 3 contiene los pokemon pendientes de capturar
# Las siguientes son listas de valores válidos para ciertos ingresos de datos
colores = ['Green','Red','Blue','White','Brown','Yellow','Purple','Pink','Gray','Black']
elementos =['Grass','Fire','Water','Bug','Normal','Poison','Electric','Ground','Fighting','Psychic','Rock','Ghost','Ice','Dragon']


#-------------------------------------------------
# Bloque de menú
#-------------------------------------------------
while True:
    while True:
        try:
            print()
            print("---------------------------")
            print("¡BIENVENIDO ENTRENADOR!    ")
            print("---------------------------")
            print("[1] Cargar Pokemon Capturado")
            print("[2] Mostrar Pokemon capturados por tipo")
            print("[3] Mostrar Pokemon capturados por Color")
            print("[4] Actualizar pendientes por capturar")
            print("---------------------------")
            print("[0] Salir del programa")
            print("---------------------------")
            print()
            opcion = int(input("Seleccione una opción: "))
            if opcion in range(0,5): # Sólo continua si se elije una opcion de menú válida
                break
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
        except ValueError:
            input("Opción inválida. Presione ENTER para volver a seleccionar.")

    if opcion == 0: # Opción: Salir del programa
        exit()
        
    elif opcion == 1:   
        nuevoPokemonCapturado(path1, path2) # Llama a la función que nos permite cargar un nuevo pokemon atrapado
        
    elif opcion == 2:   
        pokemonCapturadosPorTipo(path2, elementos) # Llama a la función que nos permite ver los pokemon capturados por elemento (Tipo 1)
        
    elif opcion == 3:   
        pokemonCapturadosPorColor(path2, colores) # Llama a la función que nos permite ver los pokemon capturados por color
        
    elif opcion == 4:
        pokemonPorCapturar(path1, path2, path3) # Llama a la función que sobreescribir el archivo con los pokemon pendientes de capturar
        
    print()
    input("Presione ENTER para volver al menú.")


# ULTIMA ACTUALIZACIÓN POR: Facundo Conde Zabulanes , 07/12/2023 a las 16:50.
