"""
Ejercicio 1
Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
"""
word = input( "Enter a word: " )
for x in range( 0, 10 ):
    print( word )
    
"""
Ejercicio 2
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los 
años que ha cumplido (desde 1 hasta su edad).
"""
user_years_old = int( input( "Enter your age: " ))

for year in range(1, user_years_old+1):
    print( year )
    
"""
Ejercicio 3
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla 
todos los números impares desde 1 hasta ese número separados por comas.
"""
num = int( input( "Enter a number:" ) )

for x in range(1, num+1, 2):
    print(x, end=", ")
print("\n")
    
"""
Ejercicio 4
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla 
la cuenta atrás desde ese número hasta cero separados por comas.
"""
num = int( input( "Enter a number:" ) )

for x in range(num, -1, -1):
    print(x, end=", ")
print("\n")

"""
Ejercicio 5
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y 
el número de años, y muestre por pantalla el capital obtenido en la inversión 
cada año que dura la inversión.
"""
capital = int( input( "Enter your capital: " ))
annual_profit_percentage = int( input( "Enter the annual profit percentage: " ))
time_investment = int( input( "Enter the time investemnt: " ))

for x in range(1, time_investment+ 1 ):
    capital += annual_profit_percentage / 100 * capital * 1 
    print( round( capital, 2 ))

"""
Ejercicio 6
Escribir un programa que pida al usuario un número entero y muestre por pantalla un 
triángulo rectángulo como el de más abajo, de altura el número introducido.
  *
  **
  ***
  ****
"""
num = int( input( "Enter a num:" ))

for x in range(1, num+1):
    print(x * "*")
    
"""
Ejercicio 7
Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
"""
for x in range( 1, 11 ):
    for i in range( 1, 11 ):
        print(i * x, end="\t")
    print("")
    
"""
Ejercicio 8
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo 
rectángulo como el de más abajo.
1
31
531
7531
"""
num = int( input("Enter a number: "))

for i in range(1, num+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")

"""
Ejercicio 9
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
"""
password = "1234"

while True:
    verification = input( "Enter your password: " )
    if verification != password:
        print( "Incorrect, try again" )
        continue
    else: 
        print( "Correcto, welcome" )
        break
        
"""
Ejercicio 10
Escribir un programa que pida al usuario un número entero y muestre por pantalla 
si es un número primo o no.
"""
num = int( input("Enter a number: "))

while True:
    if num % 2 == 0:
        print("Your number is even")
        break
    else:
        print("Your number is odd")
        break

"""
Ejercicio 11
Escribir un programa que le pida al usuario una palabra y luego muestre por pantalla
una a una las letras de la palabra introducida empezando por la ultima
"""
phrase = input( "Enter a phrase: " )

for letter in phrase[::-1]:
    print(letter)

"""
Ejercicio 12
Escribir un programa que le pregunte al usuario una frase y una letra, y muestre el numero 
de veces que aparece la letra en la frase
"""
phrase = input( "Enter a phrase: " )
letter = input( "Enter a letter: " )
letter_in_phrase = 0

for l in phrase:
    if l == letter:
        letter_in_phrase += 1
    else: None
if letter_in_phrase >= 2:
    print(f"In your phrase exists {letter_in_phrase} letter's {letter}")
else:
    print(f"In your phrase exists {letter_in_phrase} letter {letter}")
"""
Ejercicio 13
Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario 
escriba "salir" que terminará.
"""
while True:
    repite_phrase = input( "Enter a phrase to repite 3 times: " )
    if repite_phrase.lower() != "salir":
        for x in range(0,3):
            print(repite_phrase)
        continue
    else:
        break

"""
Estos ejercicios son sacados de la pagina de https://aprendeconalf.es/
"""

