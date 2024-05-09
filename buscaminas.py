buscaminas = [['♡︎','♡︎','♡︎','♡︎','♡︎'],['♡︎','♡︎','♡︎','♡︎','♡︎'],['♡︎','♡︎','♡︎','♡︎','♡︎'],['♡︎','♡︎','♡︎','♡︎','♡︎'],['♡︎','♡︎','♡︎','♡︎','♡︎']]
import os 
contador = -1
def fnt_limpiar():
    os.system('cls')
    print('Autor: ✮ Keisy Murillo ✮')
    fnt_impresion_buscaminas()
    print('\n')

def fnt_impresion_buscaminas():
    for i in range(len(buscaminas)):
        for j in range(len(buscaminas[i])):
            print(buscaminas[i][j], end = ' ')
        print()
    
def fnt_agregar(x,y):
    if x == 0 and y == 0:
        buscaminas[x][y] = '✔'

    elif x == 0 and y == 1:
        buscaminas[x][y] = '✔'

    elif x == 0 and y == 2:
        buscaminas[x][y] = '✘'   
    
    elif x == 0 and y == 3:
        buscaminas[x][y] = '✔'

    elif x == 0 and y == 4:
        buscaminas[x][y] = '✘'

    elif x == 1 and y == 0:
        buscaminas[x][y] = '✘'

    elif x == 1 and y == 0:
        buscaminas[x][y] = '✘'

    elif x == 1 and y == 1:
        buscaminas[x][y] = '✔'

    elif x == 1 and y == 2:
        buscaminas[x][y] = '✘'

    elif x == 1 and y == 3:
        buscaminas[x][y] = '✘'

    elif x == 1 and y == 4:
        buscaminas[x][y] = '✔'

    elif x == 2 and y == 0:
        buscaminas[x][y] = '✘'

    elif x == 2 and y == 1:
        buscaminas[x][y] = '✘'

    elif x == 2 and y == 2:
        buscaminas[x][y] = '✔'

    elif x == 2 and y == 3:
        buscaminas[x][y] = '✘'

    elif x == 2 and y == 4:
        buscaminas[x][y] = '✘'

    elif x == 3 and y == 0:
        buscaminas[x][y] = '✔'

    elif x == 3 and y == 1:
        buscaminas[x][y] = '✔'

    elif x == 3 and y == 2:
        buscaminas[x][y] = '✔'

    elif x == 3 and y == 3:
        buscaminas[x][y] = '✘'

    elif x == 3 and y == 4:
        buscaminas[x][y] = '✘'

    elif x == 4 and y == 0:
        buscaminas[x][y] = '✔'

    elif x == 4 and y == 1:
        buscaminas[x][y] = '✘'

    elif x == 4 and y == 2:
        buscaminas[x][y] = '✘'

    elif x == 4 and y == 3:
        buscaminas[x][y] = '✔'

    elif x == 4 and y == 4:
        buscaminas[x][y] = '✘'

sw = True
while sw == True:
    fnt_limpiar()
    fnt_agregar(int(input('Fila: ')),int(input('Columna: ')))