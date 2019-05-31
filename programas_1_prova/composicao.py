#funcao para determinar as relacoes
def relaciona(c1, c2):
    #declara o conjunto a ser retornado
    conjunto = []
    #declara a variavel de decisao
    val = 0
    #para todo i em c1(conjunto1)
    for i in c1:
        #para todo x em c2(conjunto2)
        for x in c2:
            #pergunta ao usuario se os elementos se relacionam
            print(i," se relaciona com:",x,"?(0-Não, 1-Sim)")
            val = int(input())
            #se sim, adicione ao conjunto
            if val == 1:
                conjunto.append([i,x])
    #retorne o conjunto
    return conjunto


#lendo os conjuntos
print("Entre com os elementos do conjunto A separados por um espaco(ex: a b c 2)")
conjuntoA = input().split(" ")
print("Entre com os elementos do conjunto B separados por um espaco(ex: a b c 2)")
conjuntoB = input().split(" ")
print("Entre com os elementos do conjunto C separados por um espaco(ex: a b c 2)")
conjuntoC = input().split(" ")

#chama a funcao para determinar a relacao entra A e B
relAB = relaciona(conjuntoA,conjuntoB)
#chama a funcao para determinar a relacao entra B e C
relBC = relaciona(conjuntoB,conjuntoC)

#declarando a relacao entre A e C
relAC = []

#para todo z em AB
for z in relAB:
    #para todo w em BC
    for w in relBC:
        #se o segundo termo de z for igual o primeiro termo de w (z = <a;b>  w = <b;c> se b=b)
        if z[1] == w[0]:
            #adicione o primeiro termo de z e o segundo termo de w a relacao AC 
            #(z = <a;b>  w = <b;c> relAC = <a;c>)
            relAC.append([z[0],w[1]])


#para todo y em AC
for y in relAC:
    #imprima o primeiro termo de y se relaciona com o segundo termo de y (y = <a;c>)
    print(y[0]," se relaciona com:",y[1])

