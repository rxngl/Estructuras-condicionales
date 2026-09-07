print("COMPARACION DE TRES NUMEROS")

numero1 = float(input("Ingresa el primer numero: "))
numero2 = float(input("Ingresa el segundo numero: "))
numero3 = float(input("Ingresa el tercer numero: "))

if numero1 >= numero2 and numero1 >= numero3:
    mayor = numero1
elif numero2 >= numero1 and numero2 >= numero3:
    mayor = numero2
else:
    mayor = numero3

if numero1 <= numero2 and numero1 <= numero3:
    menor = numero1
elif numero2 <= numero1 and numero2 <= numero3:
    menor = numero2
else:
    menor = numero3

print("El numero mayor es:", mayor)
print("El numero menor es:", menor)
