from bs4 import BeautifulSoup as soup                 #import bs4 package
from urllib.request import urlopen as uReq            #import urllib package
from Flipkart_firestore import firestore_flipkart


def flipkart(j):     #j is the product
    
    y = "https://www.flipkart.com/search?q="                        # url for amazon site
    z = y + str(j)                  # string concatenation of amazon url and product
    uClient = uReq(z)                   # (WEB SCRAPPING OF AMAZON)         #request to url for extraction
    page_html = uClient.read()          # Read url
    uClient.close()
    page_soup = soup(page_html, "html.parser")              # html parsing

    containers = page_soup.findAll("div", {"class": "_3liAhj"})        # Extracting product name

    try:                                                                #Using exception Handling
        container = containers[0]
        list=[]
        for container in containers:                            # for loop for extracting all product name and price
            product_name_flipkart = container.img['alt']          # Extracting product name

            price_container = container.findAll("div", {"class": "_1vC4OE"})

            price = price_container[0].text.strip()             # extracting product price

            trim_price = ''.join(price.split(','))
            rm_rupee = trim_price.split("₹")
            add_rs_price = rm_rupee[1]  # String parsing for displaying name of product and
            split_price = add_rs_price.split('E')  # its price
            final_price_flipkart = split_price[0]
            
            for i in container.find_all('a', href=True):
                x = i['href']
                product_reference = "https://www.flipkart.in" + str(x)
                list.append({"Name":product_name_flipkart,"Price":final_price_flipkart,"Reference":product_reference})
                break
        dict_flipkart={}
        dict_flipkart["Products"]=list
        firestore_flipkart(dict_flipkart)
    except IndexError:
        print("Product Not available")











