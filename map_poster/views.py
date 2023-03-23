from django.shortcuts import render
from django.http import HttpResponse


def show_main(request):

    return render(request, 'index.html')
