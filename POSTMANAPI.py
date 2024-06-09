import requests
import pandas as pd
def get_json():
    url = "https://catalog.chaldal.com/searchOld"

    payload = "{\r\n    \"apiKey\": \"e964fc2d51064efa97e94db7c64bf3d044279d4ed0ad4bdd9dce89fecc9156f0\",\r\n    \"storeId\": 1,\r\n    \"warehouseId\": 8,\r\n    \"pageSize\": 300,\r\n    \"currentPageIndex\": 0,\r\n    \"metropolitanAreaId\": 1,\r\n    \"query\": \"\",\r\n    \"productVariantId\": -1,\r\n    \"bundleId\": {\r\n        \"case\": \"None\"\r\n    },\r\n    \"canSeeOutOfStock\": \"false\",\r\n    \"filters\": [\r\n        \"numOfferPicturesUrls%3E0\"\r\n    ],\r\n    \"maxOutOfStockCount\": {\r\n        \"case\": \"Some\",\r\n        \"fields\": [\r\n            5\r\n        ]\r\n    },\r\n    \"shouldShowAlternateProductsForAllOutOfStock\": {\r\n        \"case\": \"Some\",\r\n        \"fields\": [\r\n            true\r\n        ]\r\n    },\r\n    \"customerGuid\": {\r\n        \"case\": \"None\"\r\n    }\r\n}"
    headers = {
    'accept': 'application/json',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,fr;q=0.6',
    'cache-control': 'no-cache',
    'content-type': 'application/json, application/json',
    'cookie': '_ga=GA1.2.742829191.1717774129; _gid=GA1.2.654246782.1717774129; cf_clearance=V3RDsjbcAQRFBvFPaGsmnh.obHzcBV6ieRMzwDmiiiM-1717774417-1.0.1.1-2z74cB0WXB67vSgSaAFaGn6jRmby0zVbpHAVx4BgiGWlDpIyvAhh9wtUJCt1J5QL0xgTM.F25RX2RBMtKTryHw',
    'origin': 'https://chaldal.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://chaldal.com/',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    # print(response.text)
    return response.json()


def save_to_csv(data):
    if data: 
        df=pd.json_normalize(data)
        df.to_csv('chaldal.csv')
        
def main():
    data=get_json()
    save_to_csv(data.get('hits'))
    print('done')
    
if __name__=='__main__':
    main()