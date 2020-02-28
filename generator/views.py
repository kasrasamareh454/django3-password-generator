from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.



def home(request) :
    return render(request , 'generator/home.html')




def password(request) :

    

    charecters = list('qwertyuioplkjhgfdsazxcvbnm')


    if request.GET.get('uppercase') :
        charecters.extend(list('QWERTYUIOPLKJHGFDSAZXCVBNM'))
    
    
    
    if request.GET.get('numbers') :
        charecters.extend(list('0123456789'))

    
    if request.GET.get('sepecial') :
        charecters.extend(list('!@#$%^&*'))
    
    
    length = int(request.GET.get('length',12))


    thepassword = ''
    
    for x in range(length) :
        thepassword += random.choice(charecters)
    
    
    return render(request , 'generator/password.html' , {'password' : thepassword})





def about (request) :
    return render (request , 'generator/about.html')