#21/11/2023
"""
coche = "audi"
print(coche == "subaru")  #False
print(coche == "audi")    #True

print(coche != "audi")          #False
print(coche != "mercedes")      #True


pizza = "Margarita"

print(pizza.lower() == "margarita")
print(pizza)
print(pizza == "Margarita")


numero = 25

print(numero == 25)       #true
print(numero == 30)        #false
print(numero <= 10)        #false
print(numero <= 58)        #true
print(numero >= 17)        #true
print(numero >= 45)        #false
print(numero < 24)         #false
print(numero < 26)         #true
print(numero > 20)         #true
print(numero > 43)         #false


n1 = 30
n2 = 24

print(n1 == 30 and n2 <= 48)      #true
print(n1 >= 16 and n2 != 23)      #true
print(n1 <=12 and n2 ==24)        #false

print(n1 == 39 or n2 <= 48)      #true
print(n1 >= 56 or n2 == 48)      #false
print(n1 <= 31 or n2 >= 56)      #true


menu = ("espaguetis", "ensaladilla", "lentejas", "michirones", "callos")
comida = "pepino"
kiko = "mierda"

print("tortilla" in menu)
print("lentejas" in menu)

if comida not in menu:
    print(f"{comida.title()} no está en el menu.")
    
if kiko in menu:
    print("muy bien")
else:
    print(f"Pero como va a haber {kiko.title()} en el menu?")


edad = 17

if edad >= 18:
    print("Tienes edad para votar!!!")
    print("Te has registrado para votar?")
else:
    print("Lo siento, eres joven para votar.")
    print("Registrate en cuanto cumplas 18")
    
# 23/11/2023

ingredientes_añadidos = []

if ingredientes_añadidos:
    for ingrediente_añadido in ingredientes_añadidos:
        print(f"Añade {ingrediente_añadido}.")
    print("\nTerminando de hacer tu pizza!!")
else:
    print("Estas seguro de que quieres una pizza básica?")

ingredientes = ["champiñones", "olivas", "pimiento verde", "pepperoni", "piña", 
                "extra queso"]
 
ingredientes_añadidos = ["champiñones", "patatas fritas", "extra queso"]

for ingrediente_añadido in ingredientes_añadidos:
    if ingrediente_añadido in ingredientes:
        print(f"Añadiendo {ingrediente_añadido}.")
    else:
        print(f"Lo siento no tenemos {ingrediente_añadido}")
print("\nTerminando de hacer tu pizza.")
"""

users = ["pedro", "javier", "maria", "Lucia", "admin", "antonio", "maikel"]

for user in users:
    if user == "admin":
        print("Hola Admin, ¿quieres ver un informe de estado?")

    else:
        print(f"Hola {user.title()}, gracias por volver a entrar.")

