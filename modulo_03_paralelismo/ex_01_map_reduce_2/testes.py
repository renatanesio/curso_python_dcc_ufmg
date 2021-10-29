import os
from collections import Counter  # RECOMENDADO!

from modulo_03_paralelismo.ex_01_map_reduce_2.todo import conta_um_arquivo, reduz

current_directory = os.getcwd()
monster = os.path.join(current_directory, "MonsterMaker.txt")
prejudice = os.path.join(current_directory, "PridePrejudice.txt")

monstro = conta_um_arquivo(monster)
preconceito = conta_um_arquivo(prejudice)

soma = reduz(monstro, preconceito)
