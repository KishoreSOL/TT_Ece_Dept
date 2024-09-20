import pymongo
from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017/')
db = client['ECE_DPT']
collection = db['student_mail_pass']


data = [
    {"name": "AADHAVAN G V", "email": "aadhavangv.22ece@kongu.edu", "password": "aadhavan@kec"},
    {"name": "ABHENATHAN S", "email": "abhenathans.22ece@kongu.edu", "password": "abhenathan@kec"},
    {"name": "ABHINAV R", "email": "abhinavr.22ece@kongu.edu", "password": "abhinav@kec"},
    {"name": "ABHINEVEASH S D", "email": "abhineveashsd.22ece@kongu.edu", "password": "abhineveash@kec"},
    {"name": "ABINASH M", "email": "abinashm.22ece@kongu.edu", "password": "abinash@kec"},
    {"name": "ABINAYA A S", "email": "abinayaas.22ece@kongu.edu", "password": "abinayaa@kec"},
    {"name": "ABINAYA P S", "email": "abinayaps.22ece@kongu.edu", "password": "abinayap@kec"},
    {"name": "ABINESH K", "email": "abineshk.22ece@kongu.edu", "password": "abinesh@kec"},
    {"name": "ABINITHY M", "email": "abinithym.22ece@kongu.edu", "password": "abinithy@kec"},
    {"name": "ABISHEK M", "email": "abishekm.22ece@kongu.edu", "password": "abishek@kec"},
    {"name": "ABZAANAA T", "email": "abzaanaat.22ece@kongu.edu", "password": "abzaanaa@kec"},
    {"name": "ADHISH K S", "email": "adhishks.22ece@kongu.edu", "password": "adhish@kec"},
    {"name": "ADITHYA R", "email": "adithyar.22ece@kongu.edu", "password": "adithya@kec"},
    {"name": "AISHWARYA G", "email": "aishwaryag.22ece@kongu.edu", "password": "aishwarya@kec"},
    {"name": "AJAY K S", "email": "ajayks.22ece@kongu.edu", "password": "ajay@kec"},
    {"name": "AKASH B", "email": "akashb.22ece@kongu.edu", "password": "akash@kec"},
    {"name": "AKSHAYA M", "email": "akshayam.22ece@kongu.edu", "password": "akshaya@kec"},
    {"name": "ALAGU DIVYA SHREE M", "email": "alagudivyashreem.22ece@kongu.edu", "password": "alagudivyashree@kec"},
    {"name": "AMIRTHA S", "email": "amirthas.22ece@kongu.edu", "password": "amirtha@kec"},
    {"name": "ARAVINTH B", "email": "aravinthb.22ece@kongu.edu", "password": "aravinth@kec"},
    {"name": "ARULNITHI E", "email": "arulnithie.22ece@kongu.edu", "password": "arulnithi@kec"},
    {"name": "ARUNESH K", "email": "aruneshk.22ece@kongu.edu", "password": "arunesh@kec"},
    {"name": "ARYAN P", "email": "aryanp.22ece@kongu.edu", "password": "aryan@kec"},
    {"name": "ASHIKA BANU M", "email": "ashikabanum.22ece@kongu.edu", "password": "ashikabanu@kec"},
    {"name": "ASHWIN R", "email": "ashwinr.22ece@kongu.edu", "password": "ashwin@kec"},
    {"name": "ASMEETHA BEGAM A", "email": "asmeethabegama.22ece@kongu.edu", "password": "asmeethabegam@kec"},
    {"name": "ASVANTHIKAA S P", "email": "asvanthikaasp.22ece@kongu.edu", "password": "asvanthikaa@kec"},
    {"name": "ASWANTH G", "email": "aswanthg.22ece@kongu.edu", "password": "aswanth@kec"},
    {"name": "ATHISH S K", "email": "athishsk.22ece@kongu.edu", "password": "athish@kec"},
    {"name": "AYISHA A", "email": "ayishaa.22ece@kongu.edu", "password": "ayisha@kec"}
]

# Insert the data into the collection
result = collection.insert_many(data)

print(f"Inserted {len(result.inserted_ids)} documents")

# Close the connection
client.close()