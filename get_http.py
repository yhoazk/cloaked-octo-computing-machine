from bs4 import BeautifulSoup
import requests
import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'}

with requests.Session() as s:
      baseurl = 'https://ds.suning.com/ds/generalForTile/000000010606656239_,000000000690128135_,000000010606649857_,000000010597840415_,000000010597840391_-010-2-0000000000-1--ds0000000002391.json'
      url_fetch = s.get(baseurl, headers=headers).json()
      print([rs['price'] for rs in url_fetch['rs']])

      #['5588.00', '5988.00', '7188.00', '7688.00', '5188.00']
