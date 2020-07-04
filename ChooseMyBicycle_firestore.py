#In this firestore_choosemybicycle function,
#1.first we get the latest date data from cloud firestore and convert it into dictionary format
#and then store today's data in cloud firestore
#Then we pass latest date data and today's data to other function

import datetime                     
import firebase_admin                     #
from firebase_admin import credentials    #for firebase setup
from firebase_admin import firestore      #
from Choose_My_Bicycle_Notification import Price_comparison_choosemybicycle

def firestore_choosemybicycle(dict_choosemybicycle):
      
      u = datetime.datetime.now()
      Date=u.strftime("%d") + "-" + u.strftime("%b") + "-" + u.strftime("%Y")   #for getting today's Date   
      #Date= (u.strftime("%H") + "-" + u.strftime("%M"))  # Time for checking code
      db = firestore.client()
      abcd = db.collection_group(u'Choose My Bicycle')      #take the latest date present in document section of collection choosemybicycle
      docs = abcd.stream()
      x={}
      for doc in docs:
            x=(u'{}'.format(doc.id))                        
      #print(x)

      db.collection(u'Choose My Bicycle').document(Date).set(dict_choosemybicycle)  #Store today's data in cloud firestore
      
      doc_ref_older = db.collection(u'Choose My Bicycle').document(x) #\ converting latest date data into dict
      old_data = doc_ref_older.get().to_dict()                        #/
      doc_ref = db.collection(u'Choose My Bicycle').document(Date)    #\converting today's date data into dict
      new_data = doc_ref.get().to_dict()                              #/

      Price_comparison_choosemybicycle(old_data,new_data)   #Passing latest data and today's date data to a function present in another file
    
