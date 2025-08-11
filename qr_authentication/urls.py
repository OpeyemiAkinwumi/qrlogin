from django.urls import path
from . import views

urlpatterns = [
    path('create', views.GenerateTemporaryId.as_view(), name="generate_temp_id")
]