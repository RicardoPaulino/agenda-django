from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [   
    path('info/<str:contact_id>/', views.contact_info, name='info'),  
    path('create/',views.contact_create, name='create'),
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),  
]