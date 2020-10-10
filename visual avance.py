#-*-coding: utf-8-*-
# Edgar Andrade, Septiembre 2018

# Visualizacion de tableros de ajedrez 3x3 a partir de
# una lista de literales. Cada literal representa una casilla;
# el literal es positivo sii hay un caballo en la casilla.

# Formato de la entrada: - las letras proposionales seran: 1, ..., 9;
#                        - solo se aceptan literales (ej. 1, ~2, 3, ~4, etc.)
# Requiere también un número natural, para servir de índice del tablero,
# toda vez que pueden solicitarse varios tableros.

# Salida: archivo tablero_%i.png, donde %i es un número natural

#################
# importando paquetes para dibujar
print("Importando paquetes...")
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
print("Listo!")

def dibujar_tablero(f, n):
    # Visualiza un tablero dada una formula f
    # Input:
    #   - f, una lista de literales
    #   - n, un numero de identificacion del archivo
    # Output:
    #   - archivo de imagen tablero_n.png

    # Inicializo el plano que contiene la figura
    fig, axes = plt.subplots()
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)

    # Dibujo el tablero
    step = 1./7
    tangulos = []
    # Creo los cuadrados claros en el tablero
    mn=0;
    pd=0;
    for re in range(48):
       if f[re+1]==1:
           
           tangulos.append(patches.Rectangle(*[(pd * step, mn * step), step, step],\
               facecolor='black'))
       pd=pd+1
       
       if pd>6:
            mn=mn+1
            pd=0
       
           
           
    tangulos.append(patches.Rectangle(*[(0 * step, 1 * step), step, step],\
              facecolor='blue'))
    tangulos.append(patches.Rectangle(*[(6 * step, 4 * step), step, step],\
              facecolor='blue'))
    # Creo las líneas del tablero
    for j in range(7):
        locacion = j * step
        # Crea linea horizontal en el rectangulo
        tangulos.append(patches.Rectangle(*[(0, step + locacion), 1, 0.005],\
                facecolor='black'))
        # Crea linea vertical en el rectangulo
        tangulos.append(patches.Rectangle(*[(step + locacion, 0), 0.005, 1],\
                facecolor='black'))

    for t in tangulos:
        axes.add_patch(t)

    
    #plt.show()
    fig.savefig("tablero_" + str(n) + ".png")
 

f={1:1, 2:1, 3:0,4:0, 5:1, 6:0,7:0, 8:0, 9:1, 10:0, 11:0, 12:1, 13:0,14:0, 15:0, 16:1,17:0, 18:0, 19:1,
   20:0, 21:0, 22:0, 23:1,24:0, 25:0, 26:1,27:0, 28:0, 29:0, 30:1, 31:0, 32:0, 33:1,34:0, 35:0, 36:0,37:1, 38:0, 39:0,
   40:1, 41:0, 42:0, 43:0,44:0, 45:0, 46:0,47:0, 48:0, 49:0
   }

dibujar_tablero(f,121)

