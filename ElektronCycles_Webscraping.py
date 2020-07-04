from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from ElektronCycles_firestore import firestore_elektroncycles

def elektroncycles():
    my_url="https://elektroncycles.in/"
    uClient=uReq(my_url)
    page_html=uClient.read()
    uClient.close()
    page_soup=soup(page_html,"html.parser")
    containers=page_soup.findAll("div",{"class":"grid__item grid-product medium--one-half large--one-third"})
    container=containers[0]
    list=[]
    for container in containers:
        name = container.findAll("span", {"class": "grid-product__title"})
        name_1=name[0].text.strip()

        price = container.findAll("span", {"class": "grid-product__price"})
        price_1=price[0].text.strip()
        price_2=price_1.split(".")
        price_3=price_2[1]
        price_4=price_3.replace(' ','')
        price_5=price_4.split("\n")
        price_6=price_5[0]
        price_6=price_6.replace(",","")

        for i,j in zip(container.find_all('a',href=True),container.findAll("img")):
            x=i['href']
            y="https://elektroncycles.in"+str(x)

            a=j['src']
            break
        list.append({"Name":name_1,"Price":price_6,"Image":a,"Reference":y})

    dict_elektroncycles={}
    dict_elektroncycles["Products"]=list
    firestore_elektroncycles(dict_elektroncycles)









