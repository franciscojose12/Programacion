"""
1.Crea un programa que genere 100 números de forma aleatoria y que posteriormente
ofrezca al usuario la posibilidad de:
a. Conocer el mayor
b. Conocer el menor
c. Obtener la suma de todos los números
d. Obtener la media
e. Sustituir el valor de un elemento por otro número introducido por teclado
f. Mostrar todos los números
⇒ Realiza cada una de las opciones con funciones.
⇒ Utiliza la función siguiente para generar números aleatorios (entre 0 y 1000).
"""
"""
def ConocerMayor(lista):
    mayor=lista[0]
    for i in lista:
        if i > mayor:
            mayor = i
    return mayor
def ConocerMenor(lista):
    menor=[100]
    for i in lista:
        if i<menor:
            menor=i
    return menor
def Suma(lista):
    suma=0
    for i in lista:
        if i>0:
            suma+=i                       
    return suma
"""
"""

"""

"""
2.Realiza un programa que lea 10 números, los imprima separados por coma y a
continuación los desplace una posición (y los muestre por pantalla desplazados), de
tal forma que el último pase a la primera posición, el primero a la segunda, el
segundo a la tercera, y así sucesivamente
"""

    



"""
3.realiza un programa que solicite la fecha como tres datos numéricos (día, mes y
año) y muestre a continuación la fecha en formato largo.
Introduce el día de la fecha: 15
Introduce el mes de a fecha: 3
Introduce el año de a fecha: 2009
La fecha en formato largo es 15 de Marzo de 2009
Debe validar los datos y ejecutarse hasta que se introduzca un día negativo.
"""
"""
def es_bisiesto(year):
    return (year%4==0 and (year%100!=0 or year%400==0))

def es_fecha_valida(d, m, y):
    dias_maximo_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    return (1<= d <= dias_maximo_por_mes[m-1]
            or (es_bisiesto(y) and m==2 and 1<=d<=29)
        )

def transformar_fecha(day, month, year):
    nombre_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    
    if es_fecha_valida(day, month, year):
    
        mes_largo = nombre_meses[month-1]
        resultado = f"{day} de {mes_largo} de {year}"
        
    else:
        resultado = "La fecha introducida es incorrecta."
        
    return resultado


dia     = int(input("Introduzca un día: "))
mes     = int(input("Introduzca un mes válido: "))
anyo    = int(input("Introduzca un mes válido: "))

while dia >= 0:
    print(transformar_fecha(dia, mes, anyo))
    
    dia     = int(input("Introduzca un día: "))
    mes     = int(input("Introduzca un mes válido: "))
    anyo    = int(input("Introduzca un mes válido: "))
"""
"""
4.Crea un programa que lea por teclado números de forma sucesiva y los guarde en
una lista; el proceso de lectura y guardado finalizará cuando metamos un número
negativo. En ese momento se mostrará el elemento mayor y los números pares.
"""
"""
fin="no"
lista=[]
while fin!="si":
    numero=int(input("Dime un numero"))
    lista.append(numero)
    if numero<0:
        fin="si"
    
def Obtener_elemento_mayor(lista):
    mayor=lista[0]
    for i in lista:
        if i > mayor:
            mayor = i
   
        
    return mayor


def numero_Pares(lista):
    par=[0]
    for i in lista:
        if i%2==0:
            par.append(i)
            
    return par
print(f"Los numeros pares son los siguente:{numero_Pares(lista)}")
print(f"El numero mayor es :{Obtener_elemento_mayor(lista)}")
"""

         
        
"""
5. Realiza una función reverse que reciba una lista y devuelva una nueva lista cuyo
contenido sea igual a la original pero invertida. Así, dada la lista [‘Di’, ‘buen’, ‘día’, ‘a’,
‘papa’], deberá devolver [‘papa’, ‘a’, ‘día’, ‘buen’, ‘Di’].
"""
"""
#Superimportante para futuro
lista=["Di","buen", "dia", "a" , "papa", "y" ,"a","mama"]
def Reverse(lista):
    invertida=[]
    for i in lista:
        invertida=[i] + invertida
    return invertida
        
print(Reverse(lista))
"""


"""
6. Diseña una función llamada estaOrdenada que reciba una lista de elementos y
devuelva True si está ordenada o False en caso contrario.
"""
"""
#Superimportante para futuro
lista=[1,2,3,4]
ordenada=True
def esta_Ordenada(lista):
    for i in range(0,len(lista)-1,1):
        if lista[i]>lista[i+1]:
            ordenada=False

    return ordenada
print(f"La {lista} esta ordenda:{ordenada}")
"""


"""
7. Escribir una función denominada encajan que indique si dos fichas de dominó
encajan o no. Las fichas son recibidas en dos cadenas de texto con el siguiente
formato
[3,4] [2,5]
"""
"""
MINIMO=0
MAXIMO=6
def es_valida(ficha):
    resultado=False
    if len(ficha)==5 and ficha[1] in "0123456" and ficha[3] in "0123456":
        resultado=True
    return resultado
ficha_1="[3,6]"
ficha_2="[5,3]"

if (es_valida(ficha_1) and es_valida(ficha_2)) and ficha_1[1]==ficha_2[1] or  ficha_1[1]==ficha_2[3] or ficha_1[3]==ficha_2[1] or  ficha_1[3]==ficha_2[3]:
    print("Encajan")
else:
    print("No encajan")
"""



