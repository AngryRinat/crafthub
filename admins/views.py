from django.shortcuts import render

def adminstaff(request):
    return render(request, 'admins/index.html')
