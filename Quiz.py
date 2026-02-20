class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
class Node1:
  def __init__(self, data):
    self.data = data
    self.next = None
class Node2:
  def __init__(self, data):
    self.data = data
    self.next = None

def ImprimirListaHuespedes(cabeza):
  currentNode = cabeza
  while currentNode:
    print(f"\n",currentNode.data, end="->")
    currentNode = currentNode.next

def AgregarAlInicio(cabeza, nuevo_nodo):
    nuevo_nodo.next = cabeza
    return nuevo_nodo
    currentNode = currentNode.next
    nuevo_nodo.next = currentNode.next
    currentNode.next = nuevo_nodo
    return cabeza
def EliminarHuesped(cabeza, cedula):
  if cabeza.data == cedula:
    return cabeza.next

  currentNode = cabeza
  while currentNode.next and currentNode.next.data != cedula:
    currentNode = currentNode.next

  if currentNode.next is None:
    return cabeza

  currentNode.next = currentNode.next.next

  return cabeza
node1= Node(None)
habitaciones1 = Node1(None)
nombre1 = Node2(None)
opcion=0
Habitaciones = input("Ingrese el numero de habitaciones: ")
for i in range(int(Habitaciones)):
  habitaciones1 = AgregarAlInicio(habitaciones1, Node1(i+1))
  i=i+1
ImprimirListaHuespedes(habitaciones1)
while opcion != "4":
  print("\nOpciones:")
  print("1. Añadir un huesped")
  print("2. Consultar")
  print("3.Eliminar un huesped")
  print("4. Salir")
  opcion= input()
  if opcion == "1":
    nuevo_nodo = Node(input("Ingrese Numero de Cedula "))
    node1 = AgregarAlInicio(node1, nuevo_nodo)
    nuevo_nodo = Node(input("Ingrese Nombre "))
    nombre1 = AgregarAlInicio(nombre1, nuevo_nodo)
    nuevo_nodo = Node(input("Ingrese habitacion: "))
    habitaciones1 = EliminarHuesped(habitaciones1, nuevo_nodo)
  if opcion == "2":
    ImprimirListaHuespedes(node1)
    ImprimirListaHuespedes(nombre1)
    ImprimirListaHuespedes(habitaciones1)
  if opcion == "3":
    node1 = EliminarHuesped(node1, input("Ingrese Numero de Cedula "))
