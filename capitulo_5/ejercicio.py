"""
coches = ['audi', 'bmw', 'subaru', 'toyota']

for coche in coches:
    if coche == 'bmw':
        print(coche.upper())
    else: 
        print(coche.title())

car = 'Audi'
car.lower() == 'audi'
print(car)


coche = 'subaru'
print("Es coche == 'subaru?? yo predigo que True")
print(coche == 'subaru')

print("\nEs coche == 'audi'? yo predigo que False")
print(coche == 'audi')

coche = 'seat'
print("\nEs coche == 'peugeot'? yo predigo que False")
print(coche == 'peugeot')
print("\nEs coche == 'seat'? yo predigo que True")
print(coche == 'seat')


edad = int(input("Cual es tu edad? "))

if edad < 4:
    precio = 0
elif edad < 18:
    precio = 25
elif edad < 65:
    precio = 40
elif edad >= 65:
    precio = 20

print(f"Tu entrada cuesta {precio} €")
"""

ingredientes_extras = ['champiñones', 'extra de queso', 'pepperoni']

if 'champiñones' in ingredientes_extras:
    print("Añadiendo Champiñones")
if 'alcaparras' in ingredientes_extras:
    print("Añadiendo Alcaparras") 
if 'extra de queso' in ingredientes_extras:
    print("Añadiendo Extra de Queso")   
if 'pepperoni' in ingredientes_extras:
    print("Añadiendo Pepperoni")

print("\nTerminando de hacer tu pizza")

