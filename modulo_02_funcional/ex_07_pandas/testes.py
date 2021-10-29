from modulo_02_funcional.ex_07_pandas.todo import numRows, numColumns, numGoldTotal, numSummerGoldCountry, \
    getCodeMaxSummerGold, getNthBestSummerCountry, numCountriesWithMoreThanNWinterMedals, numWinterCountries, \
    countGoldsWithLetter, countHybernalCountries
import pandas as pd

games = pd.read_csv('games.csv')

print(numRows(games))

print(numColumns(games))

print(numGoldTotal(games))

print(numSummerGoldCountry(games, 'Brazil'))

print(getCodeMaxSummerGold(games))

print(getNthBestSummerCountry(games, 5))

print(numCountriesWithMoreThanNWinterMedals(games, 63))

print(numWinterCountries(games))

print(countGoldsWithLetter(games, "B"))

print(countHybernalCountries(games))
