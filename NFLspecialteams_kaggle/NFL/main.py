#%% imports
from pandas import DataFrame, read_csv
import pandas as pd

#global variables
games = pd.read_csv(".Users/robin/OneDrive/Desktop/data/games.csv", sep=',')
scout_data = pd.read_csv(".Users/robin/OneDrive/Desktop/data/PFFScoutingData.csv", sep=',')
players = pd.read_csv(".Users/robin/OneDrive/Desktop/data/players.cs", sep=',')
plays = pd.read_csv(".Users/robin/OneDrive/Desktop/data/plays.csv", sep=',')
track18 = pd.read_csv(".Users/robin/OneDrive/Desktop/data/tracking2018.csv", sep=',')
track19 = pd.read_csv(".Users/robin/OneDrive/Desktop/data/tracking2019.csv", sep=',')
track20 = pd.read_csv(".Users/robin/OneDrive/Desktop/data/tracking2020.csv", sep=',')

