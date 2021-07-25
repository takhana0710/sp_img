from django.urls import path
from . import views

urlpatterns=[
    path('run/',views.SpiderPtt.as_view()),
    path('px/',views.SpiderPivix.as_view()),
]