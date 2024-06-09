import requests
import json
import pandas as pd
#json links
res=requests.get('https://www.brewersassociation.org/wp-content/themes/ba2019/json-store/breweries/breweries.json?nocache=1717430850402')
print(res.status_code)

# print(len(res.text))

# print(res.text[:200])   #print 200 characters
# print(type(res.json()))   #it is a type of list
# print(res.json()[:100])
# print(type(json.loads(res.json())))   no need to load as it is already parsed
data=res.json()
# print(data)
# print(type(data))
results=[]

def e_billing_info(bill):
    billing_info=bill.get('BillingAddress', {})
    return list(billing_info.values())
    
for i in data[:10]:
    name=i.get('Name','No name')
    phone=i.get('Phone','No phone')
    brewery_type=i.get('Brewery_Type__c','No type')
    billing_address=e_billing_info(i)
    
    # print({name})
    # print({phone})
    # print({brewery_type})
    # print(f"{billing_address}")   #f here stands for format string
    
    results.append({'Name':name,
            'Phone':phone,
            'Brewery_Type':brewery_type,
            'BillingAddress':billing_address
            })
    
df=pd.DataFrame(results)

print(df.head())
print(df.shape)   #gives rows*columns

df.to_csv("infinite_scroll_brewery.csv", index=False)
