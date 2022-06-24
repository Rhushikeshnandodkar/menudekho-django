from unicodedata import name
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name="index"),
    path('nonveg', views.nonveg, name="nonveg"),
    path('update/<int:pk>', views.update, name="update"),
    path('handlelogin', views.handlelogin, name="handlelogin"),
    path('profile', views.profile, name="profile"),
    path('detail/<int:pk>', views.detail, name="detail"),
    path('search', views.search, name="search"),
    
]