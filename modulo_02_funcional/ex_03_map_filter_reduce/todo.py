from functools import reduce


def firstChars(L):
    """ Maps strings in L to a list with the first character of each string.
    For instance:
    firstChars(['python', 'is', 'pythy']) == ['p', 'i', 'p']
    """
    return list(map(lambda x: x[0], L))


def sum(L):
    """ Sums the elements in L """
    return reduce(lambda acc, b: acc + b, L, 0)


def avg(L):
    """ Returns the average of the elements in L """
    soma = sum(L)
    return soma / len(L)


def maxString(L):
    """ Retorna a maior string dentre as strings em L.
    Por exemplo: maxString(['python', 'is', 'pythy']) == 'python'
    Se houver empate, retorna a primeira string encontrada.
    """
    max_len = 0

    for item in L:
        if len(item) > max_len:
            max_len = len(item)
            string = item

    return string

    return reduce(lambda acc, b: acc if acc > b else b, L)


def add2Dict(D, N, S):
    """ Insere a string S na lista associada ao inteiro N dentro
    do dicionario D.
    Por exemplo, se D = {1: ['b'], 2: ['xd'], 3: ['abc']}, entao,
    add2Dict(D, 2, 'ww') produz o novo dicionario:
    {1: ['b'], 2: ['xd', 'ww'], 3: ['abc']}
    Voce pode usar essa funcao para completar buildLenFreq
    """
    D[N] = D[N] + [S] if N in D else [S]
    return D


def buildLenFreq(L):
    """ Esta funcao constroi um dicionario que associa inteiros a listas com
    palavras daquele tamanho. Por exemplo:
    ins(['abc', 'xd', 'b', 'xxx']) = {1: ['b'], 2: ['xd'], 3: ['abc', 'xxx']}
    """
    D = {}
    for item in L:
        D = add2Dict(D, len(item), item)

    return D


def incValue(D, N):
    """Esta funcao incrementa o valor associado a chave N dentro do dicionario
    D. Por exemplo, se D = {1: 2, 2: 4, 3: 11}, entao
    Voce pode usar essa funcao para completar countFirsts
    """
    D[N] = D[N] + 1 if N in D else 1
    return D


def countFirsts(L):
    """ Conta o numero de ocorrencias do primeiro caracter de cada string em L.
    Por exemplo, countFirsts(['python', 'is', 'pythy']) === {'i': 1, 'p': 2}
    Note que essa funcao retorna um dicionario com cada caracter associada ao
    numero de strings que comecam com aquele caracter.
    """

    D = {}
    for item in L:
        D = incValue(D, item[0])

    return D


def mostCommonFirstChar(L):
    """ Retorna a letra mais comum entre as primeiras letras de strings em L.
    Por exemplo:
    mostCommonFirstChar(['python', 'is', 'pythy']) === 'p'
    """

    D = countFirsts(L)
    max_value = 0

    for key, value in D.items():
        if value > max_value:
            max_value = value
            max_key = key

    return max_key
