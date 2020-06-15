#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pandas as pd
import datetime

def setPandas():
    pd.set_option('display.max_columns', 120)
    pd.set_option('display.max_rows', 120)

def findTeamsAbbreviation(nba_teams):
    teams_abbreviation = []
    for iterator in range(len(nba_teams)):
        if nba_teams[iterator]['abbreviation']:
                teams_abbreviation.append(nba_teams[iterator]['abbreviation'])
    return teams_abbreviation

def findIdTeams(nba_teams):
    teams_id = []
    for iterator in range(len(nba_teams)):
        if nba_teams[iterator]['id']:
            teams_id.append(nba_teams[iterator]['id'])
    return teams_id

def findFullName(nba_teams):
    teams_fullName = []
    for iterator in range(len(nba_teams)):
        if nba_teams[iterator]['full_name']:
             teams_fullName.append(nba_teams[iterator]['full_name'])
    return teams_fullName

def teams_info(nba_teams):
    teams_id = findIdTeams(nba_teams)
    teams_abbreviation = findTeamsAbbreviation(nba_teams)
    teams_fullName = findFullName(nba_teams)
    teamsAbbrID = {'TeamsAbbr': teams_abbreviation, 'TeamsID': teams_id, 'TeamsFullName': teams_fullName}
    df = pd.DataFrame(teamsAbbrID)

    return df


def currentDay():
    today = datetime.datetime.today()
    today = today.strftime('%d-%m-%Y')
    return print(type(today))


