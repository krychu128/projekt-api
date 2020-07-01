import requests 
from bs4 import BeautifulSoup

def my_url():
    URL = 'https://suchen.mobile.de/fahrzeuge/details.html?id=296119051&damageUnrepaired=NO_DAMAGE_UNREPAIRED&isSearchRequest=true&makeModelVariant1.makeId=3500&makeModelVariant1.modelGroupId=53&pageNumber=1&scopeId=C&sfmr=false&searchId=6ba54eac-b865-d29d-6bd5-3bc7f9fb9e72'

    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

    str = requests.get(URL, headers=headers)

    bsoup = BeautifulSoup(str.content, 'html.parser')



    dict=[]
    
    comp={
        "Nazwa": bsoup.find(class_="g-col-7").text,
        "Cena": bsoup.find(class_="rbt-sec-price").text,
        }
    dict.append(comp)
    print(dict)  
    return dict
my_url()
