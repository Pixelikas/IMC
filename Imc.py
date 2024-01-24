# Cria variáveis e recebe os valores digitados pelo usuário
peso = input ('Digite o seu peso (kg): ')
altura = input ('Digite a sua altura (m): ')

# Cálcula o IMC através da fórmula, utilizando arredondamento em duas casas
imc = round(float (peso) / (float (altura)**2), 2) 

# Mostra o IMC na tela para o usuário
print ('O seu IMC é',imc)

# Verifica se o IMC ficou na faixa abaixo do peso
if imc <= 18.5:
    
    # Mostra na tela mensagem indicando IMC baixo
    print ('Você está abaixo do peso!')

# Verifica se o IMC ficou na faixa adequada de peso
elif imc > 18.5 and imc <= 25:

    # Mostra na tela mensagem indicando IMC adequado
    print ('Você está com o peso adequado!\n')
    
# Caso o IMC não tenha ficado nas faixas de "abaixo" ou "adequado"
else:

    # Mostra na tela mensagem indicando IMC alto
    print ('Você está acima do peso!')