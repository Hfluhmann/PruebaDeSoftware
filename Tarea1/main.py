
def checkCorrectIndex(index, lenght):
  
  if index.isnumeric():
    index = int(index)
    if ( index >= 0 and index < lenght ):
      return True
    else:
      return False
  else:
    return False

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
  1: Manejar el Stack.
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
    if (len(stack) > 0):
      max = 0
      maxWord = ''
      for element in stack:
        if len(element) > max:
          maxWord = element
          max = len(element)
      print('\n'+maxWord+'\n')
    else:
      print('No hay elementos suficientes en la pila')
    option = ''

  elif option == '3':
    if (len(stack) > 0):
      min = float('inf')
      minWord = ''
      for element in stack:
        if len(element) < min:
          minWord = element
          min = len(element)
      print('\n'+minWord+'\n')
    else:
      print('No hay elementos suficientes en la pila')
    option = ''

  elif option == '4':
    if (len(stack) > 0):
      selectedText = input('Selecciona el indice de la palabra a imprimir (0, 1, 2, ...): ')
      valid = checkCorrectIndex(selectedText, int(len(stack)))
      while (not valid):
        print('selecciona una opcion valida')
        selectedText = input('Selecciona el indice de la palabra a imprimir (0, 1, 2, ...): ')
        valid = checkCorrectIndex(selectedText, int(len(stack)))
      selectedText = int(selectedText)
      print('\n'+stack[selectedText])
    else:
      print('No hay elementos suficientes en la pila')
    option = ''

  elif option == '5':
    if len(stack) >= 2:
      firstText = input('Selecciona el indice de la primera palabra (0, 1, 2, ...): ')
      valid = checkCorrectIndex(firstText, int(len(stack)))
      while (not valid):
        print('selecciona una opcion valida')
        firstText = input('Selecciona el indice de la palabra a imprimir (0, 1, 2, ...): ')
        valid = checkCorrectIndex(firstText, int(len(stack)))
      
      secondText = input('Selecciona el indice de la segunda palabra (0, 1, 2, ...): ')
      valid = checkCorrectIndex(secondText, int(len(stack)))
      while (not valid or firstText==secondText ):
        print('selecciona una opcion valida')
        secondText = input('Selecciona el indice de la palabra a imprimir (0, 1, 2, ...): ')
        valid = checkCorrectIndex(secondText, int(len(stack)))
      firstText = int(firstText)
      secondText = int(secondText)
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
