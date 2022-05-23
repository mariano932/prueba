class Cuenta:

	def __init__(self,titular,cantidad):
		self.titular=titular
		self.cantidad=cantidad
	def mostrar(self):
		print("Nombre del usuario:"+self.titular+"\nSaldo disponible:"+str(self.cantidad))
	def ingresar(self,deposito):
		self.deposito=deposito
		if deposito>=0:
			self.cantidad+=self.deposito
			print("Se ingresó:"+str(self.deposito)+"$.Su monto total es:"+str(self.cantidad))
		else:
			print("Ingreso una cantidad negativa, no se realizará ninguna acción")
	def retirar(self,retiro):
		self.retiro=retiro
		self.cantidad-=self.retiro
		print("Se retiró:"+str(self.retiro)+"$. Su monto disponible es:"+str(self.cantidad))
contador=1
titular=input("Ingrese nombre:")
cantidad=int(input("Ingrese cantidad:"))
e = Cuenta(titular,cantidad)
e.mostrar()
while(contador!=2):
	seleccion=int(input("Seleccione que desea realizar:\nPresione 1 para ingresar dinero\nPresione 2 para retirar dinero\n"))
	if seleccion==1:
		cantidad=int(input("¿Qué cantidad desea ingresar?"))
		e.ingresar(cantidad)
	elif seleccion==2:
		cantidad=int(input("¿Qué cantidad desea retirar?"))
		e.retirar(cantidad)
	else:
		print("Opción erronea")
	contador=int(input("¿Desea realizar otra operación?\nPresione 1 para SI y 2 para NO:"))
