#!/usr/bin/python3
# -*- coding: utf-8 -*-
from nba_api.stats.endpoints import leaguegamefinder
from nba_api.stats.static import teams
import pandas as pd
import numpy as np
import pprint

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

teams = teams.get_teams()
games = leaguegamefinder.LeagueGameFinder(season_segment_nullable='Regular Season', season_nullable='2019-20', team_id_nullable=1610612738).get_data_frames()[0]



pprint.pprint(teams[0].keys())
teams_abbreviation = []
teams_id = []
teams_fullname = []
for team in teams:
    teams_abbreviation.append(team['abbreviation'])
    teams_id.append(team['id'])
    teams_fullname.append(team['full_name'])

    


teams_info = {}
teams_info['TEAMS_ABBREVIATION'] = teams_abbreviation
teams_info['ID'] = teams_id
teams_info['FULL_NAME'] = teams_fullname
# pprint.pprint(teams_info)
pd_teams_info = pd.DataFrame.from_dict(teams_info)

pd_teams_info.to_csv('teams_info.csv', index=False, encoding='utf-8')



