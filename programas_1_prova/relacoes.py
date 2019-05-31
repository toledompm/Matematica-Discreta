#define as funcoes para as operacoes
def maior(n,n2):
    if n > n2:
        return True
    return False

def menor(n,n2):
    if n < n2:
        return True
    return False

def igual(n,n2):
    if n == n2:
        return True
    return False

#leia o tipo da relacao
print("escreva o tipo da relacao(<;>;=;<=;>=)")
tipoRelacao = input()

#leia os 2 conjuntos
print("escreva os valores do conjunto A separados por um espaco(ex: '1 2 3 4')")
conjuntoA = input().split(" ")
print("escreva os valores do conjunto B separados por um espaco(ex: '1 2 3 4')")
conjuntoB = input().split(" ")

#escreva a relacao e o conjuntoB
print (tipoRelacao+"|"+"|".join(conjuntoB))

#para todo i em A
for i in conjuntoA:
    #cria um vetor para representar a linha i
    linha = []
    #para todo x em B
    for x in conjuntoB:
        #compara i com x, se as comparações forem verdadeiras adiciona i a linha, se não adiciona 0
        if tipoRelacao == "<":
            if menor(i,x):
                linha.append(1)
                continue
        elif tipoRelacao == ">":
            if maior(i,x):
                linha.append(1)
                continue
        elif tipoRelacao == "=":
            if igual(i,x):
                linha.append(1)
                continue
        elif tipoRelacao == ">=":
            if maior(i,x) or igual(i,x):
                linha.append(1)
                continue
        elif tipoRelacao == "<=":
            if menor(i,x) or igual(i,x):
                linha.append(1)
                continue

        linha.append(0)

    #escreva i e a linha com as relacoes
    print(i+"|"+";".join([str(i) for i in linha]))