from django.shortcuts import render
import datetime

# Create your views here.

def blog(request):    
    val = {
        'day': ['Saturday', 'Sunday', 'Monday', 'Tuesday' , 'Wednesday', 'Thursday', 'Friday'],
        'dt': datetime.datetime.now(),
        'tm': datetime.datetime.now(),
        'add': 10,
        'nm': 'bangladesh',
        'cutting': "Saturday, - Sunday, - Monday, - Tuesday, - Wednesday, - Thursday, - Friday",
        'dictsorts': [
            {'name': 'Rahim', 'age': 25},
            {'name': 'Karim', 'age': 22},
            {'name': 'Salam', 'age': 35},
            {'name': 'Jobbar', 'age': 30},
        ], 
        'firsts': ['banana', 'pineapple', 'orange'],
        'lasts': ['banana', 'pineapple', 'orange'],        
        'some_list': ['banana', 'pineapple', 'orange'],        
        'len': ['banana', 'pineapple', 'orange'],
        'linenum': ['banana', 'pineapple', 'orange'],
        'low': 'This is Django Website.',
        'up': 'this is django website.',
        'titles': 'this is django website.',
        'trances': 'this is django website.',
        'wrdcnt': 'this is django website.',
        'trancewrd': 'this is django website.',
        'strip': 'this is django website.',
        'randm': ['banana', 'pineapple', 'orange'],
        'num_message': 2,
        
    }
    return render(request, 'practice_app/blogs.html', val)

    
