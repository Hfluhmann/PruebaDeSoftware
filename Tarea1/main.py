
 
# # append() function to push
# # element in the stack
# stack.append('a')
# stack.append('b')
# stack.append('c')
 
# print('Initial stack')
# print(stack)
 
# # pop() function to pop
# # element from stack in
# # LIFO order
# print('\nElements popped from stack:')
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
 
# print('\nStack after elements are popped:')
# print(stack)


def stackMenu(option):
  while (option != '1' and option != '2' and option != '3' and option != '4'):
    option = input(
      '''\nIngresa el numero de la opcion que deseas:
  1: Pushear de la pila.
  2: Popear de la pila.
  3: Ver pila.
  4: Volver.
  \nIngrese respuesta: ''')
    if (option != '1' and option != '2' and option != '3' and option != '4'):
      print('\n\nSelecciona una opcion correcta\n')
  return option

def stackManagment(stack):
  option = ''
  while option != '4':
    option = stackMenu(option)

    if option == '1':
      stack.append(input('Escribe el texto a agregar: '))
      option = ''

    elif option == '2':
      stack.pop()
      option = ''

    elif option == '3':
      print(stack)
      option = ''

  return

def menu(option):
  while (option != '1' and option != '2' and option != '3' and option != '4' and option != '5' and option != '6'):
    option = input(
      '''\nIngresa el numero de la opcion que deseas:
  1: Manejar la cola.
  2: Ver texto mas largo.
  3: Ver texto mas corto.
  4: Ver un texto.
  5: Comparar 2 textos.
  6: Salir.
  \nIngrese respuesta: ''')
    if (option != '1' and option != '2' and option != '3' and option != '4' and option != '5' and option != '6'):
      print('\n\nSelecciona una opcion correcta\n')
  return option


stack = []
option = ''
while option != '6':
  option = menu(option)

  if option == '1':
    stackManagment(stack)
    option = ''
    
  elif option == '2':
    max = 0
    maxWord = ''
    for element in stack:
      if len(element) > max:
        maxWord = element
        max = len(element)
    print('\n'+maxWord+'\n')
    option = ''

  elif option == '3':
    min = float('inf')
    minWord = ''
    for element in stack:
      if len(element) < min:
        minWord = element
        min = len(element)
    print('\n'+minWord+'\n')
    option = ''

  elif option == '4':
    selectedText = int(input('Selecciona el indice de la palabra a imprimir: '))
    print('\n'+stack[selectedText]+'\n')
    option = ''

  elif option == '5':
    if len(stack) >= 2:
      firstText = int(input('Selecciona el indice de la primera palabra: '))
      secondText = int(input('Selecciona el indice de la segunda palabra: '))
      if ( len(stack[firstText]) > len(stack[secondText]) ):
        print('\n'+stack[firstText]+' -> '+ str(len(stack[firstText])) + ' > '+stack[secondText]+' -> '+ str(len(stack[secondText])) +'\n')
      elif ( len(stack[firstText]) < len(stack[secondText]) ):
        print('\n'+stack[firstText]+' -> '+ str(len(stack[firstText])) + ' < '+stack[secondText]+' -> '+ str(len(stack[secondText])) +'\n')
      else:
        print('\n'+stack[firstText]+' -> '+ str(len(stack[firstText])) + ' = '+stack[secondText]+' -> '+ str(len(stack[secondText])) +'\n')

    else:
      print('No hay suficientes elementos para poder comparar')
    option = ''

print('Saliendo...')
