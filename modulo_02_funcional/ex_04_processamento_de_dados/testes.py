from modulo_02_funcional.ex_04_processamento_de_dados.todo import lastNames, citations, fullCitations, \
    singleFullCitation

L = [['Antonio', 'franco'], ['Caius', 'vitelus', 'Aquarius'], ['Cristovao', 'Buarque']]
caius = ['Caius', 'vitelus', 'Aquarius']

print(lastNames(L))

print(citations(L))

print(singleFullCitation(caius))

print(fullCitations(L))
