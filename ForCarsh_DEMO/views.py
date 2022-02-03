from django.shortcuts import render
import pyrebase

firebaseConfig={ 'apiKey': "AIzaSyD3qcCh1MxUoiqk7dld7hLuGVmx--ri3hY",
  'authDomain': "forcrashdemo.firebaseapp.com",
  'databaseURL': "https://forcrashdemo-default-rtdb.firebaseio.com",
  'projectId': "forcrashdemo",
  'storageBucket': "forcrashdemo.appspot.com",
  'messagingSenderId': "216908476609",
  'appId': "1:216908476609:web:872afce2e6255e1e1fe440",
  'measurementId': "G-FJMZLMD0ZY"

}
firebase=pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()
database=firebase.database()
# Create your views here.
def hello(request):
    db_name = database.child('Member').child('Name').get().val()
    db_surname = database.child('Member').child('Surname').get().val()
    return render(request,'index.html',{
        'db_name' : db_name,
        'db_surname':db_surname     
    })
def Page1(request):
    return render(request,'Page1.html')