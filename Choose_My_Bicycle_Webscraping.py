from bs4 import BeautifulSoup as soup                             #import BeautifulSoup package
from urllib.request import Request, urlopen                       #import request package
from ChooseMyBicycle_firestore import firestore_choosemybicycle

def choosemybicycle():
      req = Request('https://www.choosemybicycle.com/en/bicycles/e-bicycles', headers={'User-Agent': 'Mozilla/5.0'})    #request to url for data extraction
      webpage = urlopen(req).read()       #Read url data
      page_soup=soup(webpage,"html.parser") #parser is used to convert into html
      containers=page_soup.findAll("div",{"class":"productCard"})
      container=containers[0]
      list=[]                             #List is used to store product name,price,Image,reference
      for container in containers:
            name=container.findAll("span",{"class":"productName"})      #for getting product name
            name_1=name[0].text.strip()

            price=container.findAll("span",{"class":"sellingPrice"})
            price_1=price[0].text.strip()
            price_1=price_1.replace("₹","")
            price_1=price_1.replace(",","")                             #for getting product price

            for i,j in zip(container.find_all('a',href=True),container.findAll("div",{"class":"imageContainer"})): 
                  x=i['href']
                  y="https://www.choosemybicycle.com/"+str(x)           #for getting product reference

                  a=j['data-img']
                  b="https://s3.ap-south-1.amazonaws.com/choosemybicycle"+str(a)    #for getting product image
                               
            list.append({"Name":name_1,"Price":price_1,"Image":b,"Reference":y})#appending to list product name.price,image,url in dictionary format
      
      dict_choosemybicycle={}
      dict_choosemybicycle["Products"]=list
      firestore_choosemybicycle(dict_choosemybicycle)











