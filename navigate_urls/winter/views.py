from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from datetime import datetime


def index(request):
    strResponse = (
            '<p style="color:white; font-size:40px; background: green; ">Tuyết rơi lạnh giá, '
            '<br/> mùa đông lặng lẽ trôi ...  '
            + '<br/> ~ ' + datetime.now().strftime('%A, %d-%B-%Y %H:%M:%S')
            + '</p>'
    )

    return HttpResponse(strResponse)


def listInWinter(request):
    strResponse = (
            '<p style="color:white; font-size:40px; background: green; ">Tuyết rơi lạnh giá, '
            '<br/> mùa đông lặng lẽ trôi ...  '
            + '<br/> ~ ' + datetime.now().strftime('%A, %d-%B-%Y %H:%M:%S')
            + '</p>'
            + '<br/> ---- Danh sách cho mùa đông: '
            + '<br/> ------- Gấu ngủ đông '
            + '<br/> ------- Trời lạnh giá '
            + '<br/> ------- Mau đói bụng ... '
    )

    return HttpResponse(strResponse)
