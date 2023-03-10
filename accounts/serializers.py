

import re
from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class ProfileSerializer(serializers.ModelSerializer):
    birthdate = serializers.DateField(input_formats=['%d-%m-%Y'],format="%d-%m-%Y")
    class Meta:  
        model = Profile
        fields = ['bio', 'birthdate']

class USerSerializer(serializers.ModelSerializer):

    profile = ProfileSerializer(required = True)

    class Meta:  
        model = User
        fields = ['username', 'email', 'password', 'profile']
        extra_kwargs = {
            'password':{'write_only':True}
        }
    def validate_email(self, value):

        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', value):
            raise serializers.ValidationError('Enter a valid email address')
        return value

    def validate_name(self, value):

        if not re.match(r'^[a-zA-Z ]+$', value):
            raise serializers.ValidationError('Name can only contain letters and spaces')
        return value

    def validate_password(self, value):
        if not re.match(r'^[A-Za-z0-9@#$%^&+=]{8,}$', value):
            raise serializers.ValidationError('Password must be at least 8 characters long and contain letters, numbers, and special characters')
        return value




    def create(self, validated_data):
        prorile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        profile = Profile.objects.create(user=user,**prorile_data)
        return user
    