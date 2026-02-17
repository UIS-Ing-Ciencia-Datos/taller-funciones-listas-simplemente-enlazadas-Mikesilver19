# ===========================================
# By: Nury Farelo - Estructuras Datos
# Name: Lista Simplemente Enlazada 
# ===========================================

# Clase Nodo
class Nodo:
	def __init__(self, data):
		self.data = data
		self.siguiente = None

# CLase Listas enlazada simple
class ListaSE:
	def __init__(self):
		self.cabeza = None
  
  	# Lista Vacia
	def vacio(self):
		if self.cabeza == None:
			print("Está vacia")
		else:
			print("Lista no vacia")

	# Agregar al inicio
	def agregarInicio(self, data):
		nuevo_nodo = Nodo(data)
		if self.cabeza is None:
			self.cabeza = nuevo_nodo
			return
		else:
			nuevo_nodo.siguiente = self.cabeza
			self.cabeza = nuevo_nodo

	def agregarFinal(self, data):
		nuevo_nodo = Nodo(data)
		if self.cabeza is None:
			self.cabeza = nuevo_nodo
			return
		actual = self.cabeza
		while actual.siguiente:
			actual = actual.siguiente
		actual.siguiente = nuevo_nodo
	
	def insertarAntesDe(self, X, data):
		actual = self.cabeza
		while actual is not None:
			if actual.data == X:
				actual=Nodo(data)
				actual.siguiente = X
				X=X.siguiente
				return
		
	def insertarAntes(self, X, data):
		if self.cabeza is None:
			print("Lista vacía")
			return

		if self.cabeza.data == X:
			nuevo = Nodo(data)
			nuevo.siguiente = self.cabeza
			self.cabeza = nuevo
			return

		actual = self.cabeza
		while actual.siguiente and actual.siguiente.data != X:
			actual = actual.siguiente

		if actual.siguiente is None:
			print("Elemento no encontrado")
		else:
			nuevo = Nodo(data)
			nuevo.siguiente = actual.siguiente
			actual.siguiente = nuevo

	def insertarDespues(self, X, data):
		actual = self.cabeza

		while actual and actual.data != X:
			actual = actual.siguiente

		if actual is None:
			print("Elemento no encontrado")
		else:
			nuevo = Nodo(data)
			nuevo.siguiente = actual.siguiente
			actual.siguiente = nuevo

	def eliminarPrimero(self):
		if self.cabeza is None:
			print("Lista vacía")
		else:
			self.cabeza = self.cabeza.siguiente

	def eliminarUltimo(self):
		if self.cabeza is None:
			print("Lista vacía")
			return

		if self.cabeza.siguiente is None:
			self.cabeza = None
			return

		actual = self.cabeza
		while actual.siguiente.siguiente:
			actual = actual.siguiente

		actual.siguiente = None

	def buscar(self, valor):
		actual = self.cabeza

		while actual:
			if actual.data == valor:
				return True
			actual = actual.siguiente

		return False
	
	def contar(self):
		contador = 0
		actual = self.cabeza

		while actual:
			contador += 1
			actual = actual.siguiente

		return contador

