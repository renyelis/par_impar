

print(".....................................................")
print("...............INGRESE UN NUMERO.....................")
print(".....................................................")

#input

x = int(input("Digite un numero:"))

#processing
r = (x % 2)

if r==0:
    msj= "PAR"

else:
    msj= "IMPAR"


#output
print("...............................................")
print("..................RESULTADOS...................")
print("...............................................")

print("el numero " + str(x) + " es: " + msj)