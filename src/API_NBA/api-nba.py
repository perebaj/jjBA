#!/usr/bin/python3
# -*- coding: utf-8 -*-
from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder
import pandas as pd
import pprint 


nba_teams = teams.get_teams()
games = leaguegamefinder.LeagueGameFinder().get_data_frames()[0]
games1920 = games[games.SEASON_ID.str[-4:] == '2019']

print(games1920['GAME_ID'][:20])
regular_season = games1920[games1920.GAME_DATE.str[-5:] == '10-22']
print(regular_season.shape)
print(regular_season.iloc[-1])
# games1920.to_csv('games.csv', index=False)
