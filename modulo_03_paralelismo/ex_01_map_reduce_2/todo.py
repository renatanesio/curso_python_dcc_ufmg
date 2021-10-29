# -*- coding: utf8


from collections import Counter  # RECOMENDADO!


def conta_um_arquivo(fpath):
    texto = []

    with open(fpath) as input_file:
        for line in input_file:
            line = line.lower().strip()
            if line:
                palavras = line.split()
                texto.extend(palavras)
        return dict(Counter(texto))


def reduz(contagens_1, contagens_2):
    return sum((Counter(dict(x)) for x in [contagens_1, contagens_2]), Counter())
