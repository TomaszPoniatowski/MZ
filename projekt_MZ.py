#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 16:03:31 2019

@author: tomasz
"""
#wczytuje dane
import pandas as pd
import matplotlib.pyplot as plt
udary = pd.read_csv('/Users/tomasz/Documents/szkolka/projekt MZ/dane_udary.csv', delimiter = ';')
historia = pd.read_csv('/Users/tomasz/Documents/szkolka/projekt MZ/historia_pacjenta_udarowego.csv', delimiter = ';',
                 encoding='iso-8859-1')
plt.hist(udary['PLEC'])
