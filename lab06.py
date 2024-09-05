lista = []

nome1 = input('Digite um nome: ')
lista.append(nome1)

nome2 = input('Digite outro nome: ')
lista.append(nome2)

lista.sort()

if nome1 in lista:
  print(f'Sim, o {nome1} está adicionado na lista')
else:
  print(f'Não, o {nome1} não está na lista')

  num1 = 10
  num2 = 20

  if num1 > num2:
    print('É maior')
  else:
    print('É menor')
    if num1 < num2:
      print('É menor')
    else:
      print('É maior')
print('Fim do bloco if else')

