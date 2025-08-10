from django.urls import path
from . import views

urlpatterns = [
    path('user-contacts/', views.UserContactsView.as_view(), name='user_contacts')
]