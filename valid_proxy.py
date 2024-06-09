import requests

with open("valid_proxy.txt","r") as f:
    proxies=f.read().splitlines()
    
sites_to_check=["https://books.toscrape.com/",
                "https://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html"]

counter=0

for site in sites_to_check:
    try:
        print(f"Using the proxy: {proxies[counter]}")
        res=requests.get(site, proxies={"http":proxies[counter],
                                        "https":proxies[counter]})
        print(res.status_code)
        print(res.text)
    
    except:
        print("failed")
    finally:
        counter+=1
        counter % len(proxies)