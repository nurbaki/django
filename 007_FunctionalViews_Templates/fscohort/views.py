from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

# def home(request):
#     print("request.user : ", request.user)
#     html = request.GET.get("name")
#     return HttpResponse(html)




def home(request):

    context = {
        'company': 'clarusway',
        'dict1': {'django': 'best framework'},
        'my_list': [2, 3, 4]
    }


    return render(request, "fscohort/home.html", context)