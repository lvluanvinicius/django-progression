from django.urls import path 
from .views import CreateView

urlpatterns = [
    path('/register', CreateView.as_view(), name="register-activity"),
]
