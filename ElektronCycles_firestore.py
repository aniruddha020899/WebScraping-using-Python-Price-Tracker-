import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from ElektronCycles_Notification import Price_comparison_elektroncycles

def firestore_elektroncycles(dict_elektroncycles):
    
    db = firestore.client()
    
    u = datetime.datetime.now()
    Date=u.strftime("%d") + "-" + u.strftime("%b") + "-" + u.strftime("%Y")
    #Date= (u.strftime("%H") + "-" + u.strftime("%M"))  # Date

    abcd = db.collection_group(u'ElektronCycles')
    docs = abcd.stream()
    x={}
    for doc in docs:
        x=(u'{}'.format(doc.id))
    #print(x)
    
    db.collection(u'ElektronCycles').document(Date).set(dict_elektroncycles)
    doc_ref_older = db.collection(u'ElektronCycles').document(x)
    
    old_data = doc_ref_older.get().to_dict()
    doc_ref = db.collection(u'ElektronCycles').document(Date)
    new_data = doc_ref.get().to_dict()

    Price_comparison_elektroncycles(old_data,new_data)
