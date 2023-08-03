from rest_framework import serializers
from .models import Menu, Booking
from django.contrib.auth.models import User, Group


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"


# class GroupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model: Group
#         fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    # groups = GroupSerializer()

    class Meta:
        model = User
        fields = [
            "url",
            "username",
            "email",
            "groups",
        ]  # fields to be exposed via the API
