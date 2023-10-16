from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from datetime import datetime


from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from models import Post

# Định nghĩa model cần serialize và các trường, ở đây mình để là all
# Có rất nhiều API class mà rest đã impl sẵn,
#   ở đây mình chỉ dùng 2 class để thao tác CRUD với Database
class PostListSerializier(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

# API get detail, update, delete
class PostDetailUpdateAPIView(viewsets.GenericViewSet, RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializier
    lookup_field = 'id'
    # permission_classes = [IsAuthenticated]

# API get list and create
class PostListCreateAPIView(viewsets.GenericViewSet, ListCreateAPIView):
    serializer_class = PostListSerializier
    queryset = Post.objects.all()



def index(request):
    strResponse = (
            '<p style="color:lightgreen; font-size:40px; ">Mùa xuân ấm áp nhẹ nhàng, '
            + '<br/> giọt sương rơi trên lá ...  '
            + '<br/> ~ ' + datetime.now().strftime('%A, %d-%B-%Y %H:%M:%S')
            + '</p>'
    )

    return HttpResponse(strResponse)


def listInRestful(request):
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


def getAPI():
    return 'Get dataAPI'
