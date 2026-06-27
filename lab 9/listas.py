#questao 1
numeros = []

while True:
    valor = input("Digite um número: ")

    if valor == "":
        if len(numeros) >= 4:
            break
        print("Digite pelo menos 4 numeros")
    else:
        numeros.append(int(valor))

print("Lista original:", numeros)
print("3 primeiros elementos:", numeros[:3])
print("2 últimos elementos:", numeros[-2:])
print("Lista invertida:", numeros[::-1])
print("Índices pares:", numeros[::2])
print("Índices ímpares:", numeros[1::2])


#questao 2

urls = [
    "www.google.com",
    "www.gmail.com",
    "www.github.com",
    "www.reddit.com",
    "www.yahoo.com"
]

dominios = []

for url in urls:
    dominios.append(url[4:-4])

print("URLs:", urls)
print("Domínios:", dominios)


#questao 3

from random import randint

numeros = []

for _ in range(10):
    numeros.append(randint(-100, 100))

ordenada = sorted(numeros)

print("Lista ordenada:", ordenada)
print("Lista original:", numeros)
print("Índice do maior valor:", numeros.index(max(numeros)))
print("Índice do menor valor:", numeros.index(min(numeros)))
print("Soma:", sum(numeros))
print("Média:", sum(numeros) / len(numeros))


#questao 4

lista1 = []
lista2 = []

qtd1 = int(input("Quantidade de elementos da lista 1: "))

for _ in range(qtd1):
    lista1.append(int(input()))

qtd2 = int(input("Quantidade de elementos da lista 2: "))

for _ in range(qtd2):
    lista2.append(int(input()))

intercalada = []

menor = min(len(lista1), len(lista2))

for i in range(menor):
    intercalada.append(lista1[i])
    intercalada.append(lista2[i])

intercalada.extend(lista1[menor:])
intercalada.extend(lista2[menor:])

print("Lista intercalada:", intercalada)


#questao 5

lista1 = [randint(0, 50) for _ in range(20)]
lista2 = [randint(0, 50) for _ in range(20)]

interseccao = sorted(list(set(lista1) & set(lista2)))

print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Intersecção:", interseccao)


#questao 6

lista = [randint(0, 100) for _ in range(20)]

tamanho = int(input("Tamanho para divisão: "))

sublistas = []

for i in range(0, len(lista), tamanho):
    sublistas.append(lista[i:i+tamanho])

print("Lista original:", lista)
print("Sublistas:", sublistas)


#questao 7

n = int(input("Digite n: "))

matriz = []

for i in range(n):
    linha = [i] * n
    matriz.append(linha)

print("Resultado:")
print(matriz)