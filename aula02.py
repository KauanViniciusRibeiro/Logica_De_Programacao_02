# Tipos de concatenação
# Concatenação com sinal (+)
num = int(input('Digite um número inteiro:'))

#não é possivel concatenar numero inteiro usando esse metodo, a menos que
# converta o numero inteiro em uma string
print('Ola, ' + str(num) +' . Seja bem-vindo!')
print(type(num))

#concatenação com a (,)
print('O numero digitando é:',num)

# Concatenção com sstring(f)
print(f'O numero digitando é: {num} usando a concatenação "f"')

div = num / 3
# Usando format para formatação numérica
#limitando a quantidade de casas decimais
print(f'O resultado da divisão é {div:.2f}')