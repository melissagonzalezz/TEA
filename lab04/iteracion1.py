#Tendencias e Innovación en Tecnologia Agricola

contador=0
valor=0
while True:
    numero=input("introduzca el numero: ")
    if numero=="fin":
        break
    try:
        valor=valor+int(numero)
        contador=contador+1
    except:
        print("valor incorrecto")
print("la suma de los numeros es: ", valor)
print("el conteo de los numeros es: ", contador)
print("el promedio de los numeros es: ", valor/contador)