from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from datetime import datetime


def index(request):
    strResponse = (
            '<p style="color:yellow; background: blue; font-size:40px; ">Nắng vàng lung linh, '
            '<br/> mùa hè đang đến, ve kêu ra rả ... : '
            + datetime.now().strftime('%A, %d-%B-%Y %H:%M:%S')
            + '</p>'
    )

    return HttpResponse(strResponse)
