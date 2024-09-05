'''
- in
- insert
- append
- lista[indice] = valor substituido
- remove
- if else elif
'''

notas = []
print(30*'-', 'BOLETIM ESCOLAR' ,30*'-')
numero_usuario1 = int(input('Digite um numero: '))
notas.append(numero_usuario1)

numero_usuario2 = int(input('Digite um numero: '))
notas.append(numero_usuario2)

numero_usuario3 = int(input('Digite um numero: '))
notas.append(numero_usuario3)

numero_usuario4 = int(input('Digite um numero: '))
notas.append(numero_usuario4)

numero_usuario5 = int(input('Digite um numero: '))
notas.append(numero_usuario5)

# Len conta a quantidade de elementos dentro da lista
quantidade_notas = len(notas)

# sum ira somar todos os elementos da lista
soma = sum(notas)

media = soma / quantidade_notas

print(f'As notas são: {notas}')
print(f'A quantidade de notas: {quantidade_notas}')
print(f'A soma de todas as notas: {soma}')
print(f'A media é: {media}')

'''
    #TODO: Situação
    Aprovado >= 7
    Recuperção >= 5 
    Reprovado
'''
if media >= 7:
    print(f'Aprovado com media {media}')

elif media >= 5:
    print(f'Recuperação com media {media}')

else:
    print(f'Reprovado com media {media} ')