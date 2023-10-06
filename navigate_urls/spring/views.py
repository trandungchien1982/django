from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from datetime import datetime


def index(request):
    strResponse = (
            '<p style="color:lightgreen; font-size:40px; ">Mùa xuân ấm áp nhẹ nhàng, '
            '<br/> giọt sương rơi trên lá ... : '
            + datetime.now().strftime('%A, %d-%B-%Y %H:%M:%S')
            + '</p>'
    )

    return HttpResponse(strResponse)
