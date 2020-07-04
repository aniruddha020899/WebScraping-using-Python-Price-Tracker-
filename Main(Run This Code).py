import firebase_admin                   #
from firebase_admin import credentials  #  libraries for firebase Setup
from firebase_admin import firestore    # 
import configparser                                             #import configparser for reading ini file
from Choose_My_Bicycle_Webscraping import choosemybicycle       #from Choose_My_Bicycle_Webscraping file import choosemybicycle function
from ElektronCycles_Webscraping import elektroncycles           #from ElektronCycles_Webscraping import elektroncycles function
from Amazon_WebScraping import amazon                           #from Amazon_WebScraping function import amazon function
from Flipkart_WebScraping import flipkart

cred = credentials.Certificate(r'C:\Users\aniru\Downloads\rosy-house-264304-firebase-adminsdk-2h4ly-ea56979eae.json') #Credentials of firebase
firebase_admin.initialize_app(cred)                             #initializing firebase app
    

# Reading ini file
config = configparser.ConfigParser()
config.read(r'C:\Users\aniru\PycharmProjects\Web_Scraping_for_E-Bikes/Enter_Site_and_Product_in_ini_file.ini')    #For Reading data from ini file

'Web_Sites' in config                                                   #Web sites section in ini file
website=config['Web_Sites']['list_of_sites']                            #keys of website section
website=website.split(":")                                              #split websites

for i in website:                                                       #for loop for getting every combination of website and product

    if (i=="choosemybicycle" or i=="CHOOSEMYBICYCLE"):                  #if website section contains choosemybicycle
        
        'Choose_my_bicycle' in config                                   #access Choose_my_bicycle section
        product=config['Choose_my_bicycle']['list_of_product']
        choosemybicycle()
                
    if (i=="elektroncycles" or i=="ELEKTRONCYCLES"):                    #if website section contains elektroncycles
        
        'Elektroncycles' in config                                      #access Elektroncycles section
        product=config['Elektroncycles']['list_of_product']
        elektroncycles()

    if (i=="amazon" or i=="AMAZON"):                                    #if website section contains amazon

        'Amazon' in config                                              #access Amazon section
        product=config['Amazon']['list_of_product']
        product=product.split(":")                                      #Split function is used to separate one product from other 
        for j in product:
            amazon(j)

    if (i=="flipkart" or i=="FLIPKART"):                                #if website section contains flipkart
        
        'Flipkart' in config                                            #access FLipkart section                             
        product=config['Flipkart']['list_of_product']                  
        product=product.split(":")                                      #Split function is used to separate one product from other
        for j in product:
            flipkart(j)
            
            
#Commented the entire procedure of choosemybicycle webscraping,storing in cloud firestore and the teams notifications part.
#The comments for amazon,flipkart,elektroncycles remains the same.Hence no comments is done  
        
        
    

















    
