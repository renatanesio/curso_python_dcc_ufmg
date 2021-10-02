from modulo_02_funcional.ex_05_compreensoes_de_dados.todo import delInitials, everyOccurrence, factors, isPerfect

print(delInitials(['Fer', 'mag', 'Q', 'pereira']))
print(delInitials(['Fer', 'm', 'Q', 'pereira']))
print(delInitials(['Fer', 'mag', 'Q', 'pereira', 'S', 'Sa']))
print(delInitials(['a', 'aa', 'b', 'bb']))

print(everyOccurrence('Fernando', 'aeiou'))
print(everyOccurrence('xaxbxaxyza', 'aeiou'))
print(everyOccurrence('0a1e2i3o4u', 'aeiou'))

print(factors(6))
print(factors(10))
print(factors(12))
print(factors(28))

print(isPerfect(6))
print(isPerfect(10))
print(isPerfect(12))
print(isPerfect(28))
