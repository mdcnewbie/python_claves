#Programa para crear claves de manera aleatoria
#Maximiliano Daniel Chiecher - 2024

#Importamos la libreria random para utilizar sus funciones
import random

#Definimos listas con elementos para los distintos tipos de caracteres
dicminusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
dicmayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'N', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
dicespeciales = ['!', '"', '#', '$', '%', '&', '/', '(', ')', '=', '?', '¡']
dicnumericos = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#Inicializamos las variables con sus valores por defecto
diccionario = dicminusculas
contador = 0
clave = ""
restar = 0

print("Generador de claves aleatorias")

#Tomamos el datos de longitud y se comprueba si es una entrada válida
try:
    longitud = int(input('Longitud deseada: '))
except ValueError:
    print('Longitud invalida')
    exit()
if longitud < 1:
    print('Longitud invalida')
    exit()

#Tomamos el dato de incluir mayúsculas o no y se valida la entrada
mayusculas = input('Desea incluir mayúsculas? (S/N): ')
if mayusculas != 'S' and mayusculas != 's' and mayusculas != 'N' and mayusculas != 'n' :
    print('Entrada invalida')
    exit()

#Tomamos el dato de incluir caractéres especiales o no y se valida la entrada
especiales = input('Desea incluir caractéres especiales? (S/N): ')
if especiales != 'S' and especiales != 's' and especiales != 'N' and especiales != 'n' :
    print('Entrada invalida')
    exit()

#Tomamos el dato de incluir caractéres numéricos o no y se valida la entrada
numericos = input('Desea incluir caractéres numéricos? (S/N): ')
if numericos != 'S' and numericos != 's' and numericos != 'N' and numericos != 'n' :
    print('Entrada invalida')
    exit()

#Si se seleccionó incluir mayúsculas ya se genera un caracter de dicha lista y se mete en la clave.
#También se adiciona al diccionario de generación la lista de mayúsculas.
#Se incrementa el contador restar para indicar que ya se consumió un caractér de la longitud máxima definida.
#Luego se repite lo mismo para el caso de caracteres especiales y numéricos
if mayusculas == 'S' or mayusculas == 's' :
    diccionario = diccionario + dicmayusculas
    clave = clave + random.choice(dicmayusculas)
    restar += 1
if especiales == 'S' or especiales == 's' :
    diccionario = diccionario + dicespeciales
    clave = clave + random.choice(dicespeciales)
    restar +=1
if numericos == 'S' or numericos == 's' :
    diccionario = diccionario + dicnumericos
    clave = clave + random.choice(dicnumericos)
    restar +=1

#Se completa el resto de los caracteres de la clave con valores aleatorios en base al diccionario creado
while contador < (longitud-restar) :
    clave = clave + random.choice(diccionario)
    contador +=1

#Se ordena de manera aleatoria la clave para mezclar los caracteres generados arbitrariamente con los demás
#generados completamente al azar
clave_shuffled = ''.join(random.sample(clave, len(clave)))

#Finalmente se muestra la clave mezclada final
print(clave_shuffled)
exit()
