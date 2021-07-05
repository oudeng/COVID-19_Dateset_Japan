#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

NHK COVID-19 Dataset

Data link: https://www3.nhk.or.jp/n-data/opendata/coronavirus/nhk_news_covid19_prefectures_daily_data.csv

Created on Mon Jul  5 23:16:52 2021
@author: oudeng

Q: How it works?
A: It gets NHK COVID-19 dataset automatically and saves as working csv, then plots them.

Q: How to use this file?
A: Input in line77 of a_0 to choose which column of data.
   And input in line112 to choose the prefecture(s) to plot.


"""

import numpy as np
import pandas as pd
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt

import io
import requests

# NHK COVID-19 Dataset.
url="https://www3.nhk.or.jp/n-data/opendata/coronavirus/nhk_news_covid19_prefectures_daily_data.csv"
s=requests.get(url).content
data_all=pd.read_csv(io.StringIO(s.decode('utf-8')))

df0 = data_all.rename(columns = {'日付': 'Date', 
                                 '都道府県コード': 'Prefecture_ID', 
                                 '都道府県名':'Name',
                                 '各地の感染者数_1日ごとの発表数':'Daily_Confirmed_Cases',
                                 '各地の感染者数_累計':'Daily_Confirmed_Cases_Total',
                                 '各地の死者数_1日ごとの発表数':'Daily_Death',
                                 '各地の死者数_累計':'Death_Total'}, inplace = False)

df_target = pd.DataFrame(index=[], columns=[])  # Make an empty dataframe container.

Prefecture_IDs = df0["Prefecture_ID"].unique() # Make Prefecture_ID be unique.

# ref: https://www.delftstack.com/ja/howto/python-pandas/split-pandas-dataframe/
Prefectures = df0.groupby(df0.Prefecture_ID)

for Prefecture_ID in Prefecture_IDs:
    df_tmp = Prefectures.get_group(Prefecture_ID).set_index(['Date'])
    df_target = pd.concat([df_target,df_tmp], axis=1, ignore_index=False)

# df_target saves as csv, the work file.
df_target.to_csv('df_target.csv',index=True, encoding='cp932')

# Load df_target.csv and df_target_tmp.csv to contat, then asve as df_target_all.csv.
df_target_tmp = pd.read_csv('df_target_tmp.csv', parse_dates=True, index_col='Date', encoding='cp932')
df_target = pd.read_csv('df_target.csv', parse_dates=True, index_col='Date', encoding='cp932')

df_target_all = pd.concat([df_target_tmp, df_target], axis=0)
df_target_all.to_csv('df_target_all.csv',index=True, encoding='cp932')

# REF: https://www.cnpython.com/qa/367000

# df_target_all:
# index: Date
# iloc: (0)Prefecture_ID, (1)Name, (2)Daily_Confirmed_Cases, (3)Daily_Confirmed_Cases_Total, (4)Daily_Death, (5)Death_Total, 

Col_Dict = {'0':'Prefecture_ID', '1':'Name', '2':'Daily_Confirmed_Cases', '3':'Daily_Confirmed_Cases_Total',
            '4':'Daily_Death', '5':'Death_Total'}

# Prefecture_Dict
Prefecture_Dict = {'1': 'Hokkaido','2': 'Aomori','3': 'Iwate','4': 'Miyagi','5': 'Akita','6': 'Yamagata','7': 'Fukushima',
                   '8': 'Ibaraki','9': 'Tochigi','10': 'Gunma','11': 'Saitama','12': 'Chiba','13': 'Tokyo','14': 'Kanagawa',
                   '15': 'Niggata','16': 'Toyama','17': 'Ishikawa','18': 'Fukui','19': 'Yamanashi','20': 'Nagano',
                   '21': 'Gifu','22': 'Shizuoka','23': 'Aichi','24': 'Mie','25': 'Shiga','26': 'Kyoto','27': 'Osaka',
                   '28': 'Hyogo','29': 'Nara','30': 'Wakayama','31': 'Totori','32': 'Shimane','33': 'Okayama','34': 'Hiroshima',
                   '35': 'Yamaguchi','36':'Tokushima','37': 'Kagawa','38': 'Ehime','39': 'Kochi','40': 'Fukuoka',
                   '41': 'Saga','42': 'Nagasaki','43': 'Kumamoto','44': 'Oita','45': 'Miyazaki','46': 'Kagoshima','47': 'Okinawa'}

# If graph "Daily_Confirmed_Cases", column iloc=2,8,14..., a_n = a_0+6*(n-1)
# e.g. r = pd.DataFrame(df_target_all.iloc[:,2])

a_0 = 2  # Choose in Col_Dict.

df_target = pd.DataFrame(index=[], columns=[])  # Make an empty dataframe container.

for i in range(1, 48):
    col = a_0 + 6*(i-1)
    
    if col < 5:
        Col_Dict_Key = Col_Dict[str(a_0)]
    else:
        Col_Dict_Key = Col_Dict[str(a_0)]+'.'+str(i-1)
            
    df_target_tmp = df_target_all.iloc[:,[col]].rename(columns = {Col_Dict_Key:Prefecture_Dict[str(i)]}, inplace = False)
    df_target = pd.concat([df_target, df_target_tmp], axis=1, ignore_index=False)
    
    # Ref:
    #r = pd.DataFrame(df_target.iloc[:,2])
    #df_1and2 = pd.concat([df1, df2], axis=1, ignore_index=False)
    #.rename(columns = {'日付': 'Date'}, inplace = False)

file = 'data_target_' + str(a_0) +'.csv'
df_target.to_csv(file, index=True, encoding='cp932')

# Input the prefecture(s) to disply.
fig, ax = plt.subplots(1,1,figsize=(10,6), dpi=120)
plt.grid(axis='both') #axis='y'

Prefecture_Dict = {'1': 'Hokkaido','2': 'Aomori','3': 'Iwate','4': 'Miyagi','5': 'Akita','6': 'Yamagata','7': 'Fukushima',
                   '8': 'Ibaraki','9': 'Tochigi','10': 'Gunma','11': 'Saitama','12': 'Chiba', '13': 'Tokyo','14': 'Kanagawa',
                   '15': 'Niggata','16': 'Toyama','17': 'Ishikawa','18': 'Fukui','19': 'Yamanashi','20': 'Nagano',
                   '21': 'Gifu','22': 'Shizuoka','23': 'Aichi','24': 'Mie','25': 'Shiga','26': 'Kyoto','27': 'Osaka',
                   '28': 'Hyogo','29': 'Nara','30': 'Wakayama','31': 'Totori','32': 'Shimane','33': 'Okayama','34': 'Hiroshima',
                   '35': 'Yamaguchi','36':'Tokushima','37': 'Kagawa','38': 'Ehime','39': 'Kochi','40': 'Fukuoka',
                   '41': 'Saga','42': 'Nagasaki','43': 'Kumamoto','44': 'Oita','45': 'Miyazaki','46': 'Kagoshima','47': 'Okinawa'}

to_display = [13, 27, 1]

L1 = df_target[Prefecture_Dict[str(to_display[0])]].tolist()
L2 = df_target[Prefecture_Dict[str(to_display[1])]].tolist()
L3 = df_target[Prefecture_Dict[str(to_display[2])]].tolist()

ax.set_ylabel('Daily confirmed cases of the selected prefectures', color='black') # If a_0 =2
ax.plot(L1, color='tomato', linewidth=1.0, linestyle='-', label=Prefecture_Dict[str(to_display[0])])
ax.plot(L2, color='royalblue', linewidth=1.0, linestyle='-', label=Prefecture_Dict[str(to_display[1])])
ax.plot(L3, color='peru', linewidth=1.0, linestyle='-', label=Prefecture_Dict[str(to_display[2])])

ax.legend(loc='upper left', borderaxespad=2, fontsize=12)

ax.xaxis.set_major_locator(mdates.MonthLocator())
# 16 is a slight approximation since months differ in number of days.
ax.xaxis.set_minor_locator(mdates.MonthLocator(bymonthday=16))

ax.xaxis.set_major_formatter(ticker.NullFormatter())
ax.xaxis.set_minor_formatter(mdates.DateFormatter('%b'))

for tick in ax.xaxis.get_minor_ticks():
    tick.tick1line.set_markersize(0)
    tick.tick2line.set_markersize(0)
    tick.label1.set_horizontalalignment('center')

ax.set_xlabel('2019 / 2020 ------------------------------------------------------------------------ 2020 / 2021 -------------------------------------------', loc='left')

plt.show()

######################################################

# Graph all Japan data.

fig, ax = plt.subplots(1,1,figsize=(10,6), dpi=120)
plt.grid(axis='both') #axis='y'

ax.plot(df_target)

ax.xaxis.set_major_locator(mdates.MonthLocator())
# 16 is a slight approximation since months differ in number of days.
ax.xaxis.set_minor_locator(mdates.MonthLocator(bymonthday=16))

ax.xaxis.set_major_formatter(ticker.NullFormatter())
ax.xaxis.set_minor_formatter(mdates.DateFormatter('%b'))

ax.set_ylabel('Daily confirmed cases of each prefecture', color='black')

for tick in ax.xaxis.get_minor_ticks():
    tick.tick1line.set_markersize(0)
    tick.tick2line.set_markersize(0)
    tick.label1.set_horizontalalignment('center')

ax.set_xlabel('2019 / 2020 ------------------------------------------------------------------------ 2020 / 2021 -------------------------------------------', loc='left')

plt.show()



