from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework import exceptions

from .models import User


class RegistrationNormalUserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length = 128,
        min_length = 8,
        write_only = True
    )

    first_name = serializers.CharField(
        max_length = 30
    )

    last_name = serializers.CharField(
        max_length = 30
    )

    class Meta:
        model = User
        # List all of the fields that could possibly be included in a request
        # or response, including fields specified explicitly above.
        fields = ['pk','email','username','password','is_active','first_name','last_name','middle_name']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class RegistrationSuperUserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length = 128,
        min_length = 8,
        write_only = True
    )

    first_name = serializers.CharField(
        max_length = 30
    )

    last_name = serializers.CharField(
        max_length = 30
    )

    class Meta:
        model = User
        # List all of the fields that could possibly be included in a request
        # or response, including fields specified explicitly above.
        fields = ['email','username','password']

    def create(self, validated_data):
        return User.objects.create_superuser(**validated_data)


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = User
        fields = ('email','username','password')

    def update(self, instance, validated_data):

        password = validated_data.pop('password',None)

        for (key, value) in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)

        instance.save()

        return instance