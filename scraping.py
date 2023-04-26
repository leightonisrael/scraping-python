import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

dic_produtos = {'marca':[], 'preco':[]}

#Esse não é o melhor método de colocar o valor da última página
for i in range(1, 14):

    #Url do site
    url_pag = f'https://www.zoom.com.br/celular?enableRefinementsSuggestions=true&hitsPerPage=48&page={i}&pageTitle=Smartphone&q=&sortBy=price_asc'
    
    #Pegue seu User-Agent
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
    site = requests.get(url_pag, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    produtos = soup.find_all('div', class_=re.compile("Paper_Paper__HIHv0 Paper_Paper__bordered__iuU_5 Card_Card__LsorJ Card_Card__clicable__5y__P SearchCard_ProductCard__1D3ve"))


    for produto in produtos:

        marca = produto.find('h2', class_=re.compile("Text_Text__h_AF6 Text_MobileLabelXs__ER_cD Text_DesktopLabelSAtLarge__baj_g SearchCard_ProductCard_Name__ZaO5o")).get_text().strip()  
        preco = produto.find('p', class_=re.compile("Text_Text__h_AF6 Text_MobileHeadingS__Zxam2")).get_text().strip()

        print(marca, preco)

        dic_produtos['marca'].append(marca)
        dic_produtos['preco'].append(preco)

    print(url_pag)


df = pd.DataFrame(dic_produtos)
df.to_csv('preco_celular.csv', encoding='utf-8', sep=';')




