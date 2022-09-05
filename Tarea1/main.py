def menu(option):
  while (option != '1' and option != '2' and option != '3' and option != '4'):
    option = input(
      '''\nIngresa el numero de la opcion que deseas:
  1: Agragar texto.
  2: Ver texto mas largo y texto mas corto.
  3: Ver un texto.
  4: Comparar tamanio de 2 textos.
  \nIngrese respuesta: ''')
    if (option != '1' and option != '2' and option != '3' and option != '4'):
      print('\n\nSelecciona una opcion correcta;\n')
  return option

option = '0'
option = menu(option)

