####################################################

# Autores: Ander Lifeng Sola y Victoria Hadjieva

# Grado: Ingeniería Informática
# Asignatura: Informática
# Centro: Universidad Pública de Navarra; Campus de Arrosadía

# Fecha: Jv 27/11/2025
# Archivo: 2048.py
# Lenguaje: python
# Descripción: Proyecto fin de asignatura; este será el JUEGO 2048.

####################################################

##########      LIBRERIAS
from random import randint

##########      FUNCIONES
# 1. Mostrar e Inicializar
def mostrar_juego(tablero):  # Para mostrar la cuadrícula del juego 
    # Variables para el tamaño de la cuadrícula
    ancho = 6    
    alto = 3     

    # La línea horizontal que separa las filas del tablero
    linea_horizontal = '+' + '+'.join(['-' * ancho] * 4) + '+'

    salida = ''  # Se va guardando toda la cuadricula como texto

    for fila in tablero:
        salida += linea_horizontal + '\n' #'\n' es un salto de línea

        # Cada celda tiene 3 líneas de alto
        for i in range(alto):
            fila_impresa = '|'

            # Se recorre cada valor de la fila
            for valor in fila:

                if i == alto // 2:  # Línea central (donde va el número)
                    texto = '' if valor == 0 else str(valor)
                    texto_centrado = texto.center(ancho, ' ') #center. centra los valores simplifcando el programa
                    fila_impresa += texto_centrado + '|'
                else:
                    fila_impresa += ' ' * ancho + '|' 

            salida += fila_impresa + '\n'

    # La última línea horizontal
    salida += linea_horizontal

    # Se muestra la cuadricula 
    print(salida)

    # Devulevo la salida
    return salida

def iniciar_juego(): #Para iniciar el juego
    #Variables y Listas
    matriz_juego = [[], [], [], []] #Crearemos una matriz de 4x4
    tamaño_tablero = 4

    #Crear la matriz 4x4 con todos los elementos iguales a 0
    for fila in range(tamaño_tablero):
        for columna in range(tamaño_tablero):
            matriz_juego[fila].append(0)

    #Posiciones inicio (2 posiciones) 
    fila_1 = randint(0, 3)
    columna_1 = randint(0, 3)

    fila_2 = randint(0, 3)
    columna_2 = randint(0, 3)

    while fila_2 == fila_1 and columna_1 == columna_2: #Para no repetir las mismas posiciones
        fila_2 = randint(0, 3)
        columna_2 = randint(0, 3)

    #Dos números aleatorios (2 o 4)
    numero_nuevo_2 = siguiente_numero()
    numero_nuevo_1 = siguiente_numero()
    
    #En dos posiciones aleatorias distintas se ponen dos números aleatorios (2 o 4)
    matriz_juego[fila_1][columna_1] = numero_nuevo_1
    matriz_juego[fila_2][columna_2] = numero_nuevo_2
    
    return matriz_juego #Devuelvo el tablero de juego inicial (Una matriz 4x4)

# 2. Recoger datos antes de cambiar el tablero
def movimiento(): #Para coger el movimiento del usuario (este debe ser válido)
    #Variables
    tecla_valida = True #Empieza siendo True y lo verifica

    #Pido la nueva tecla al usuario
    tecla = input("Introduce el siguiente movimiento (a/w/s/d): ")

    if tecla != 'a' and tecla != 'w' and tecla != 's' and tecla != 'd':
        tecla_valida = False #Falso si la tecla no es válida

    while tecla_valida == False: #El bucle termina cuando la tecla es válida
        print("Introduce en MINÚSCULAS UNA de ESTAS letras (a, w, s, d): ")
        tecla = input("Introduce el siguiente movimiento (a/w/s/d): ")
        if tecla == 'a' or tecla == 'w' or tecla == 's' or tecla == 'd':
            tecla_valida = True #Falso si la tecla no es válida

    return tecla #Devuelve el siguiente movimiento (una tecla válida)

def siguiente_numero(): #Genera un nuevo número (2 o 4) aleatorio
    numero = randint(1, 10)

    if numero == 10: #Un 10% de probabilidades
        numero_aleatorio = 4
    else: #Un 90% de probabilidades
        numero_aleatorio = 2

    return numero_aleatorio #Devuelve un número aleatorio entre 2 y 4