"""  
8. Realiza un programa que añada números enteros a una lista hasta que se
introduzca un número negativo. Haciendo uso de esta lista, elabora funciones que
devuelvan:
a. una lista con todos los que sean primos.
b. el sumatorio
c. el promedio de los valores.
d. una lista con el factorial de cada uno de esos números.
"""
"""
fin="no"
lista=[]
while fin!="si":
    numero=int(input("Introduce numero:"))
    lista.append(numero)
    if numero<0:
        fin="si"
def Primos(lista):
    primo=[]
    for i in lista:         #acabar
        if i>2:
            for i in range(2,i):
                if i%i!=0:
                    primo.append(i)
                       
    return primo  
print(Primos(lista))       
def Sumatorio(lista):
    suma=0
    for i in lista:
        if i>0:
            suma+=i                       
    return suma
def Promedio_Valores(lista):

    suma=0
    for i in lista:
        if i>0:
            suma+=i
            promedio=suma/((len(lista)-1))
    return promedio

print(f"El sumatorio es:{Sumatorio(lista)}")
print(f"El promedio es:{Promedio_Valores(lista)} ")
"""

"""
9. Desarrolla un programa que a partir de una lista de números y un entero k, realice la
llamada a tres funciones: a) para devolver una lista de números con los menores de
k, b) otra con los mayores y c) otra con aquellos que son múltiplos de k.
"""
"""
numero=90

lista=[23,9,808,686,84,27,80,60,500,540]

def ObtenerMenor(lista):
    menores=[]
    for i in lista:
        if i<numero:
            menores.append(i)
    return menores
def ObtenerMayor(lista):
    mayores=[]
    for i in lista:
        if i>numero:
            mayores.append(i)
    return mayores

def ObtenerMultiplo(lista):
    multiplo=[] 
    for i in lista:
        if i%numero==0:
            multiplo.append(i)   
    return multiplo
print(f"{ObtenerMenor(lista)} Estos son los numeros Menores")
print(f"{ObtenerMayor(lista)} Estos son los numeros Mayores")
print(f"{ObtenerMultiplo(lista)} Estos son los numeros Multiplos")
"""

"""
10. Diseña una función conversor que convierta un número de binario a decimal o de
decimal a binario. Esta función recibirá un número en formato de cadena de texto
cuya última posición indica el sistema numérico utilizado (D-decimal, B-binario).
Debe validar la información, así, por ejemplo, el número ‘1020101B’ no sería válido
puesto que los valores en binario son 0 y 1.
"""
"""
11. Escribe una función intersect que reciba dos listas y devuelva otra lista con los
elementos que son comunes a ambas, sin repetir ninguno.
"""
"""
lista1=[1,7,287,37,9,372,950,27]
lista2=[4,9,950,8673,2,78,27,287]

def intersect(lista1,lista2):
    comunes=[]
    for i in lista1:
        for y in lista2:
            if i==y:
                comunes.append(i)
    return comunes
print(intersect(lista1, lista2))
"""

"""
12. Escribe una función unionListas que reciba dos listas y devuelva los elementos que
pertenecen a una, o bien, a la otra, pero sin repetir ninguno (unión de conjuntos).
"""
"""
lista1=[1,7,287,37,9,372,950,27]
lista2=[4,9,950,8673,2,78,27,287]
def unionLista(lista1,lista2):
    for i in lista1:
        for y in lista2:                       #acaba
          if i!=y:
            lista2.append(i)
    return lista2
print(unionLista(lista1, lista2))
"""

                

"""
13. Escribe una función que, dada una lista de nombres y una letra, devuelva una lista
con todos los nombres que empiezan por dicha letra. Debe validar los datos.
"""
"""
letra=str(input("Dime una letra"))    
lista=["Abel","Monica","Francisco","Adelina","Almudena","Jose"]

def unionLista(lista):                            
    union=[]
    for i in lista:
        if i[0]==letra:
            union.append(i)
    return union
print(unionLista(lista))
"""

    
    
"""
14. Escribe una función que, dada una lista de cadenas, devuelva la cadena más larga.
Si dos o más cadenas miden lo mismo y son las más largas, la función devolverá la
que tenga el mayor número de caracteres repetidos .
"""
"""
lista=["hoooolaaaaa","Holaquehaces","kjsju"]
def obtener_cadena_mayor(cad1,cad2):
    mayor=""
    if(len(cad1))>len(cad2):
        mayor=cad1
    elif len(cad1<len(cad2)):
        mayor=cad2
    else:
        
        
        
    return mayor
print(obtener_cadena_mayor(lista[0],lista[2]))
"""


