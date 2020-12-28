from django.urls import path
from .import views
urlpatterns = [
    #path('', views.login),
    #path('profile/<str:pk>/',views.profile),
    path('', views.index, name='index'),
    path('<str:userName>/', views.room, name='room'),

    #path('<str:username>/', views.room, name='room'),
    #path('',views.private),
    #path('<str:username>/<str:otheruser>/',views.private_chat)

]
