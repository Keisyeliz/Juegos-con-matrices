matriz = [['❄', '❄', '❄', '❄', '❄'],
          ['❄', '❄', '❄', '❄', '❄'],
          ['❄', '❄', '❄', '❄', '❄'],
          ['❄', '❄', '❄', '❄', '❄'],
          ['❄', '❄', '❄', '❄', '❄']]

correcto = '😃'
incorrecto = '👎'

list_preguntas = ['¿Qué es Python?\n\n1. Juego\n2. Lenguaje de programación\n3. Ninguna de las anteriores',
'¿Qué es HTML?\n\n1. Lenguaje de maquetación\n2. Navegador\n3. Quesuda',
'¿Cuál es el color del cielo en un día soleado? \n\n1. Rojo\n2. Azul\n3. Verde',
'¿Cuál es el animal que dice "muuu"?\n\n1. Perro\n2. Gato\n3. Vaca',
'¿Cuál es la fruta del árbol de manzanas?\n\n1. Peras\n2. Manzana\n3. Platano',
'¿Cuál es el día después del miércoles?\n\n1. Jueves\n2. Martes\n3. Viernes',
'¿Cuál es el lugar donde viven los peces?\n\n1. Océano\n2. Montaña\n3. Desierto',
'¿Cuál es el animal que dice "guau guau"?\n\n1. Oveja\n2. León\n3. Perro',
'¿Cuál es el nombre del planeta en el que vivimos?\n\n1. Marte\n2. Tierra\n3. Júpiter',
'¿Cuál es el color del tomate maduro?\n\n1. Verde\n2. Blanco\n3. Rojo',
'¿Cuál es la forma de la pelota?\n\n1. Cuadrado\n2. Triángulo\n3. Círculo',
'¿Cuál es el color de la nieve?\n\n1. Blanco\n2. Rojo\n3. Azul',
'¿Cuál es el animal que dice "miau"?\n\n1. Perro\n2. Gato\n3. Vaca',
'¿Cuál es el opuesto de grande?\n\n1. Pequeño\n2. Alto\n3. Ancho',
'¿Cuál es el nombre del objeto que usamos para escribir?\n\n1. Borrador\n2. Sacapuntas\n3. Lapiz',
'¿Cuál es el opuesto de día?\n\n1. Semana\n2. Mes\n3. Noche',
'¿Cuál es el nombre del objeto que usamos para cortar papel?\n\n1. Tijeras\n2. Regla\n3. Goma de borrar',
'¿Cuál es el color del arcoíris?\n\n1. Blanco\n2. Negro\n3. Multicolor',
'¿Cuál es el animal que dice "pío pío"?\n\n1. Pollo\n2. Pato\n3. Ganso',
'¿Cuál es el nombre del objeto que usamos para medir?\n\n1. Lapicero\n2. Regla\n3. Tigeras',
'¿Cuál es el nombre del objeto que usamos para pintar?\n\n1. Tijeras\n2. Pintura\n3. cartón',
'¿Cuál es el nombre del objeto que usamos para barrer?\n\n1. Escoba\n2. Trapeador\n3. Pala',
'Indica el opuesto de la palabra "vacío"\n\n1. Lleno\n2. Medio\n3. Hueco',
'Selecciona el nombre del objeto que usamos para ver de lejos\n\n1. Telescopio\n2. Microscopio\n3. Prismáticos',
'Selecciona el nombre del objeto que usamos para cortar carne\n\n1. Tenedor\n2. Cuchillo\n3. Cuchara'
]

list_respuestas = ['2','1','2','3','2','1','1','3','2','3','3','1','2','1','3','3','1','3','1','2','2','1','1','3','2']

def fnt_impresion_matriz():
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end = ' ')
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
