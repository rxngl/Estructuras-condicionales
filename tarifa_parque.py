print("TARIFA DE ENTRADA AL PARQUE")

edad = int(input("Ingresa tu edad: "))

if edad < 0:
    print("La edad no es valida.")
elif edad < 12:
    print("El costo de entrada es: $50")
elif edad <= 17:
    print("El costo de entrada es: $80")
else:
    print("El costo de entrada es: $120")
