from rest_framework import serializers  
from django.contrib.auth.models import User  
from .models import Profile  
from django.contrib.auth import password_validation  
from django.utils.translation import gettext_lazy as _  

class UserSerializer(serializers.ModelSerializer):  
    # We do not include the password in the output  
    class Meta:  
        model = User  
        fields = ['id', 'username', 'email', 'first_name', 'last_name']  

    def create(self, validated_data):  
        # Create a user and hash the password  
        user = User(  
            username=validated_data['username'],  
            email=validated_data['email'],  
            first_name=validated_data.get('first_name', ''),  
            last_name=validated_data.get('last_name', ''),  
        )  
        user.set_password(validated_data['password'])  
        user.save()  
        return user  


class ProfileSerializer(serializers.ModelSerializer):  
    user = UserSerializer()  

    class Meta:  
        model = Profile  
        fields = ['id', 'user', 'profile_picture']  

    def create(self, validated_data):  
        user_data = validated_data.pop('user')  
        user_serializer = UserSerializer(data=user_data)  

        if user_serializer.is_valid():  
            user = user_serializer.save() 
            profile = Profile.objects.create(user=user, **validated_data) 
            return profile  
        else:  
            raise serializers.ValidationError(user_serializer.errors)  

    def update(self, instance, validated_data):  
        user_data = validated_data.pop('user', None)  
        if user_data:  
            user_serializer = UserSerializer(instance.user, data=user_data)  
            if user_serializer.is_valid():  
                user_serializer.save()  
            else:  
                raise serializers.ValidationError(user_serializer.errors)  
        
        # Update profile fields  
        instance.profile_picture = validated_data.get('profile_picture', instance.profile_picture)  
        instance.save()  
        return instance

class UserRegisterSerializer(serializers.ModelSerializer):  
    password1 = serializers.CharField(write_only=True)  
    password2 = serializers.CharField(write_only=True)  

    class Meta:  
        model = User  
        fields = ['username', 'email', 'password1', 'password2']  

    def validate(self, data):  
        if data['password1'] != data['password2']:  
            raise serializers.ValidationError(_("Passwords do not match."))  
        password_validation.validate_password(password=data['password1'])  
        return data  

    def create(self, validated_data):  
        user = User(  
            username=validated_data['username'],  
            email=validated_data['email']  
        )  
        user.set_password(validated_data['password1'])  
        user.save()  
        return user  