def tablero_traspuesto(tablero):
    #lIstas
    tablero_nuevo = []

    #Cuerpo General
    for i in range(len(tablero)):
        nueva_fila = []

        for fila in tablero:
            nueva_fila.append(fila[i])
        
        tablero_nuevo.append(nueva_fila)

    return tablero_nuevo #Por columnas

def cambio_tablero_usuario(tablero, tecla): #Cambia el tablero de juego después del movimiento del usuario
    if tecla == 'a': #Si el jugador introduce la tecla 'a', habrá un cambio en columnas hacia la izquierda
        tablero = cambio_tablero_a(tablero)

    elif tecla == 'd':
        tablero = cambio_tablero_d(tablero)
    
    elif tecla == 's':
        tablero = cambio_tablero_s(tablero)

    else:
        tablero = cambio_tablero_w(tablero)
    
    return tablero #Devuelve el nuevo tablero con las filas o columnas cambiadas


def cambio_tablero_a(tablero): # #Cuando la tecla es 'a'
    for fila in range(len(tablero)):
        #Variables
        vector_fila = tablero[fila]
        nueva_fila = [0, 0, 0, 0] #Nueva fila llena de 0 para agregar los números del vector_fila
        pos = 0 #Donde estoy en la nueva_fila
        fusionado = False # Será True si el número ya se ha fusionado antes

        #Cuerpo general
        for elemento in vector_fila:
            if elemento != 0:
                if pos > 0 and nueva_fila[pos - 1] == elemento and not fusionado: #Un número igual a su anterior, y su anterior no se ha fusionado todavía
                    nueva_fila[pos - 1] = elemento * 2 # Fusionamos
                    fusionado = True #Este número ya se ha unido, no lo tocamos más

                else:
                    nueva_fila[pos] = elemento #Lo añadimos al siguiente hueco vacío
                    pos += 1
                    fusionado = False

        tablero[fila] = nueva_fila

    return tablero

def cambio_tablero_d(tablero): #Cuando la tecla es d
    for fila in range(len(tablero)):
        vector_fila = tablero[fila] 
        nueva_fila = [0, 0, 0, 0] #Nueva fila llena de 0 para agregar los números del vector_fila
        pos = 3 #Donde estoy en la nueva_fila (empezamos desde el final)
        fusionado = False

        #Cuerpo general
        for i in range(3, -1, -1):
            elemento = vector_fila[i]
            if elemento != 0:
                if pos < 3 and nueva_fila[pos + 1] == elemento and not fusionado: #Un número igual a su anterior, y su anterior no se ha fusionado todavía
                    nueva_fila[pos + 1] = elemento * 2 #Unimos
                    fusionado = True #Este número ya se ha unido, no lo tocamos más

                else:
                    nueva_fila[pos] = elemento #Lo añadimos al siguiente hueco vacío
                    pos -= 1
                    fusionado = False

        tablero[fila] = nueva_fila

    return tablero

def cambio_tablero_w(tablero): #Cuando la tecla es 'w'
    # Cambio filas-columnas
    tablero = tablero_traspuesto(tablero) #En vez de jugar con las columnas, si trasponemos el tablero, podemos jugar con filas, y eso ya lo hemos programado con 'a' y 'd'

    #Cuerpo General
    for fila in range(len(tablero)): #Como hemos traspuesto el tablero, hay que hacer lo mismo que con la tecla 'a', y volver a trasponer
        #Variables
        vector_fila = tablero[fila]
        nueva_fila = [0, 0, 0, 0] #Nueva fila llena de 0 para agregar los números del vector_fila
        pos = 0 #Donde estoy en la nueva_fila
        fusionado = False # Será True si el número ya se ha fusionado antes

        #Cuerpo general
        for elemento in vector_fila:
            if elemento != 0:
                if pos > 0 and nueva_fila[pos - 1] == elemento and not fusionado: #Un número igual a su anterior, y su anterior no se ha fusionado todavía
                    nueva_fila[pos - 1] = elemento * 2 # Fusionamos
                    fusionado = True #Este número ya se ha unido, no lo tocamos más

                else:
                    nueva_fila[pos] = elemento #Lo añadimos al siguiente hueco vacío
                    pos += 1
                    fusionado = False

        tablero[fila] = nueva_fila
    
    # Cambio columnas-filas de vuelta
    tablero = tablero_traspuesto(tablero) #Vuelvo atrasponer, y conseguimos el tablero original con las columnas desplazadas hacia arriba
    
    return tablero

