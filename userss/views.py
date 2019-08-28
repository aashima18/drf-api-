from django.shortcuts import render
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from userss.models import User,Item
from userss.serializers import UserSerializer,ItemSerializer,LoginSerializer
import json
from rest_framework.decorators import api_view
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

from rest_framework import status
from rest_framework.views import APIView

def index(request):
   return render(request, 'regis.html')    

def indexx(request):
   return render(request, 'item.html')  

def indexxx(request):
   return render(request, 'signup.html')  


def indexl(request):
   return render(request, 'iteml.html')   

class UserCreateAPIView(generics.CreateAPIView):
   
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)



@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    serializer = LoginSerializer(request.data)
    username = request.data["username"]
    password = request.data["password"]
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,)) 
def logout(request):
    request.user.auth_token.delete()
    return Response(status=status.HTTP_200_OK)


@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes((AllowAny,))
# @authentication_classes((TokenAuthentication,))
def item_list(request):
   
    if request.method == 'GET':
        items = Item.objects.filter(user_s=request.user.id)
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ItemSerializer(data=request.data)
        title = request.data["title"]
        description = request.data["description"]
        if serializer.is_valid():
            serializer.save(user_s=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# @csrf_exempt
# @api_view(["POST"])
# @permission_classes((AllowAny,))
# def signup(request):
#     serializer = UserSerializer(request.data)
#     username = request.data["username"]
#     first_name = request.data["first_name"]
#     last_name = request.data["last_name"]
#     email = request.data["email"]
#     password = request.data["password"]
#     token, _ = Token.objects.get_or_create(user=user)
#     return Response({'token': token.key},
#                     status=HTTP_200_OK)


















