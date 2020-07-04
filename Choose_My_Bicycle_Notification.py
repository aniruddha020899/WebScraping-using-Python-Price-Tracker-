#Here we first compare the product names present in old data and new data if the product name match we see if the price is different
#of same product we sent a notification on microsoft teams

import pymsteams

def Price_comparison_choosemybicycle(old_data,new_data):
    x=old_data["Products"]                              
    old_data__=[k["Name"] for k in x if k.get("Name")]
    old_data_length=len(old_data__)                     #length of latest date data(i.e. number of products present)
    y=new_data["Products"]
    new_data__=[k["Name"] for k in y if k.get("Name")]
    new_data_length=len(new_data__)                     #length of today's day data
    for i in range(0,new_data_length):
        for j in range(0,old_data_length):
            if(new_data["Products"][i]["Name"]==old_data["Products"][j]["Name"]):       #if the product name matched
                if(new_data["Products"][i]["Price"]!=old_data["Products"][j]["Price"]): #if the price is different of same prodcut
                    print("Price Changed")                                      #print price changed and send a notificaton on teams
                    myTeamsMessage = pymsteams.connectorcard("https://outlook.office.com/webhook/c773f8b0-dfb8-4ba1-bde6-3742af93d8d9@8c4858b5-f020-483a-b7ef-71ded6e81767/IncomingWebhook/4ac039be94c64aa28e53f448e7571982/57e1e599-de0e-4e8f-be89-4f86146ae25c")
                    myMessageSection = pymsteams.cardsection()
                    myTeamsMessage.title("PRICE CHANGED   (website:Choose My Bicycle)") #title of notification
                    myTeamsMessage.text("```Name```:" +new_data["Products"][i]["Name"]) #name of product whose price changed
                    myMessageSection.text("```old price```:"+str(old_data["Products"][j]["Price"])+"```new price```:"+str(new_data["Products"][i]["Price"]))
                    #(product old price and product new price)
                    myTeamsMessage.addLinkButton("Reference",new_data["Products"][i]["Reference"])  #reference button 
                    myTeamsMessage.addSection(myMessageSection)
                    myMessageSection.addImage(new_data["Products"][i]["Image"]) #Image of the product
                    myTeamsMessage.send()
               
