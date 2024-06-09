# galat o/p aa ha hai
#project -2
import requests
import pandas as pd
from bs4 import BeautifulSoup

Names=[]
Prices=[]
Desc=[]
# Reviews=[]

url="https://www.airbnb.co.in/s/New-Delhi--Delhi--India/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2024-06-01&monthly_length=3&monthly_end_date=2024-09-01&price_filter_input_type=0&channel=EXPLORE&query=New%20Delhi%2C%20Delhi&place_id=ChIJLbZ-NFv9DDkRzk0gTkm3wlI&location_bb=QeWkpUKasJ9B4zuZQpolYg%3D%3D&date_picker_type=calendar&source=structured_search_input_header&search_type=autocomplete_click"
r=requests.get(url)
# print(r)

soup=BeautifulSoup(r.text,"html.parser")
# print(soup)
# print(soup.prettify())

for i in range(1,13):
    np=soup.find("a",class_ ="l1ovpqvx").get("href")

    # print(np)
    cnp="https://www.airbnb.co.in/"+np
    # print(cnp)

    url=cnp
    r=requests.get(url)
    soup=BeautifulSoup(r.text,"html.parser")
    
    names=soup.find_all("div",class_="t1jojoys atm_g3_1kw7nm4 atm_ks_15vqwwr atm_sq_1l2sidv atm_9s_cj1kg8 atm_6w_1e54zos atm_fy_1vgr820 atm_7l_jt7fhx atm_cs_9dzvea atm_w4_1eetg7c atm_ks_zryt35__1rgatj2 dir dir-ltr")
    for i in names:
        n=i.text.strip()
        Names.append(n)
    print(len(names))
    
    prices=soup.find_all("span",class_="a8jt5op atm_3f_idpfg4 atm_7h_hxbz6r atm_7i_ysn8ba atm_e2_t94yts atm_ks_zryt35 atm_l8_idpfg4 atm_mk_stnw88 atm_vv_1q9ccgz atm_vy_t94yts dir dir-ltr")
    for i in prices:
        p=i.text.strip()
        Prices.append(p)
    print(len(prices))
    
    desc=soup.find_all("span",class_="t6mzqp7 atm_g3_1kw7nm4 atm_ks_15vqwwr atm_sq_1l2sidv atm_9s_cj1kg8 atm_6w_1e54zos atm_fy_kb7nvz atm_7l_1he744i atm_am_qk3dho atm_ks_zryt35__1rgatj2 dir dir-ltr")
    # print(desc)
    for i in desc:
        d=i.text.strip()
        Desc.append(d)
    print(len(desc))
    
    # reviews=soup.find_all("span",class_="a8jt5op dir dir-ltr")
    # for i in reviews:
    #     r=i.text
    #     Reviews.append(r)
    # print(len(reviews))
        
# df=pd.DataFrame({"Name":Names, "Prices":Prices, "Description":Desc})
    # print(df)