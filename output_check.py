import pandas as pd
from team_classes import ATL
from stat_functions import ppg

name = input("player name?")


df = ATL.bos()

f = ppg(name, df)

print(f)

# this taught me that to use the ppg function you must insert the specific df