from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('fetch-data/', views.fetch_data, name='fetch_data'),
    path('display-data/', views.display_data, name='display_data'),
    path('visualization/', views.visualization, name='visualization'),
]
