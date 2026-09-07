print("CLASIFICACIÓN DE TRIANGULOS")

lado1 = float(input("Ingresa la longitud del primer lado: "))
lado2 = float(input("Ingresa la longitud del segundo lado: "))
lado3 = float(input("Ingresa la longitud del tercer lado: "))

if lado1 == lado2 and lado2 == lado3:
    print("El triangulo es equilátero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("El triangulo es isósceles.")
else:
    print("El triangulo es escaleno.")
