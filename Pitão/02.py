#Suponha que uma pessoa possa se aposentar pelo INSS caso atenda alguma das situações abaixo:
#• É do gênero masculino, possui pelo menos 65 anos e pelo menos 10 anos de contribuição.
#• É do gênero masculino, possui pelo menos 63 anos e pelo menos 15 anos de contribuição.
#• É do gênero feminino, possui pelo menos 63 anos e pelo menos 10 anos de contribuição.
#• É do gênero feminino, possui pelo menos 61 anos e pelo menos 15 anos de contribuição.
#Crie um programa que leia um caractere (‘M’ ou ‘F’), que representa o gênero de um indivíduo,
# e dois inteiros, que representam a idade e o tempo de contribuição. O programa deverá então imprimir
# “Aposentável” se o indivíduo atender uma das situações acima. Caso contrário, o programa deverá imprimir “Não Aposentável”.

print('=-=-=-=-= Simulação de Aposentadoria do INSS =-=-=-=-=')
nome = str(input('\nInforme seu nome: '))
idade = int(input('Informe sua idade: '))
genero = str(input('M ou F: ')).upper
tempo_contribuicao = int(input('Informe seu tempo de contribuição: '))

if genero == 'M' and idade >= 65 and tempo_contribuicao >= 10:
    print(f'Sr(a) {nome} você é Aposentável!')
else:
    print(f'Sr(a) {nome} você não é Aposentável!')