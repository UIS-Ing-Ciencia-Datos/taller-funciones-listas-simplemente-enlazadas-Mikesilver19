class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def Imprimir(cabeza):
  actual = cabeza
  while actual:
    print(actual.data, end="->")
    actual = actual.next
  print()

def AgregarAlInicio(cabeza, nuevo_nodo):
    nuevo_nodo.next = cabeza
    return nuevo_nodo

def Eliminar(cabeza, data): 
  if cabeza is None:
    return None
  if cabeza.data == data:
    return cabeza.next
  actual = cabeza
  while actual.next and actual.next.data != data:
    actual = actual.next
  if actual.next is None:
    return cabeza
  actual.next = actual.next.next
  return cabeza

def BuscarPosicion(cabeza, dato): #Ingresa data devuelve posicion :D
    actual = cabeza
    posicion = 1
    while actual:
        if actual.data == dato:
            return posicion
        actual = actual.next
        posicion += 1
    return -1

    
def EliminarPorPosicion(cabeza, posicion):
    if cabeza is None:
        return None
    if posicion == 1:
        return cabeza.next
    actual = cabeza
    contador = 1
    while actual and contador < posicion - 1:
        actual = actual.next
        contador += 1
    if actual is None or actual.next is None:
        return cabeza
    actual.next = actual.next.next
    return cabeza

Cedula= None
HabitacionesDisponibles = None
habitacionesOcupadas = None
Nombre = None
opcion=0
Habitaciones = input("Ingrese el numero de habitaciones: ")
for i in range(int(Habitaciones)):
  HabitacionesDisponibles = AgregarAlInicio(HabitacionesDisponibles, Node(i+1))
while opcion != 4:
  print("\nOpciones:")
  print("1. Añadir un huesped")
  print("2. Consultar")
  print("3. Eliminar un huesped")
  print("4. Salir")
  opcion= int(input())
  if opcion == 1:
    nuevo_nodo = Node(input("Ingrese Numero de Cedula "))
    Cedula = AgregarAlInicio(Cedula, nuevo_nodo)
    nuevo_nodo = Node(input("Ingrese Nombre "))
    Nombre = AgregarAlInicio(Nombre, nuevo_nodo)
    a = 0
    while a == 0:
        nuevo_nodo = int(input("Ingrese Habitacion: "))
        actual = HabitacionesDisponibles
        encontrado = False
        while actual:
            if actual.data == nuevo_nodo:
                encontrado = True
                break
            actual = actual.next
        if encontrado:
            HabitacionesDisponibles = Eliminar(HabitacionesDisponibles, nuevo_nodo)
            habitacionesOcupadas = AgregarAlInicio(habitacionesOcupadas, Node(nuevo_nodo))
            a = 1
        else:
            print("Habitacion no disponible")

  if opcion == 2:
    print("1.Huespedes")
    print("2.Habitaciones")
    a=int(input())
    if a == 1:
      print("1.individual")
      print("2.Todos los Huespedes")
      b = int(input())
      if b == 2:
        Imprimir(Cedula)
        
    if a == 2:
      print("1.Habitaciones Disponibles")
      print("2.Habitaciones Ocupadas")
      b = int(input())
      if b == 1:
        Imprimir(HabitacionesDisponibles)
      if b == 2:
        Imprimir(habitacionesOcupadas)

  if opcion == 3:
      print("Digite la cedula del huesped a eliminar")
      a = input()
      posicion = BuscarPosicion(Cedula, a)
      if posicion == -1:
          print("Huesped no encontrado")
      else:
          Cedula = Eliminar(Cedula, a)
          Nombre = EliminarPorPosicion(Nombre, posicion)
          actual = habitacionesOcupadas
          contador = 1
          while actual and contador < posicion:
              actual = actual.next
              contador += 1
          if actual:
              HabitacionesDisponibles = AgregarAlInicio(HabitacionesDisponibles, Node(actual.data))
          habitacionesOcupadas = EliminarPorPosicion(habitacionesOcupadas, posicion)
