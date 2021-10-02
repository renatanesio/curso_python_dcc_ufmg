from modulo_02_funcional.ex_06_modulo_itertools.todo import buildTurns, printCSV, firstDay, countTurns, payTurns

profs = ['Ana', 'Bruno', 'Camila', "Ricardo"]

print(list(buildTurns(profs)))

printCSV(profs)

print(firstDay(['Ana', 'Bruno', 'Camila'], 'Ana'))
print(firstDay(['Ana', 'Bruno', 'Camila'], 'Camila'))

print(countTurns(['Ana', 'Bruno', 'Camila'], 'Ana'))
print(countTurns(['Ana', 'Bruno', 'Camila'], 'Camila'))
print(countTurns(['Ana', 'Bruno', 'Camila'], 'Douglas'))

print(payTurns(['Ana', 'Bruno', 'Camila'], 'Ana'))
print(payTurns(['Ana', 'Bruno', 'Camila'], 'Camila'))
print(payTurns(['Ana', 'Bruno', 'Camila'], 'Douglas'))
