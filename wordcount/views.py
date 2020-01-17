from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('Hello, Django!')


def count(request):
    return render(request, 'count.html')


def show(request):
    text = request.POST['text']
    length = len(text.split())
    splitted_text = text.split()
    mydict = {}
    for word in splitted_text:
        if word not in mydict:
            mydict[word] = 1
        else:
            mydict[word] += 1

    mydict = mydict.items()
    return render(request, 'show.html', {'text': text, 'words': length, 'fulldictionary': mydict})


def about(request):
    return render(request, 'about.html')
