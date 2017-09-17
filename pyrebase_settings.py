import pyrebase

config = {
    "apiKey": "AIzaSyAr2E8ufRxOTNDwz92hyapuCsBdLOQ15tM",
    "authDomain": "track-5b168.firebaseapp.com",
    "databaseURL": "https://track-5b168.firebaseio.com",
    "projectId": "track-5b168",
    "storageBucket": "track-5b168.appspot.com",
    "messagingSenderId": "356977118606"
}
firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

user2 = auth.sign_in_with_email_and_password("leebet1@gmail.com", "p@ssw0rd")
db = firebase.database()
