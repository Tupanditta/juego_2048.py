# MENCIÓN IMPORTANTE

Este programa ha sido desarrollado en conjunto con una `AMIGA`; **Victoria Hadjieva**.

## 2048 - Lógica y Estructura

Este programa está basado en el juego del **2048**. El juego consta de un tablero 4x4, el cual el usuario controla el movimiento de filas/columnas con las teclas a,w,s,d.
El objetivo es ir sumando números hasta lograr el número final `2048`. 

### Arquitectura del Juego

Hemos dividido el programa en varias funciones, las cuales las hemos unificado posteriormente en una misma función general (`2048`). 
Dichas funciones tienen como fin general...

    --> Crear (inicializar) la partida, creando la tabla 4x4 y mostrandola.
    --> Recoger los datos, tanto del usuario (tecla a,w,s,d) como el número aleatorio (2 o 4).
    --> Cambiar el tablero de juego según los nuevos datos.
    --> Analizar el tablero para determinar cuando se acaba la partida (El jugador PIERDE o GANA)

### Flujo de Ejecución del Código

1. Inicio: El programa comienza creando un tablero vacío de 4x4 e inserta dos números aleatorios iniciales (2 o 4) en posiciones distintas.

2. Bucle de Partida: Se inicia el ciclo principal que se repite indefinidamente hasta que el jugador pierde.

      //// Verificaciones de Estado

            --> Verificación de Derrota: Antes del movimiento, se comprueba si quedan huecos libres o fusiones posibles.

                  % % Si no hay movimientos: El juego termina inmediatamente ("HAS PERDIDO").

                  % % Si es posible jugar: El turno continúa.

            --> Verificación de Victoria: Se revisa el tablero para ver si alguna casilla ha alcanzado el valor 2048.

                  % % Si existe: Se muestra un mensaje de "ENHORABUENA" (el juego permite seguir jugando).

      //// Turno del Jugador

            --> Entrada de Datos: Se solicita al usuario la dirección del movimiento (teclas 'w', 'a', 's', 'd').

            --> Validación: Se comprueba si la tecla introducida es válida.

                  % % Si no es válida: Se pide al usuario que repita la entrada hasta que sea correcta.

            --> Procesamiento: Se guarda una copia del tablero, se desplazan los números en la dirección elegida y se fusionan los iguales.

            --> Generación Aleatoria: Se compara el tablero resultante con la copia original.

                  % % Si hubo cambios (movimiento efectivo): Se genera un nuevo número aleatorio (2 o 4) en una casilla vacía.

                  % % Si no hubo cambios: No se genera número nuevo y se vuelve a pedir movimiento.

            --> Visualización: Se muestra el estado actualizado del tablero en la consola.

   
