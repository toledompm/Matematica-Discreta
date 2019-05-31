#lendo os elementos do conjunto
elementos = input("entre com os elementos do conjunto separados por um espaço.(ie: \'a A b 3\'):\n").split()
relacoes = []
while (True):
    #lendo relações
    entrada = input("entre com dois elementos que se relacionam, separados por um espaço.(ie: \'a a\')\nDigite 0 para sair:\n").split()
    if len(entrada) == 1:
        if entrada[0] == '0':
            break    
    if len(entrada) == 2:
        relacoes.append(entrada)

#montando a matriz
mat = {}
for linha in elementos:
    l = {}
    for coluna in elementos:
        l[coluna] = 0
    mat[linha] = l 

#inserindo as relações na matriz
for ele1,ele2 in relacoes:
    mat[ele1][ele2] = 1

#definindo o fecho
fecho = relacoes

#varrendo a diagonal principal da matriz
for elem in elementos:
    #se algum elemento da diagonal principal for 0, adicione-o ao fecho
    if mat[elem][elem] == 0:
        fecho.append([elem,elem])

#imprimindo o fecho
saida = []
for i in fecho:
    saida.append('({})'.format(','.join(i)))

print('Fecho Reflexivo: '+';'.join(saida))
