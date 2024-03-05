from rest_framework import serializers
from .models import Group, Position, BotUser, AdminGroup


class AdminSerializers(serializers.ModelSerializer):
    class Meta:
        model = AdminGroup
        fields = '__all__'


class GroupSerializers(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class PositionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class BotUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = BotUser
        fields = '__all__'