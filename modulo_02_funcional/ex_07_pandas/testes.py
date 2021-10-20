from modulo_02_funcional.ex_07_pandas.todo import numRows, numColumns, numGoldTotal, numSummerGoldCountry, \
    getCodeMaxSummerGold
import pandas as pd

games = pd.read_csv('games.csv')

print(numRows(games))

print(numColumns(games))

print(numGoldTotal(games))

print(numSummerGoldCountry(games, 'Brazil'))

print(getCodeMaxSummerGold(games))
