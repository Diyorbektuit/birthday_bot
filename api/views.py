from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Group, Position, BotUser, AdminGroup
from .serializers import GroupSerializers, PositionSerializers, BotUserSerializers, AdminSerializers
# Create your views here.


class CreateAdminView(ListCreateAPIView):
    queryset = AdminGroup.objects.all()
    serializer_class = AdminSerializers


class CreateGroupView(ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializers


class CreatePositionView(ListCreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializers


class CreateBotUserView(ListCreateAPIView):
    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializers



