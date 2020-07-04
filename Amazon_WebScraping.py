from bs4 import BeautifulSoup as soup                 #import bs4 package
from urllib.request import urlopen as uReq            #import urllib package
from Amazon_firestore import firestore_amazon                       



def amazon(j):   #j is the product

    y = "https://www.amazon.in/s?k="                        # url for amazon site
    z = y + str(j)                  # string concatenation of amazon url and product
    uClient = uReq(z)                   # (WEB SCRAPPING OF AMAZON)         #request to url for extraction
    page_html = uClient.read()          # Read url
    uClient.close()
    page_soup = soup(page_html, "html.parser")              # html parsing

    containers = page_soup.findAll("div", {"class": "s-include-content-margin s-border-bottom"})      # Extracting product name
    
    try:                                                                                #Using exception Handling
        container = containers[0]
        list=[]
        for container in containers:                            # for loop for extracting all product name and price
            product_name_amazon = container.img['alt']          # Extracting product name

            price_container = container.findAll("div", {"class": "a-row a-size-base a-color-base"})
            price = price_container[0].text.strip()             # extracting product price

            trim_price = ''.join(price.split(','))
            rm_rupee = trim_price.split("₹")
            add_rs_price = rm_rupee[1]  # String parsing for displaying name of product and
            split_price = add_rs_price.split('E')  # its price
            final_price_amazon = split_price[0]

            for i in container.find_all('a', href=True):
                x = i['href']
                product_reference = "https://www.amazon.in" + str(x)
                break
            for i in container.findAll("img",{"class":"s-image"}):
                y=i['src']

            list.append({"Name":product_name_amazon,"Price":final_price_amazon,"Image":y,"Reference":product_reference})

        dict_amazon={}
        dict_amazon["Products"]=list
        firestore_amazon(dict_amazon)
    except IndexError:
        print("Product Not Available")











