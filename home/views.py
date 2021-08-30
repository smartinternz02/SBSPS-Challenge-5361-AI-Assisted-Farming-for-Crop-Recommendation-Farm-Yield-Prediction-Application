from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from csv import writer
from datetime import datetime

# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    if request.method=='POST':
        feedback=str(request.POST["text"])
        print(feedback)

        now = datetime.now()
        d = now.strftime("%B %d, %Y")
        dt_string = now.strftime("%b-%d-%Y %H:%M:%S")
        List=[dt_string,feedback]

        with open('feedback.csv', 'a') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(List)
            f_object.close()
        messages.info(request,'Thank You for Feedback!')
        return render(request,'home.html')
    return render(request,'about.html')

