#!/usr/bin/python3
# -*- coding: utf-8 -*-
from nba_api.stats.endpoints import leaguegamefinder
from nba_api.stats.static import teams
import pandas as pd
import numpy as np
import pprint
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
teams_info = open('teams_info.csv')

teams_info = pd.read_csv('teams_info.csv', index_col=0)

games = []
dataFrame = pd.DataFrame()
for iterator in range(teams_info.shape[0]):
    game = leaguegamefinder.LeagueGameFinder(season_segment_nullable='Regular Season', season_nullable='2019-20', team_id_nullable=teams_info['ID'][iterator]).get_data_frames()[0]
    game = game[0:game.shape[0]-10]
    dataFrame = pd.concat((dataFrame,game), ignore_index=True)

games_sorted = dataFrame.sort_values(by=['GAME_DATE'], ascending=False)
games_sorted.to_csv('games_sorted.csv', index=False, encoding='utf-8')