def cambio_tablero_s(tablero): #Cuando la tecla es 's'
    # Cambio filas-columnas
    tablero = tablero_traspuesto(tablero) #En vez de jugar con las columnas, si trasponemos el tablero, podemos jugar con filas, y eso ya lo hemos programado con 'a' y 'd'
    
    #Cuerpo General
    for fila in range(len(tablero)): #Como hemos traspuesto el tablero, hay que hacer lo mismo que con la tecla 'd', y volver a trasponer
        vector_fila = tablero[fila] 
        nueva_fila = [0, 0, 0, 0] #Nueva fila llena de 0 para agregar los números del vector_fila
        pos = 3 #Donde estoy en la nueva_fila (empezamos desde el final)
        fusionado = False

        #Cuerpo general
        for i in range(3, -1, -1):
            elemento = vector_fila[i]
            if elemento != 0:
                if pos < 3 and nueva_fila[pos + 1] == elemento and not fusionado: #Un número igual a su anterior, y su anterior no se ha fusionado todavía
                    nueva_fila[pos + 1] = elemento * 2 #Unimos
                    fusionado = True #Este número ya se ha unido, no lo tocamos más

                else:
                    nueva_fila[pos] = elemento #Lo añadimos al siguiente hueco vacío
                    pos -= 1
                    fusionado = False

        tablero[fila] = nueva_fila

    # Cambio columnas-filas de vuelta
    tablero = tablero_traspuesto(tablero) #Vuelvo atrasponer, y conseguimos el tablero original con las columnas desplazadas hacia abajo

    return tablero


def cambio_tablero_aleatorio(tablero): #Después del cambio_tablero_usuario, introduzco el número aleatorio (siguiente_número)
    numero_nuevo = siguiente_numero() #Un número nuevo que se introducirá
    hay_hueco = hueco(tablero) #Comrpobar que hay hueco para el nuevo número

    #Posición aleatoria del nuevo número
    pos_col = randint(0, 3) 
    pos_fila = randint(0, 3)

    #Bucle que termina cuando la casilla aleatoria está vacía (se puede introducir un número nuevo)
    if hay_hueco:
        while tablero[pos_fila][pos_col] != 0:
            pos_col = randint(0, 3) 
            pos_fila = randint(0, 3)
    
        #En la casilla vacía aleatoria introducimos el número aleatorio (2 o 4)
        tablero[pos_fila][pos_col] = numero_nuevo

    return tablero #Devuelvo el tablero de juego con el nuevo número ya agregado

def copiar_tablero(tablero): #Una copia del tablero
    copia = []

    for fila in tablero:
        lista_fila = []
        for elemento in fila:
            lista_fila.append(elemento)
        copia.append(lista_fila)
    
    return copia

# 3. Función para terminar (Has perdido)
def hueco(tablero):
    hay_hueco = False

    for fila in tablero:
        if 0 in fila:
            hay_hueco = True
            break
    
    return hay_hueco

def hay_movimiento(tablero):
    terminado = True

    for fila in range(len(tablero)):
        if terminado:
            for columna in range(len(tablero)):
                if fila < 3:
                    if tablero[fila][columna] == tablero[fila + 1][columna]:
                        terminado = False
                        break
                if columna < 3:
                    if tablero[fila][columna] == tablero[fila][columna + 1]:
                        terminado = False
                        break

    return terminado

def pierdes(tablero):
    terminado = False
    if not hueco(tablero):
        terminado = hay_movimiento(tablero)
    
    return terminado

##########      FUNCIÓN GENERAL
def juego():
    #Variables
    tecla = ''
    terminado = False
    aux_tablero = []

    # A. Inicializar Juego
    print("______ BIENVENIDO AL JUEGO 2048 ______")
    print() #Visual

    tablero = iniciar_juego()
    mostrar_juego(tablero)
    print() #Visual
    
    # B. JUGAR
    while terminado == False:

        if pierdes(tablero):
            break

        tecla = movimiento()
        aux_tablero = copiar_tablero(tablero)
        tablero = cambio_tablero_usuario(tablero, tecla)

        if aux_tablero != tablero:
            tablero = cambio_tablero_aleatorio(tablero)

        mostrar_juego(tablero)

        print()
    
    # C. FIN
    print("______ HAS PERDIDO ______")

    
##########      JUGAR
juego()