# Tendencias e Innovacion en Teccnologia Agricola (TEA)
contador = 0
valor = 0
minimo = 0
maximo = 0
primerNumero = True
while True:
    numero=input("introduzca un numero: ")
    if numero=="fin":
        break
    else:
        valor=valor+int(numero)
        contador=contador+1
    if (primerNumero):
        minimo = int(numero)
        maximo = minimo
        primerNumero = False
    else:
        if (int(numero) > maximo):
            maximo = int(numero)
        if (int(numero) < minimo):
            minimo= int(numero)      
print("contador:", contador)
print("suma:" , valor)
print("promedio:", valor/contador)
print("maximo:" , maximo)
print("Minimo:" , minimo)