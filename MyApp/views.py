from django.shortcuts import render
import datetime
# Create your views here.
def home( request ):
    dist = {'Name' : 'Baker', 'Age' : 12, 'L' : [4,5,6], 'employees' : [
        {
            'id' : 1,
            'name' : 'Baker',
            'Designation' : 'SubAM'
        },
        {
            'id' : 2,
            'name' : 'Faker',
            'Designation' : 'Technician'
        },
        {
            'id' : 3,
            'name' : 'Jaker',
            'Designation' : 'Foreman'
        }
    ], 'data' : ['c','is','good'], 'birtday' : datetime.datetime.now()
    }
    return render(request, 'home.html', dist)
