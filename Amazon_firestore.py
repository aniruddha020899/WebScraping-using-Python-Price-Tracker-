import firebase_admin                   #
from firebase_admin import credentials  #  libraries firebase Setup
from firebase_admin import firestore    # 
import datetime 
from Amazon_Notification import Price_comparison_amazon
def firestore_amazon(dict_amazon):

    u = datetime.datetime.now()
    Date=u.strftime("%d") + "-" + u.strftime("%b") + "-" + u.strftime("%Y") #Date
    #Date= (u.strftime("%H") + "-" + u.strftime("%M"))  # Time for checking code

    db = firestore.client()    
    abcd=db.collection_group(u'Amazon')
    docs=abcd.stream()
    x={}
    for doc in docs:
        x=(u'{}'.format(doc.id))
    #print(x)
    
    db.collection(u'Amazon').document(Date).set(dict_amazon)
    doc_ref_older = db.collection(u'Amazon').document(x)
    
    old_data = doc_ref_older.get().to_dict()
    doc_ref = db.collection(u'Amazon').document(Date)
    new_data = doc_ref.get().to_dict()

    Price_comparison_amazon(old_data,new_data)


    
