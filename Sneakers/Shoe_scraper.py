#Shoe website data scraper, based on the tutorial by YasCode found at https://youtu.be/aCeoJ3PYIak

import requests
import json
import csv


for anchor in range(0,700):
    count = 60
    url = f'https://api.nike.com/cic/browse/v2?queryid=products&anonymousId=420602656827166B35A8017BFC81DF34&country=us&endpoint=%2Fproduct_feed%2Frollup_threads%2Fv2%3Ffilter%3Dmarketplace(US)%26filter%3Dlanguage(en)%26filter%3DemployeePrice(true)%26filter%3DattributeIds(16633190-45e5-4830-a068-232ac7aea82c%2C0f64ecc7-d624-4e91-b171-b83a03dd8550)%26anchor%3D{anchor}%26consumerChannelId%3Dd9a5bc42-4b9c-4976-858a-f159cf99c647%26count%3D{count}&language=en&localizedRangeStr=%7BlowestPrice%7D%20%E2%80%94%20%7BhighestPrice%7D'
    html = requests.get(url = url)
    output=json.loads(html.text)
    for item in output['data']['products']['products']:
        print(item['title'])
        print(item['subtitle'])
        print(item['price'])
        print(item['colorDescription'])
        print(item['colorways'])
        print(item['inStock'])
        print(item['productType'])
        print(item['pid'])
    anchor = anchor + 60
    print(anchor)

output = str(output)

#testfile1 = output
#with open("testfile1.csv", 'w', newline = "") as file:
 #   file.write(testfile1 + "\n")




adidas_url = f'https://www.adidas.com/api/search/product/'
adidas_html = requests.get(url = adidas_url)
adidas_output = json.loads(adidas_html.text)

#f = open("adidas_data.txt", "w")
#f.write(adidas_html.text)
#f.close()
