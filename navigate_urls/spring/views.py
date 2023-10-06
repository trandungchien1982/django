from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from datetime import datetime


def index(request):
    strResponse = (
            '<p style="color:lightgreen; font-size:40px; ">Mùa xuân ấm áp nhẹ nhàng, '
            + '<br/> giọt sương rơi trên lá ...  '
            + '<br/> ~ ' + datetime.now().strftime('%A, %d-%B-%Y %H:%M:%S')
            + '</p>'
    )

    return HttpResponse(strResponse)

def listInSpring(request):
    strResponse = (
            '<p style="color:lightgreen; font-size:40px; ">Mùa xuân ấm áp nhẹ nhàng, '
            + '<br/> giọt sương rơi trên lá ...  '
            + '<br/> ~ ' + datetime.now().strftime('%A, %d-%B-%Y %H:%M:%S')
            + '</p>'
            + '<br/> Danh sách của mùa xuân ...'
            + '<br/> ------- Thành phần 01'
            + '<br/> ------- Thành phần 02'
    )

    return HttpResponse(strResponse)
