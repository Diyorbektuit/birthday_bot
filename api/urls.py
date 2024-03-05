from django.urls import path
from .views import CreateGroupView, CreatePositionView, CreateBotUserView,CreateAdminView
urlpatterns = [
    path('create_admin/', CreateAdminView.as_view(), name='admin'),
    path('group/', CreateGroupView.as_view(), name='group'),
    path('position/', CreatePositionView.as_view(), name='position'),
    path('botuser/', CreateBotUserView.as_view(), name='botuser')
]