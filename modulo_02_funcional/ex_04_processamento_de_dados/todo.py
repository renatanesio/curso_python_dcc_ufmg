from functools import reduce


def lastNames(L):
    """Mapeia uma lista de nomes para o ultimo nome de cada item.
    Por exemplo, seja:
    L = [['Antonio', 'Franco'], ['Caius', 'Vitelus'], ['Cristovao', 'Buarque']]
    Entao lastNames(L) == ['Franco', 'Vitelus', 'Buarque']
    """
    return list(map(lambda x: x[-1].title(), L))


def citations(L):
    """Mapeia uma lista de nomes para a primeira letra mais sobrenome.
    Por exemplo, seja:
    L = [['Antonio', 'Franco'], ['Caius', 'Vitelus'], ['Cristovao', 'Buarque']]
    entao citations(L) = ['A. Franco', 'C. Vitelus', 'C. Buarque']
    Note que a primeira letra precisa estar capitalizada.
    """

    return list(map(lambda x: f"{x[0][0].capitalize()}. {x[-1].title()}", L))


def singleFullCitation(name):
    return reduce(lambda citation, n: citation + n[0].capitalize() + ". "
    if n != name[-1] else citation + n.capitalize(), name, "")


def fullCitations(L):
    """Mapeia uma lista de nomes para as iniciais mais o ultimo nome.
    Por exemplo, seja:
    L = [
        ['Antonio', 'Franco', 'Molina'],
        ['Caius', 'vitelus', 'Aquarius'],
        ['cristovao', 'buarque', 'Holanda']]
    entao fullCitations(L) = ['A. F. Molina', 'C. V. Aquarius', 'C. B. Holanda']
    Note que as iniciais precisam estar capitalizada.
    """

    return list(map(singleFullCitation, L))
