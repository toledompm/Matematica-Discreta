#declara a tabela como um vetor que contera as colunas
tabela = []

#recebe o numero de preposicoes
numPreposicoes = int(input())
#define a cardinalidade
cardinalidade = 2**numPreposicoes
#define o numero de falsos consecutivos como a cardinalidade
falsosConsecutivos = cardinalidade

for i in range(numPreposicoes):
    #divide o numero de falsos consecutivos pela metade
    falsosConsecutivos //= 2
    #declara o vetor da coluna
    coluna = []

    #enquanto o tamanho da coluna for menor que a cardinalidade
    while(len(coluna) < cardinalidade):
        #para i = 0; i < falsosConsecutivos   
        for i in range(falsosConsecutivos):
            #adicione 1 ao vetor coluna
            coluna.append(1)
        #para i = 0; i < falsosConsecutivos 
        for i in range(falsosConsecutivos):
            #adicione 0 ao vetor coluna
            coluna.append(0)

    #adicione a coluna a tabela
    tabela.append(coluna)

#para x = 0; x < cardinalidade
for x in range(cardinalidade):
    #defina o vetor linha
    linha = []
    #para z = todas colunas
    for z in tabela:
        #adicione o valor x da coluna z a linha
        linha.append(z[x])
    #escreva a linha
    print(linha)


