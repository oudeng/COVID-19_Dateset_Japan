# COVID-19_Dateset_NHK

### This programme may be the simplest method to get the COVID-19 key features of Japan. From the pandemic begining to the latest.

### As a famous public TV station, NHK made a very good open data website to press the COVID-19 situation, especially the Japan information with daily updating.
### This dataset focus on : 'Daily_Confirmed_Cases', 'Daily_Confirmed_Cases_Total', 'Daily_Death' and 'Death_Total' in each prefecture of Japan. The data is from the COVID-19 beginning in Japan to the latest.
### Datalink: https://www3.nhk.or.jp/n-data/opendata/coronavirus/nhk_news_covid19_prefectures_daily_data.csv

#### Q: How it works?
#### A: It gets NHK COVID-19 dataset automatically. Acording your input parameters, the filtering result of csv and png will be saved to the results subfolder. 

#### Q: How to use this file?
#### A: Just input prefered parameters of Col_Dict and  Prefecture_Dict. The input place is between "INPUTs START" and "INPUTs END". 

   Col_Dict = {'0':'Prefecture_ID', '1':'Name', '2':'Daily_Confirmed_Cases', '3':'Daily_Confirmed_Cases_Total',
            '4':'Daily_Death', '5':'Death_Total'}
            
   
   Prefecture_Dict = {'1': 'Hokkaido','2': 'Aomori','3': 'Iwate','4': 'Miyagi','5': 'Akita','6': 'Yamagata','7': 'Fukushima',
                   '8': 'Ibaraki','9': 'Tochigi','10': 'Gunma','11': 'Saitama','12': 'Chiba','13': 'Tokyo','14': 'Kanagawa',
                   '15': 'Niggata','16': 'Toyama','17': 'Ishikawa','18': 'Fukui','19': 'Yamanashi','20': 'Nagano',
                   '21': 'Gifu','22': 'Shizuoka','23': 'Aichi','24': 'Mie','25': 'Shiga','26': 'Kyoto','27': 'Osaka',
                   '28': 'Hyogo','29': 'Nara','30': 'Wakayama','31': 'Totori','32': 'Shimane','33': 'Okayama','34': 'Hiroshima',
                   '35': 'Yamaguchi','36':'Tokushima','37': 'Kagawa','38': 'Ehime','39': 'Kochi','40': 'Fukuoka',
                   '41': 'Saga','42': 'Nagasaki','43': 'Kumamoto','44': 'Oita','45': 'Miyazaki','46': 'Kagoshima','47': 'Okinawa'}

