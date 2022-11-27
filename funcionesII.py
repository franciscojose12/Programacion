"""
1. Diseñe un método llamado computaFactorial que reciba un entero positivo y
devuelve el factorial para ese número. Si el número es negativo, el método debe
devuelve Ninguno.
"""

numero=5
def computaFactorial(numero):
    factorial=1
    if numero>0:
        for i in range(2,numero+1):
            factorial*=i
        return factorial
    else:
        None
print(computaFactorial(numero))

"""
2. Diseñe un método llamado esAñoBisiesto que reciba un número y devuelva Falso para
años comunes y True para años bisiestos. Usted puede saber que un año se considera
ser un año bisiesto si es divisible por 4, a menos que también sea divisible por 100. Un año no es un
año bisiesto si es divisible por 100 a menos que también sea divisible por 400.
"""

anyo=2024
def esAñoBisiesto(anyo):
    esBisiesto=False
    if (anyo%4==0 or anyo%100==0):
        esBisiesto=True
    return esBisiesto
print(esAñoBisiesto(anyo))


"""
3. Diseñe un método llamado computeDaysInMonth que devuelva el número de días para
el mes y el año que se reciben como argumentos. Puede utilizar el método
año bisiesto anterior. Si los valores no son válidos, el método debería devolver -1.

"""

def computeDaysInMonth(mes,anyo):
    dias=0
    if (mes>=1 and mes<=12) and (anyo>0):
        if mes in [1,3,5,7,8,10,12]:
            dias=31
        elif mes in [4,6,9,11]:
            dias=30
        else:
            if esAñoBisiesto(anyo)==True:
                dias=29
            else:
                dias=28
    else:
        dias=-1
    
    return dias
mes=int(input("Dime que mes(1-12):"))
anyo=int(input("Dime el año:"))
print(f"Tiene :{computeDaysInMonth(mes, anyo)} dias")

"""
4. Diseñe un método llamado getDayOfWeek que reciba una lista que contenga tres números enteros
(día, mes y año) y devuelve el día de la semana para esa fecha (lunes,
Martes Miércoles Jueves Viernes Sábado Domingo).
Puede usar el siguiente algoritmo para obtener un número entre 0 (domingo) y 6
(sábado) correspondiente al día de la semana para una fecha dada:
a = (14 - mes) / 12
y = año – un
m = mes + 12 * a – 2
d = (día + y + y/4 - y/100 + y/400 + (31*m)/12) mod 7
"""

lista=[]
dia=int(input("Dime el dia"))
if dia>=1 and dia<=31:
    lista.append(dia)
mes=int(input("Dime el mes"))
if mes>=1 and mes<=12:
    lista.append(mes)
anyo=int(input("Dime el año"))
if anyo>0 and anyo<9999:
    lista.append(anyo)
a = (14 - mes) / 12
y = anyo - a
m = mes + 12 * a - 2
d = int(dia + y + y/4 - y/100 + y/400 + (31*m)/12)%7
def getDayOfWeek(d):
    day=""
    if d==1:
        day="Lunes"
    elif d==2:
        day="Martes"
    elif d==3:
        day="Miercoles"
    elif d==4:
        day="Jueves"
    elif d==5:
        day="Viernes"
    elif d==6:
        day="Sabado"
    elif d==0:
        day="Domingo"

    return day
print(f"Si el dia es {dia} el mes {mes} y el año {anyo} dia correspondiente:{getDayOfWeek(d)}")

"""
6.Diseñe un método llamado getNumberOfDigits que reciba un número (puede ser
real, entero, positivo o negativo) y debe devolver el número de dígitos que contiene. Si
el parámetro no es válido, el método debería devolver Ninguno. Extender esta función a
otros sistemas numéricos (hexadecimal, decimal, binario, octal).
"""

numero=234
def getNumberOfDigits(numero):
    digito=len(str(numero))        
    return digito
print(getNumberOfDigits(numero))
numero2=234.90

   
"""
5. Diseñe un método llamado powerIt que reciba dos enteros y eleve el primero
número al segundo. Puede usar el producto o la recursividad y verificar los valores. Si
no se proporciona ningún exponente, el primer número se eleva a 0.
"""

def powerIt(base,exponente=0):
    if base>0 and exponente>=0:
        resultado=base**exponente
    else:
        resultado=None
    return resultado
print(powerIt(2,4))

"""
7. Diseñe un método llamado isPrime que reciba un número entero positivo mayor
que 0 como parámetro. El método debe devolver True si el número es primo o False si
no primo Si el parámetro no es válido, el método debe devolver Ninguno.
"""

numero=int(input("Dime un numero"))

def isPrime(numero):
    if numero>0:
        esPrimo=True
        if numero>2:
            for i in range(2,numero):
                if numero%i==0:
                    esPrimo=False
    
    else:
        esPrimo=None
    return esPrimo
print(isPrime(numero))

"""
8. Diseñe un método llamado solveSecondOrderEquation que reciba tres enteros
números positivos correspondientes a los coeficientes de una ecuación de segundo orden
(ax2+bx+c=0) y calcula sus posibles soluciones. Si los parámetros no son válidos, el
El método debe devolver Ninguno.
"""

a=int(input("Dime un numero"))
b=int(input("Dime un numero"))
c=int(input("Dime un numero"))
def solveSecondOrderEquation (a,b,c):
    if a>0 and b>0 and c>0:
        resultado=(b**2) - (4*c*a)
    else:
        None
    return resultado
print(solveSecondOrderEquation(a, b, c))

"""
9. Diseñe un método llamado getPrimeDivisors que reciba un número positivo como
parámetro y devuelve una lista que contiene sus divisores primos. Si el parámetro no es válido
"""

numero=int(input("Dime un numero"))
def getPrimeDivisors(numero):
    lista=[]
    listaDivisores=[]
    if numero>0:
        for i in range(2,numero):
            if numero%i==0:
                listaDivisores.append(i)
        for i in listaDivisores:
            if isPrime(i):
                lista.append(i)
    else:
        None
    return lista
print(getPrimeDivisors(numero))  

"""
10. Diseñe un método llamado isFriendNumber que reciba dos números positivos y
devuelve True si los números son amigos, False en caso contrario. dos numeros son
considerados amigos si la suma de sus divisores, excepto el número dado, es igual
al segundo y viceversa.
"""

numero1=int(input("Dime un numero"))
numero2=int(input("Dime un numero"))
def isFriendNumber(numero1,numero2):
    divisores1=0
    divisores2=0
    amigos=False
    if numero1>0 and numero2>0:
        for i in range(2,numero1):
            if numero1%i==0:
                divisores1+=i
        for i in range(2,numero2):
            if numero2%i==0:
                divisores2+=i
        if divisores1==divisores2:
            amigos=True
    else:
        None
    return amigos
print(isFriendNumber(numero1, numero2))
