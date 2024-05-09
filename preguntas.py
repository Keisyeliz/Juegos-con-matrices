matriz = [['❄','❄','❄','❄','❄'],['❄','❄','❄','❄','❄'],['❄','❄','❄','❄','❄'],['❄','❄','❄','❄','❄'],['❄','❄','❄','❄','❄']]

correcto = '😃'
incorrecto = '👎'
list_preguntas= ['¿Qué es python?\n\n1. Juego\n2. Lenjuaje de programación\n3. Ninguna de las anteriores ',   '¿Qué es HTML?\n1. Lenguaje de maquetación\n2. Navegador\n3. Quesuda' ]
list_respuestas = ['2','1']

def fnt_impresion_matriz():
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end = '   ')
        print('\n')

contador = 0

for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            import os
            os.system('cls')
            fnt_impresion_matriz()
            print()
            print(list_preguntas[contador])
            print()
            r = input('-> ')
            if r == list_respuestas[contador]:
                matriz[i][j] = correcto
            else:
                matriz[i][j] = incorrecto
            contador += 1
