print("ola mundo")

#nome = 'kauan'
#idade = 25
#peso = 55.8
#altura = 1.80
#instrutor = True

# FIXME:Visualizando os tipos de dados

# FIXME:Entrada de dados

sobrenome =  input('Digite o seu sobrenome: ') 

print(type(sobrenome))

#convertendo o valor do input

idade = input('Digite sua idade: ')
idade = int(idade)
print(type(idade))

ano = int(input('em qual ano estamos: '))
print(type(ano))

if ano > 2024:
    print('dentro do if: ')