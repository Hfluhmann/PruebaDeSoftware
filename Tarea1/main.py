import os
import time
import logging
if os.path.exists("main.log"):
  os.remove("main.log")
logging.basicConfig(filename='main.log', encoding='utf-8', level=logging.DEBUG)

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
      answer = input('Escribe el texto a agregar: ')
      stack.append(answer)
      logging.info(f'{time.strftime("%H:%M:%S")} Se agrego {answer} al stack.')
      option = ''

    elif option == '2':
      if len(stack) > 0:
        removed = stack.pop()
        logging.info(f'{time.strftime("%H:%M:%S")} Se elimino {removed} del stack.')

      else:
        print('El stack esta vacio')
        logging.warning(f'{time.strftime("%H:%M:%S")} Se ha intentado sacar un elemento del stack, pero este esta vacio.')

      option = ''

    elif option == '3':
      print(stack)
      logging.info(f'{time.strftime("%H:%M:%S")} Se ha visualizado el stack: {stack}')
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
logging.info(f'{time.strftime("%H:%M:%S")} Se ha iniciado el programa')
while option != '6':
  option = menu(option)

  if option == '1':
    logging.info(f'{time.strftime("%H:%M:%S")} Se ha entrado a la seccion de manejo de stack')
    stackManagment(stack)
    logging.info(f'{time.strftime("%H:%M:%S")} Se ha salido de la seccion de manejo de stack')
    option = ''
    
  elif option == '2':
    logging.info(f'{time.strftime("%H:%M:%S")} Se ha entrado a la seccion de ver texto mas largo')
    if (len(stack) > 0):
      max = 0
      maxWord = ''
      for element in stack:
        if len(element) > max:
          maxWord = element
          max = len(element)
      print('\n'+maxWord+'\n')
      logging.info(f'{time.strftime("%H:%M:%S")} Se ha impreso el texto mas largo: {maxWord}')
    else:
      print('No hay elementos suficientes en la pila')
      logging.warning(f'{time.strftime("%H:%M:%S")} Se ha intentado visualizar el texto mas largo, pero el stack esta vacio.')
    option = ''

  elif option == '3':
    logging.info(f'{time.strftime("%H:%M:%S")} Se ha entrado a la seccion de ver texto mas corto.')
    if (len(stack) > 0):
      min = float('inf')
      minWord = ''
      for element in stack:
        if len(element) < min:
          minWord = element
          min = len(element)
      print('\n'+minWord+'\n')
      logging.info(f'{time.strftime("%H:%M:%S")} Se ha impreso el texto mas corto: {minWord}')
    else:
      print('No hay elementos suficientes en la pila')
      logging.warning(f'{time.strftime("%H:%M:%S")} Se ha intentado visualizar el texto mas corto, pero el stack esta vacio.')
    option = ''

  elif option == '4':
    logging.info(f'{time.strftime("%H:%M:%S")} Se ha entrado a la seccion de ver un texto')
    if (len(stack) > 0):
      selectedText = input('Selecciona el indice de la palabra a imprimir (0, 1, 2, ...): ')
      valid = checkCorrectIndex(selectedText, int(len(stack)))
      while (not valid):
        print('selecciona una opcion valida')
        selectedText = input('Selecciona el indice de la palabra a imprimir (0, 1, 2, ...): ')
        valid = checkCorrectIndex(selectedText, int(len(stack)))
      selectedText = int(selectedText)
      print('\n'+stack[selectedText])
      logging.info(f'{time.strftime("%H:%M:%S")} Se ha impreso el texto de la posicion {str(selectedText)}: {stack[selectedText]}')
    else:
      print('No hay elementos suficientes en la pila')
      logging.warning(f'{time.strftime("%H:%M:%S")} Se ha intentado visualizar el un texto, pero el stack esta vacio.')
    option = ''

  elif option == '5':
    logging.info(f'{time.strftime("%H:%M:%S")} Se ha entrado a la seccion de comparar 2 textos')
    if len(stack) >= 2:
      firstText = input('Selecciona el indice de la primera palabra (0, 1, 2, ...): ')
      valid = checkCorrectIndex(firstText, int(len(stack)))
      while (not valid):
        print('selecciona una opcion valida')
        firstText = input('Selecciona el indice de la palabra a imprimir (0, 1, 2, ...): ')
        valid = checkCorrectIndex(firstText, int(len(stack)))
      
      secondText = input('Selecciona el indice de la segunda palabra (0, 1, 2, ...): ')
      valid = checkCorrectIndex(secondText, int(len(stack)))
      while (not valid):
        print('selecciona una opcion valida')
        secondText = input('Selecciona el indice de la palabra a imprimir (0, 1, 2, ...): ')
        valid = checkCorrectIndex(secondText, int(len(stack)))
      firstText = int(firstText)
      secondText = int(secondText)
      if ( len(stack[firstText]) > len(stack[secondText]) ):
        print('\n'+stack[firstText]+' -> '+ str(len(stack[firstText])) + ' > '+stack[secondText]+' -> '+ str(len(stack[secondText])) +'\n')
        logging.info(f'{time.strftime("%H:%M:%S")} {stack[firstText]} es mas larga que {stack[secondText]} con {str(len(stack[firstText]))} vs {str(len(stack[secondText]))} caracteres')

      elif ( len(stack[firstText]) < len(stack[secondText]) ):
        print('\n'+stack[firstText]+' -> '+ str(len(stack[firstText])) + ' < '+stack[secondText]+' -> '+ str(len(stack[secondText])) +'\n')
        logging.info(f'{time.strftime("%H:%M:%S")} {stack[firstText]} es mas corta que {stack[secondText]} con {str(len(stack[firstText]))} vs {str(len(stack[secondText]))} caracteres')
      else:
        print('\n'+stack[firstText]+' -> '+ str(len(stack[firstText])) + ' = '+stack[secondText]+' -> '+ str(len(stack[secondText])) +'\n')
        logging.info(f'{time.strftime("%H:%M:%S")} {stack[firstText]} tiene el mismo largo que {stack[secondText]} con {str(len(stack[firstText]))} caracteres')
    else:
      print('No hay suficientes elementos para poder comparar')
      logging.warning(f'{time.strftime("%H:%M:%S")} Se ha intentado comparar el largo de 2 textos, pero no hay suficientes elementos en el stack: {stack}.')
    option = ''

print('Saliendo...')
logging.info(f'{time.strftime("%H:%M:%S")} Se ha salido del programa')

