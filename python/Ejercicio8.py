

monto = float(input("Ingrese monto a invertir: "))
interes_anual = float(input("Ingrese el interes anual: "))
años = int(input("Ingrese numero de años: "))

capital = monto/(1+interes_anual)*años

print("El capital obtenido de la inversion es: ","{0:.2f}".format(capital))