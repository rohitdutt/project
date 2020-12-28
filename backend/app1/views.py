from django.shortcuts import render
import  json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse,JsonResponse
from .models import User,Message
from .serializer import UserSerializer,MessageSerialzer
from django.views.decorators.csrf import csrf_exempt
'''@api_view(['GET', 'POST'])
def login(request):
    if request.method == 'POST':

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def profile(request,pk):
    if request.method=='GET':
        try:
            user=User.objects.get(user_id=pk)
            serialize=UserSerializer(user)
            return Response(serialize.data,status=200)
        except:
            return Response("404 error",status=404)
            '''
# Create your views here.
def index(request):
     #return render(request, 'chat/user.html')
   return render(request, 'chat/index.html')

'''def room(request, username):
    return render(request, 'chat/singleuser.html',context= {
            'userName' : username
    })'''
def room(request,userName):
    return render(request, 'chat/room.html', {
        'room_name': "myroom",
        'userName':userName
    })
'''def private(request):
    return render(request,'chat/private.html')

def private_chat(request,username,otheruser):
    return render(request,'chat/private_chat.html',context={
    'userName':username,
    'otheruser':otheruser,
    })
'''
    #return render(request, 'chat/room.html', {
    #    'room_name': room_name
    #})
