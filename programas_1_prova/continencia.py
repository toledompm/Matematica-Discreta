#funcao para verificar se um elemento existe em um conjunto
def existe(conj, ele):
    #para todo i no conjunto conj
    for i in conj:
        #se i = ele
        if i == ele:
            #retorne True
            return True
    #se nenhum i for igual ele retorne False
    return False

#leia os conjuntos
print("entre com os elementos do conjunto A separados por um espaco(ex: a b c d):")
conjuntoA = input().split(" ")
print("entre com os elementos do conjunto B separados por um espaco(ex: a b c d):")
conjuntoB = input().split(" ")

#conjunto B esta contido
contido = True
#para todo x no conjunto B
for x in conjuntoB:
    #se o elemento x não existe no conjunto A
    if not existe(conjuntoA, x):
        #conjunto B não esta contido
        contido = False

#se estiver contido
if contido:
    print("O conjunto B esta contido no conjunto A")
#se nao estiver contido
else:
    print("O conjunto B nao esta contido no conjunto A")