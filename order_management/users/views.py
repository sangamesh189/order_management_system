from django.shortcuts import render
from .models import CustomUser
# Create your views here.
from .serializer import token_obtain_pair_serializer
from .serializer import register_serializer
from .serializer import ProfileSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response


class login_token_view(TokenObtainPairView):
    serializer_class = token_obtain_pair_serializer

class register_view(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = register_serializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profile(request):
    user = request.user
    serializer = ProfileSerializer(user,many = False)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_profile(request):
    user = request.user
    serializer = ProfileSerializer(user,data = request.data,partial = True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer._errors,status=400)


