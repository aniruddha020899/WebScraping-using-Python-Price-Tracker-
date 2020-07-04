import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime
from Flipkart_Notification import Price_comparison_flipkart
def firestore_flipkart(dict_flipkart):
    
    u = datetime.datetime.now()
    Date=u.strftime("%d") + "-" + u.strftime("%b") + "-" + u.strftime("%Y")
    #Date= (u.strftime("%H") + "-" + u.strftime("%M"))  # Date

    db = firestore.client()
    abcd=db.collection_group(u'Flipkart')
    docs=abcd.stream()
    x={}
    for doc in docs:
        x=(u'{}'.format(doc.id))
    #print(x)

    db.collection(u'Flipkart').document(Date).set(dict_flipkart)
    doc_ref_older = db.collection(u'Flipkart').document(x)
    
    old_data = doc_ref_older.get().to_dict()
    doc_ref = db.collection(u'Flipkart').document(Date)
    new_data = doc_ref.get().to_dict()

    Price_comparison_flipkart(old_data,new_data)
