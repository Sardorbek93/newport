from http.client import responses

import requests
#Библиотека
# Парсинг - автоматизированный сбор и структурирование информации с сайтов при помощи программы или сервиса.
# это программа называется Парсер. Визуальную информацию превращаем в код
url = "https://aliexpress.ru/item/1005006445648728.html?spm=a2g2w.home.10009201.3.42b1558659lXCG&mixer_rcmd_bucket_id=aerabtestalgoRecommendAbV2_testVectorSearchW2vOrdersHome&ru_algo_pv_id=8c4d44-bbf0ce-061b0e-9725ba-1728129600&scenario=aerAppJustForYouNewJVSellTab&sku_id=12000037195869546&traffic_source=recommendation&type_rcmd=core"
response = requests.get(url) #

print(response.text)


