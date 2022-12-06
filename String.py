"""
1.Diseñe una función llamada caracteresEnCadena que tenga una cadena de caracteres y un carácter
como parámetros de entrada y devuelve cuántas veces aparece ese carácter en la cadena. Eso
debe hacerlo sin importar si la cadena y el carácter son minúsculas o mayúsculas.
"""
 
caracter=str(input("¿Que caracter quieres buscar?"))
cadena="as ideas que comunica un texto están contenidas en lo que se suele denominar «macroproposiciones», unidades estructurales de nivel superior o global, que otorgan coherencia al texto constituyendo su hilo central, el esqueleto estructural que cohesiona elementos lingüísticos formales de alto nivel, como los títulos y subtítulos, la secuencia de párrafos, etc. "
def caracteresEnCadena(cadena,caracter):
    contador=0
    for i in cadena:
        if i.upper()==caracter or i.lower()==caracter:
            contador+=1
    return contador
print(caracteresEnCadena(cadena,caracter))

"""
2. Diseñe una función llamada lowCaseInString que tenga una cadena de caracteres como parámetro,
el método debe devolver cuántos de esos caracteres son letras minúsculas
"""

cadena="jkHJJCJkldjsJgDF"

def lowCaseInString(cadena):
    contador=0
    for i in cadena:
        if i.islower()==True:
            contador+=1
    return contador
print(lowCaseInString(cadena))

"""
3. Diseña una función llamada upperCaseInString que tenga una cadena de caracteres como parámetro
y el método debe devolver cuántas son letras mayúsculas.
"""

cadena="jkHJJCJkldjsJgDF"
def upperCaseInString(cadena):
    contador=0
    for i in cadena:
        if i.isupper()==True:
            contador+=1
    return contador
print(upperCaseInString(cadena))

"""
4. Diseñe una función llamada númeroEnCadena que reciba una cadena de caracteres como
parámetro y devuelve cuántos de ellos son números.
"""

from curses.ascii import isdigit
cadena="hola8mañ09ana9089hayp887ruebakjkgjh5467838"
def numero_en_cadena(cadena):
    
    contador_numero=0
    for i in cadena:
        if isdigit(i)==True:
            contador_numero+=1
    return contador_numero
print(numero_en_cadena(cadena))

"""
5. Diseñe una función llamada palíndromo que tenga una cadena de caracteres como parámetro de entrada,
y devuelve True si es un palíndromo o False en otros casos. Una palabra es un palíndromo si
se puede leer igual de izquierda a derecha o de derecha a izquierda, ignorando los blancos. Por ejemplo:
"anilina" o "Dabale arroz a la zorra el abad" Para simplificar el problema, se puede suponer
que se utilicen caracteres simples, es decir, sin tildes ni diresis.
"""

palabra="ojo"

def palindromo(palabra):
    es=False      
    if  palabra==palabra[::-1]:
        es=True
    return es
print(palindromo(palabra))




"""
6.Realizar una función que busque una palabra escondida dentro de un texto. Por ejemplo,
si la cadena es “shybaoxlna” y la palabra que queremos buscar es “hola”, entonces si se
encontrará y deberá devolver True, en caso contrario deberá devolver False. Las letras
de la palabra escondida deben aparecer en el orden correcto en la cadena que la oculta:
shybaoxlna ⇒ hola: True
soybahxlna ⇒ hola: False
"""

def encontrar_palabra(frase,palabra_escondida):
    posicion=0
    for letra in frase:
        if posicion<len(palabra_escondida) and palabra_escondida[posicion]==letra:
            posicion+=1
    return posicion==len(palabra_escondida)
print(encontrar_palabra("shybaoxlna", "hola"))



"""
7. Diseñar una función que reciba como parámetro tres cadenas, la primera será una frase
y deberá buscar si existe la palabra que recibe como segundo parámetro y reemplazarla
por la tercera.
"""

frase="El partido lo juego de libero el domingo"
palabra_buscada="domingo"
palabra_reemplazar="sabado"

def reemplazar_palabra(frase,palabra_buscada,palabra_reemplazar):
    nueva_frase=""
    for i in frase:
        if i==palabra_buscada:
            palabra_buscada=palabra_reemplazar
      
        
    return 
print(reemplazar_palabra(frase, palabra_buscada, palabra_reemplazar))
        
"""
8. Diseñar una función que determine la cantidad de vocales diferentes, que tiene una
palabra o frase introducida por teclado. Por ejemplo, la cadena “Abaco”, devolvería 2.
"""

cadena="abacooi"
VOCALES="aeiou"
def cantidad_vocales(cadena):
    contador=""
    for i in cadena:
        if i.lower() in VOCALES and  i.lower() not in contador:
            contador+=i
            
      
    return len(contador)
print(cantidad_vocales(cadena))

"""
9. Crear una función que, tomando una cadena de texto como entrada, construya y
devuelva otra cadena formada de la siguiente manera: todas las consonantes estarán al
principio y todas las vocales al final de la misma, eliminando los blancos. Por ejemplo,
pasándole la cadena "curso de programacion", una posible solución sería
"crsdprgrmcnuoeoaaio’.
"""

VOCALES="aeiou"
CONSONANTES="bcdfghjklmnñpkrstvwyz"
cadena="curso de programacion"
def formar_cadena(cadena):
    cadena_vocales=""
    cadena_consonantes=""
    for i in cadena:
        if i in VOCALES:
            cadena_vocales+=i
        elif i in CONSONANTES:
            cadena_consonantes+=i
    return cadena_consonantes+cadena_vocales
print(formar_cadena(cadena))
        
"""
10. Escribir una función que devuelva el número de palabras que hay en una cadena que
recibe como parámetro. Ten en cuenta que entre dos palabras puede haber más de un
blanco. También al principio y al final de la frase puede haber blancos redundantes. Por
ejemplo, si la cadena es “He estudiado mucho”, debe devolver 3.
"""

def numero_palabras(cadena):
    resultado = len(cadena.split())
    return str(resultado)
print(numero_palabras("hola que haces jose manuel"))


