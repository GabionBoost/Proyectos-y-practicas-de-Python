"""
Ejercicio 1
Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.
"""
print("Hello world!")

"""
Ejercicio 2
Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable 
y luego muestre por pantalla el contenido de la variable.
"""
variable = "Hello world 2"
print( variable )

"""
Ejercicio 3
Escribir un programa que pregunte el nombre del usuario en la consola 
y después de que el usuario lo introduzca muestre por pantalla la cadena 
¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.
"""
userName = input( "What is your name? " )
print( f"Hi { userName }" )

"""
Ejercicio 4
Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética
(3+2/2*5)**2
"""
arithmetic_operation = ( 3+2 / 2*5 ) ** 2
print( arithmetic_operation )

"""
Ejercicio 5
Escribir un programa que pregunte al usuario por el número de horas trabajadas 
y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
"""
userHourWorks = int( input( "How many hours did you work today? " ) )
priceHour = float( input( "How much is the hourly pay? " ) )

print( f"Your pay is { userHourWorks * priceHour }" )

"""
Ejercicio 6
Escribir un programa que lea un entero positivo, n, introducido por el usuario 
y después muestre en pantalla la suma de todos los enteros desde 1 hasta n.
"""
n = int( input( "Number: " ) )
su = n * ( n + 1 ) / 2

print( su )

"""
Ejercicio 7
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
calcule el índice de masa corporal y lo almacene en una variable, 
y muestre por pantalla la frase Tu índice de masa corporal es <imc> 
donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
"""
userWeight = int( input( "What is your weight? " ) )
userHeight = float( input( "What is your height? " ) )
bmi = userWeight / ( userHeight ** 2 )

print( f"Your body mass index is { round( bmi, 2 ) }" )

"""
Ejercicio 8
Escribir un programa que pida al usuario dos números enteros y muestre por pantalla 
la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos 
por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.
"""
n = int( input( "What is your divisor? " ) ) 
m = int( input( "What is your dividend? " ) )

c = n / m
r = n % m

print( f"Between { n } and { m } your quotient is { round( c ) } and your remainder { round( r ) }" )

"""
Ejercicio 9
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y 
el número de años, y muestre por pantalla el capital obtenido en la inversión.
"""
userAmount = float( input( "What is your amount? " ) )
interestYear = int( input( "What is the interest per year? " ) )
investmentTime = int( input( "What is the investment time? " ) )

userCapital = (( interestYear / 100 ) * userAmount * investmentTime) + userAmount

print( f"Your final capital is { round( userCapital ) }$" )

"""
Ejercicio 10
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
Suele hacer venta por correo y la empresa de logística les cobra por peso de cada 
paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada 
paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. 
Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido 
y calcule el peso total del paquete que será enviado.
"""
clownWeight = 112; clowns =  int( input( "How many Clowns were sold? " ) )
dollWeight = 75; dolls =  int( input( "How many Dolls were sold? " ) )
totalWeight = ( clowns * clownWeight ) + ( dolls * dollWeight )

print( f"The total weight shall be { totalWeight }g " )

"""
Ejercicio 11
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
Estos ahorros debido a intereses, que no se cobran hasta finales de año, 
se te añaden al balance final de tu cuenta de ahorros. 
Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, 
introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la 
cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.
"""
print( "Welcome, thanks for come to the Random Company, in this company we give you the 4% of you capital" )
userAmountInRC = float( input( "What is the amount to invest in Random Company? " ) )
companyInterest  = 0.04
firstYear = userAmountInRC * companyInterest * 1; secondYear = firstYear * 2; ThirdYear = firstYear * 3
print( f"You capital in the first year is { round( firstYear + userAmountInRC, 2 ) }$ ")
print( f"You capital in the second year is { round( secondYear + userAmountInRC, 2 ) }$ ")
print( f"You capital in the third year is { round( ThirdYear + userAmountInRC, 2 ) }$ ")

"""
Ejercicio 12
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. 
Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
Después el programa debe mostrar el precio habitual de una barra de pan, 
el descuento que se le hace por no ser fresca y el coste final total.
"""


