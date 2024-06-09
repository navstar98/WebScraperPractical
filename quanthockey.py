import pandas as pd
import requests
from io import StringIO

url='https://www.quanthockey.com/nhl/teams/tampa-bay-lightning-players-2023-24-nhl-stats.html'
# df_list=pd.read_html('https://finviz.com/quote.ashx?t=TSLA&p=d')    
# gives 403 error , so we are using requests here
 # print(df_list)   
 
headers={
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36'
}

# print(headers)
res=requests.get(url, headers=headers)
print(res.status_code)
# print(res.text)

# Wrap the HTML content in a StringIO object
html_content = StringIO(res.text)

df_list=pd.read_html(html_content,attrs={'class':'ps_tbl'})
print(len(df_list))
# print(df_list)
df_list[0].to_csv('quanthockey_table.csv',index=False)
