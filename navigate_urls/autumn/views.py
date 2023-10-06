from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from datetime import datetime


def index(request):
    strResponse = (
            '<p style="color:magenta; font-size:40px; ">Mùa thu nhẹ nhàng, '
            '<br/> lá rơi êm đềm ... '
            + '<br/> ~ ' + datetime.now().strftime('%A, %d-%B-%Y %H:%M:%S')
            + '</p>'
    )

    return HttpResponse(strResponse)


def listInAutumn(request):
    strResponse = (
            '<p style="color:magenta; font-size:40px; ">Mùa thu nhẹ nhàng, '
            '<br/> lá rơi êm đềm ... '
            + '<br/> ~ ' + datetime.now().strftime('%A, %d-%B-%Y %H:%M:%S')
            + '</p>'
            + '<br/>   ------------ DANH SÁCH CHO MÙA HÈ ---------'
            + '<br/>   --------> Chuyên mục 1 ---------'
            + '<br/>   --------> Chuyên mục 2 ---------'
    )

    return HttpResponse(strResponse)
