from django.contrib import admin
from .models import AdminGroup, Group, BotUser, Position
# Register your models here.
admin.site.register(AdminGroup)
admin.site.register(Group)
admin.site.register(Position)
admin.site.register(BotUser)
