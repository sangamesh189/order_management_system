from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import CustomUser


class token_obtain_pair_serializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token['email'] = user.email
        token['role'] = user.role

        return token
    
from .models import CustomUser 
class register_serializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only = True , required = True, validators = [validate_password])
    password2 = serializers.CharField(
        write_only = True , required = True)
    
    email = serializers.EmailField(required = True,validators = [UniqueValidator(queryset = CustomUser.objects.all())])
    phone_number = serializers.CharField(
        write_only = False , required = False
    )
    address = serializers.CharField(
        write_only = False , required = False
    )
    

    class Meta:
        model = CustomUser
        fields = ('username','email','password','password2','address','phone_number')

    def validate(self,attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password":"password fields doesn't match"}
            )
        return attrs
    
    def create(self,validated_data):
        user = CustomUser.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            # phone_number = validated_data['phone_number'],
            # address = validated_data['address']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user
    
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

