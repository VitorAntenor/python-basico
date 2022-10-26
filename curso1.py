#Aspas simples = String
print("******** Mostrando Strings ********")
nome = 'vitor'
idade = '22'
print("Nome:",nome)
print("Idade:",idade)

print("******** Lista e manipulando elementos que vão aparecer ********")
lista=[1,2,3,'vitor',4,5,[1,2,3,4,5]]
print("Lista:",lista)
print("Penúltimo elemento:",lista[5])

#os dois pontos indicam de onde até onde a lista vai
print("******** Determinando valores da lista ********")
print("Determinando valores da lista:", lista[1:4])

#Dicionario pra definir uma chave correspondente a um numero (indexação)
print("******** Dicionário ********")
dic = {'Valor1' : 1, 'Valor2' : 2}
print("Valores:",dic['Valor1'])

#Tupla = lista, usando parenteses ao inves de colchetes
print("******** Tupla ********")
tupla = (1,2,3)
print("Tupla:", tupla)

#if e else
print("******** IF e Else ********")
a=1
b=2
if a==b or a+b == 3:
    print("Verdadeiro.")
else:
     print("Falso.")

#seq foi gerado apenas pra ser impresso como teste. No for "item", poderia ter
#sido escrita qualquer outra coisa
print("******** FOR ********")
seq = [9,8,7,6,5]
for item in seq:
    print("item")

# o Range preenche números dentro de um intervalo determinado
print("******** RANGE ********")
for i in range(0,10):
    print(i)

#Mostrando o funcionamento do While
#Se tirar o i= i+1, o codigo vira um loop
print("******** WHILE ********")
i = 1
while i < 5:
    print('i vale: {}'.format(i))
    i= i + 1

#FUNÇÃO
print("******** FUNÇÃO ********")
def quadrado(var):
    return var ** 2

#MAP = calcula valores de um iteravel e passa como parametros de uma funcao
print("******** MAP ********")
seq1 = [1,2,3,4]
map(quadrado, seq1)
print("Quadrado:", quadrado)
#convertendo map pra lista, pra aparecer os numeros ao quadrado
list (map(quadrado,seq1))
print("Numeros ao quadrado:", seq1)

#FILTER
print("******** FILTER ********")
list(filter(lambda item:item%2!=0, seq1))
print("Divisoes exatas:", item)

#MÉTODOS 
print("******** MÉTODOS ********")
str = 'Olá, me chamo Vitor'
print("Teste de string:", str)

print("******** SPLIT ********")
#split = quebra todas as palavras de forma individual da string
s = 'Ola, pai !'
print(s.split())

#APPEND = ADICIONA UM VALOR A UMA LISTA
print("******** APPEND ********")
list = [1,2,3,4]
list.append(5) #ADICIONANDO O NUMERO 5 À LISTA
print("Lista Adicionando o numero:", list)

print("******** LAST ********")
#O LAST PEGA E IMPRIME O NÚMERO SOLICITADO NO MÉTODO DA LISTA
last = list.pop(2) #O 2 é o número que deve ser impresso
print("Número solicitado:", last)

print("******** OPERADOR IN ********")
#VERIFICA SE O OPERADOR ESTÁ CONTIDO NA LISTA
teste = [1,2,3]
ver = 'x'
if ver in teste:
    print("True.")
else:
    print("False.")

