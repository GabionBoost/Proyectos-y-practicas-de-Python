"""
Ejercicio 1
Escibir un programa que pregunte el nombre del usuario en la consola y un numero entero e imprima por pantalla
en lineas distintas el nombre del usuario tantas veces como el numero introducido.
"""
userName = input( "What is your name? " )
numberPerName = int( input( "How many numbers do you repite your name? " ) )

for number in range(numberPerName):
    print( userName, end="\n" ) 

"""
Ejercicio 2
Escribir un programa que pregunte el nombre completo del usuario en la consola y despues muestre por pantalla
el nombre completo del usuario tres veces, una con todas las letras minusculas, otra con todas las letras mayusculas
y otra solo con la primera letra del nombre y de los apellidos en mayuscula. El usuario puede introducir su nombre
combinando mayusculas y minusculas como quiera.
"""
userName = input( "What is your complete name? " )

print( f"Hello, {userName.lower()}" )
print( f"Hello, {userName.upper()}" )
print( f"Hello, {userName.capitalize()}" )

"""
Ejercicio 3
Escribir un programa que pregunte el nombre del usuario en la consola y despues de que el usuario lo introdusca
muestre por pantalla "<Nombre> Tiene <Cantidad> de Letras", donde <Nombre> en el nombre de usuario en mayusculas
y <Cantidad> es el numero de letras que tiene <Nombre>.
"""
userName = input( "What is your name? " )
lettersInUserName = 0

for letters in range(len(userName)):
    lettersInUserName += 1
   
print( f"{userName} have {lettersInUserName} letters." )

"""
Ejercicio 4
Los telefonos de una empresa tienen el siguiente formato <prefijo-numero-extension> donde el prefijo es el codigo
del pais <+34>, y la extension tiene dos digitos. Ejemplo <+34-123456789-56>. Escribir un programa que pregunte por
un numero de telefono con este formato y muestre por pantalla el numero de telefono sin el prefijo ni la extension.
"""
numberOfPhone = input( "Enter your phone number: " )

print( f"Your number is {numberOfPhone[4:-3]}" )

"""
Ejercicio 5
Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.
"""
phrase = input( "Enter a phrase: " )

print( phrase[::-1] )

"""
Ejercicio 6
Escribir un programa que pida al usuario que introdusca una frase en la consola y una vocal, y despues muestre por pantalla
la misma frase pero con la vocal introducida en mayuscula.
"""
phrase = input( "Enter a phrase: " )
vowel = input( "Enter a vowel: " )

print( phrase.replace( vowel, vowel.upper() ) )

"""
Ejercicio 7
Escribir un programa que pregunte el correo electronico del usuario en la consola y muestre por pantalla otro correo
electronico con el mismo nombre (la parte delante de la arroba@) 
"""
email = input( "Enter your email: " )

print( email.replace( email[email.find("@"):], "@ceu.ar" ) )

""" 
Ejercicio 8 
Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla
el numero de euros y el numero de centimos del precio.
"""
priceOfProduct = input( "Enter a price with decimals: " ) 
cents = priceOfProduct[ priceOfProduct.find(".") + 1:]
price = priceOfProduct[ :priceOfProduct.find(".")]

print( f"Your price have {price} with {cents} cents of dollar" )

"""
Ejercicio 9
Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla,
el dia, el mes y el eño. Adaptar el programa anterior para que funcione cuando el dia y/o el mes se introduzca 
con un solo caracter
"""
userBirthday = "4/6/2033"

day = userBirthday[:userBirthday.find("/")]
year_month = userBirthday[userBirthday.find("/")+ 1:]
year = year_month[year_month.find("/")+ 1:]
month = year_month[:year_month.find("/")] 
 
print( f"Your birthday is the {day} of the {month} of the year {year}" )

"""
Ejercicio 10
Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas,
y muestre por pantalla cada uno de los productos en una linea distinta.
"""
products_basket = input( "Enter products Separated by commas: " )

for word in products_basket.split(","):
    print(word)

"""
Ejercicio 11
Escribir un programa que pregunte el nombre de un producto, su precio y un numero de unidades y muestre por
pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 digitos enteros
y 2 decimales, el numero de unidades con tres digitos y el coste total con 8 digitos enteros y 2 decimales
"""
productName = input( "Enter product:" )
productPrice = float( input( "Enter price: " ) )
numberOfUnits = int( input( "Enter Number of units: " ) )

print( f"Your product {productName} has the price of {round(productPrice, 2)}$"
      ,f"and you take {round(numberOfUnits,2)}, the total will be { round( productPrice * numberOfUnits , 2 )}$"   )

"""
Estos ejercicios son sacados de la pagina de https://aprendeconalf.es/
"""




