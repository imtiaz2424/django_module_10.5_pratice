from django.shortcuts import render

# Create your views here.

def about(request):

    d = {'author' : 'Rahim', 'age': 20, 'list' : [1, 2, 3], 'courses' : [

         {
            'id' : 1,
            'name' : 'Python',
            'fee' : 5000

        },
         {
            'id' : 2,
            'name' : 'Django',
            'fee' : 2000

        },
         {
            'id' : 3,
            'name' : 'C++',
            'fee' : 6500

        },
    ],

    'list_django' : ['django', 'is', 'best', 'template']
    }
    return render(request, 'navigation/about.html', d)

def contact(request):
    return render(request, 'navigation/contact.html')
