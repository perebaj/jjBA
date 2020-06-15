#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pandas as pd
regular_season19 = pd.read_csv('regularseason19.csv', index_col=0)
regular_season19.info()
#Tudo ok 