#recebe um vetor e uma posicao, verifica se algum dos valores anteriores no vetor é igual o que esta na posicao indicada
def repete(vet, pos):
    for i in range(0,pos):
        if vet[pos] == vet[i]:
            return True
    return False

#recebe um valor e um vetor, verifica se o valor existe no vetor
def existe(vet, val):
    for i in vet:
        if val == i:
            return True
    return False

#leia os 2 conjuntos
print("escreva os valores do conjunto A separados por um espaco(ex: '1 2 3 4')")
conjuntoA = input().split(" ")
print("escreva os valores do conjunto B separados por um espaco(ex: '1 2 3 4')")
conjuntoB = input().split(" ")

#define o vetor da interseccao
interseccao = []

#para x = todo valor de A
for x in range(len(conjuntoA)):
    #se nao repete
    if not repete(conjuntoA,x):
        #se existe no outro conjunto
        if existe(conjuntoB,conjuntoA[x]):
            #adiciona a interseccao
            interseccao.append(conjuntoA[x])

#escreva a interseccao
print(";".join(interseccao))

