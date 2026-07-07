#questao 1

def contagem_caracteres(texto):
    contagem = {}

    for caractere in texto:
        if caractere in contagem:
            contagem[caractere] += 1
        else:
            contagem[caractere] = 1
    return contagem


frase = "Adoro estudar POO e sonhar com um futuro aonde me torno uma engrenagem do capitalismo"
resultado = contagem_caracteres(frase)

print(resultado)

#questao 2

arquivo = open("estomago.txt", "r", encoding="utf-8")

texto = arquivo.read()
arquivo.close()

palavras = texto.split()

contagem = {}

for palavra in palavras:
    palavra = palavra.lower()

    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1

dicionarioordenado = dict(
    sorted(contagem.items(), key=lambda item: item[1], reverse=True)
)

print(dicionarioordenado)

#questao 3

def mesclardicionarios(dic1, dic2):
    resultado = {}

    for chave, valor in dic1.items():
        resultado[chave] = valor

    for chave, valor in dic2.items():
        if chave in resultado:
            if valor > resultado[chave]:
                resultado[chave] = valor
        else:
            resultado[chave] = valor

    return resultado


dicionario1 = {'a': 1, 'b': 2, 'c': 3}
dicionario2 = {'b': 4, 'd': 5}

resultado = mesclardicionarios(dicionario1, dicionario2)
print(resultado)

#questao 4

def filtrardicionario(dados, chaves_filtradas):
    resultado = {}

    for chave in chaves_filtradas:
        if chave in dados:
            resultado[chave] = dados[chave]

    return resultado


dados = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
chaves_filtradas = ['a', 'c', 'e']

resultado = filtrardicionario(dados, chaves_filtradas)
print(resultado)


# questao 05

def resultado_votacao(votos):
    novo_dic = {}
    for voto in votos:
        for chave, valor in voto.items():
            if chave in novo_dic:
                novo_dic[chave] += valor
            else:
                novo_dic[chave] = valor
    total = sum(novo_dic.values())
    for chave, valor in novo_dic.items():
        media = round((valor / total) * 100, 2)
        novo_dic[chave] = (valor, media)
    return novo_dic

votos = [
    {'candidato_A': 120, 'candidato_B': 85, 'candidato_C': 90},
    {'candidato_A': 110, 'candidato_B': 95, 'candidato_C': 80},
    {'candidato_A': 130, 'candidato_B': 78, 'candidato_C': 105},
]
resultado = resultado_votacao(votos)
print(resultado)