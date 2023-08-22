from django.shortcuts import render
from django.http import HttpResponse
import random

#Create your views here

def home(request):
    return render(request,'generator/home.html') 



def password(request):
    """
    This view generates a random password.
    The user has an option to insert the following character sets in the generated password, in addition to the lowercase characters:
        1. Uppercase
        2. Numbers
        3. Special Characters.
    """

    
    characters=list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))


    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    length=int(request.GET.get('length',12))
    password=''
    for x in range(length):
        password+=random.choice(characters) 

    return render(request,'generator/password.html',{'password':password}) 


def about(request):
    return render(request,'generator/about.html')
    