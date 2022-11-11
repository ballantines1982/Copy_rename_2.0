from webbrowser import get
from bs4 import BeautifulSoup
import requests



def main(artnr):
    url = 'https://staplesnetshop.se/web/ePortal/ctrl?action=showiteminfo&itemNo=' + str(artnr) + '&loc=homepage'
    pages = requests.get(url)
    soup = BeautifulSoup(pages.content, 'html.parser')

    result = soup.find(id="PcItemDetail")
    print(result.prettify())
    # text_elements = result.find_all('div', class_="s-product-tabs__html-content")
    # for e in text_elements:
    #     print(e.text)
    
    
    
main(244936)