edad = int(input("Introduce tu edad: "))

if edad < 2:
    print("Eres un bebé.")
elif edad > 2 and edad < 4:
    print("Eres un infante.")
elif edad >= 4 and edad < 13:
    print("Eres un niño.")
elif edad >= 13 and edad < 20:
    print("Eres un adolescente.")
elif edad >= 20 and edad < 65:
    print("Eres un adulto.")
else:
    print("Eres un anciano.")

