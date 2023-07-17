"""
Ejercicio 1
Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor o menor de edad
"""
user_years_old = int(input("What is your age? "))
print( "You are a minor" ) if user_years_old < 18 else print( "You are of legal age" )

"""
Ejercicio 2
Escribir un programa que almacene la cadena de caracteres <contraseña> en una variable, pregunte al 
usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con
la guardada en la variable sin tener en cuenta mayusculas y minusculas. 
"""
password = "Contar1234"
password_check = input( "Enter password: " )

print( "Correct" ) if password_check.lower() == password.lower() else print( "Incorrect" )

"""
Ejercicio 3
Escribir un programa que pida al usuario dos numeros y muestre por pantalla su division. Si el
divisor es cero el programa debe mostrar un error.
"""
dividend = float( input( "Enter the dividend: " ) )
divisor = float( input( "Enter the divisor: " ) )

if divisor != 0:
    print( dividend / divisor )
else: 
    print( "ERROR" )

"""
Ejercicio 4
Escribir un programa que pida al usuario un numero entero y muestre por pantalla si es par o impar.
"""
number = int( input( "Enter a number: " ) )

print( "Your number is even" ) if number % 2 == 0 else print( "Your number is odd" )

"""
Ejercicio 5
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores
a 1000$ mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre
por pantalla si el usuario tiene que tributar o no.
"""
user_years_old = int(input("What is your age? "))
user_salary = int(input("What is your monthly salary? "))

if user_years_old > 16 and user_salary >= 1000:
    print( "You have to pay taxes" )
else: 
    print( "You do not have to pay taxes" )

"""
Ejercicio 6
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta 
formado por mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B
por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo
que le corresponde.
"""
user_name = input( "Enter your name: " )
user_gender = input( "Enter your gender (M, F) : " )

if user_name.lower() < "m" and user_gender.lower() == "f" or user_name.lower() > "n" and user_gender.lower() == "m":
    print( "You are in the group A" )
else: 
    print( "You are in the group B" )

"""
Ejercicio 7
Los tramos impositivos para la declaracion de la renta en un determinado pais son los siguientes:

                       |__________Renta__________|_____Tipo Impositivo_____|
                       |      Menos de 1000$     |            5%           |
                       |  Entre 10000$ y 20000$  |           15%           |
                       |  Entre 20000$ y 30000$  |           20%           |  
                       |  Entre 40000$ y 50000$  |           30%           |
                       |      Mas de 60000$      |           45%           |

Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla al tipo impositivo
que le corresponde.
"""
user_income_gain = int( input( "What is your annual income? " ))

if user_income_gain < 10000:
    print( "Your tax rate is 5%" )
elif user_income_gain < 20000:
    print( "Your tax rate is 15%" )
elif user_income_gain < 30000:
    print( "Your tax rate is 20%" )
elif user_income_gain < 50000:
    print( "Your tax rate is 30%" )
else:
    print( "Your tax rate is 45%" )

"""
Ejercicio 8
En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener
en la evaluacion comienzan en 0.0 y pueden ir aumentando, traduciendose en mejores beneficios. Los puntos 
que pueden conseguir los empleados pueden se 0.0, 0.4, 0.6 o mas, pero no valores intermedios entre los 
mensionados. A continuacion se muestra una tabla con los niveles correspondientes a cada puntuacion.
La cantidad de dinero conseguida en cada nivel es de 2400$ multiplicada por la puntuacion del nivel.

                        |____Nivel____|__Puntuacion__|  
                        | Inaceptable |     0.0      |
                        |  Aceptable  |     0.4      |
                        |  Meritorio  |     0.6      |
                        
Escribir un programa que lea la puntuacion del usuario e idique su nivel de rendimiento, asi como la cantida 
de dinero que recibira el usuario.
"""
points = float( input( "What is your score 0.0, 0.4, 0.6 or more?: " ) )
salary = 2400

if points == 0.0:
    print( f"Unacceptable level, your salary is: {salary}" )
elif points == 0.4:
    print( f"Acceptable level, your salary is: {salary * points + salary}" )
elif points >= 0.6:
    print( f"Meritorious level, your salary is: {salary * points +salary}" )


"""
Ejercicio 9
Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma
auto,atica el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del 
cliente y mostrar el precio de la entrada. Si el cliente es menor a 4 años puede entrar gratis, si tiene entre 
4 y 18 años debe pagar 5$ y si es mayor de 18 años, 10$.
"""
user_years_old = int( input( "What is your age?: " ) )

if user_years_old < 4:
    print( "Your entrance is free" )
elif user_years_old <= 18:
    print( "Your entrance costs: 5$" )
elif user_years_old > 18:
    print( "Your entrance costs: 10$" )

"""
Ejercicio 10
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada 
tipo de pizza aparecen a continuación.

* Ingredientes vegetarianos: Pimiento y tofu.
* Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta 
le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además 
de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida
es vegetariana o no y todos los ingredientes que lleva.
"""

print( "Welcome to Bella Napoli!!" )
type_of_pizza = input( "Do you want your pizza to be vegetarian? (Y/N): " ) 
pizza = [ "Bell Pepper", "Tofu" ]
vegetarian_pizza = [ "Pepperoni", "Ham", "Salmon" ]

if type_of_pizza.lower() == "y":
    print( "Select Ingredient: Pepperoni, Ham, Salmon" )
    selection = int(input("1, 2 or 3: "))
    print( f"Your vegetarian pizza has: {vegetarian_pizza[selection-1]}, mozzarella and tomato. enjoyment." )
else: 
    print( "Select Ingredient: Bell Pepper, Tofu" ) 
    selection = int(input("1 or 2: "))
    print( f"Your pizza has: {pizza[selection-1]}, mozzarella and tomato. enjoyment." )
    
"""
Estos ejercicios son sacados de la pagina de https://aprendeconalf.es/
"""