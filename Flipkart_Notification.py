import pymsteams

def Price_comparison_flipkart(old_data,new_data):
    x=old_data["Products"]
    old_data__=[k["Name"] for k in x if k.get("Name")]
    old_data_length=len(old_data__)
    y=new_data["Products"]
    new_data__=[k["Name"] for k in y if k.get("Name")]
    new_data_length=len(new_data__)
    for i in range(0,new_data_length):
        for j in range(0,old_data_length):
            if(new_data["Products"][i]["Name"]==old_data["Products"][j]["Name"]):
                if(new_data["Products"][i]["Price"]!=old_data["Products"][j]["Price"]):
                    print("Price Changed")
                    myMessageSection = pymsteams.cardsection()
                    myTeamsMessage = pymsteams.connectorcard("https://outlook.office.com/webhook/c773f8b0-dfb8-4ba1-bde6-3742af93d8d9@8c4858b5-f020-483a-b7ef-71ded6e81767/IncomingWebhook/4ac039be94c64aa28e53f448e7571982/57e1e599-de0e-4e8f-be89-4f86146ae25c")
                    myTeamsMessage.title("PRICE CHANGED(website:Flipkart)")
                    myTeamsMessage.text("```Name```:" +new_data["Products"][i]["Name"])
                    myMessageSection.text("```old price```:"+str(old_data["Products"][j]["Price"])+"```new price```:"+str(new_data["Products"][i]["Price"]))
                    myTeamsMessage.addLinkButton("Reference",new_data["Products"][i]["Reference"])
                    myTeamsMessage.addSection(myMessageSection)
                    #myMessageSection.addImage(new_data["Products"][i]["Image"])
                    myTeamsMessage.send()
