from django.contrib.auth import authenticate, login as auth_login ,logout as auth_logout
from rest_framework import status  
from rest_framework.decorators import api_view  
from rest_framework.response import Response  
from .models import Profile  
from .serializers import ProfileSerializer, UserRegisterSerializer  

@api_view(['POST'])  
def login(request):  
    if request.method == 'POST':  
        username = request.data.get('username')  
        password = request.data.get('password')  
        user = authenticate(request, username=username, password=password)  

        if user is not None:  
            auth_login(request, user)  
            profile = Profile.objects.get(user=user)   
            serializer = ProfileSerializer(profile)   
            return Response(serializer.data, status=status.HTTP_200_OK)  
        else:  
            return Response({'error': 'Invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])  
def register(request):  
    if request.method == 'POST':  
        serializer = UserRegisterSerializer(data=request.data)  
        if serializer.is_valid():  
            user = serializer.save() 
            Profile.objects.create(user=user)  
            
            return Response({  
                'id': user.id,  
                'username': user.username,  
                'email': user.email  
            }, status=status.HTTP_201_CREATED)  
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])  
def logout(request):  
    if request.method == 'POST':  
        auth_logout(request)  
        return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)  