from django.urls import path

from . import views

urlpatterns = [
    # path(r'^$', views.Home.as_view(), name='home'),
    # path('home', views.Home.as_view(), name='home'),
    path('', views.Home.as_view(), name='home'),
    path('hanoi', views.hanoi, name='hanoi'),
    path('cantho', views.cantho, name='cantho'),
    path('engagement', views.engagement, name='engagement'),
    path('wedding', views.wedding, name='wedding-party'),
    path('save-the-dates', views.save_the_date, name='save-the-dates-photos')
]
