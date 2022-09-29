#Tendencias e Innovación en Tecnologia Agricola
def calculoSalario(Horas, Tarifa):
    MAX_HORAS_SEMANALES = 40
    horas_extra = 0
    horas_extra = Horas - MAX_HORAS_SEMANALES
    if (horas_extra > 0):
        pago = (MAX_HORAS_SEMANALES * Tarifa) + (horas_extra * (Tarifa * 1.5))
    else: 
        pago = (Horas * Tarifa)
    return pago

Horas = int(input("Ingrese la cantidad de Horas "))
Tarifa = float (input("Ingrese Tarifa: "))
Salario = calculoSalario (Horas , Tarifa)
print(Salario)