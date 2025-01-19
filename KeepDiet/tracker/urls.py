from django.urls import path
from . import views

urlpatterns = [
    path('day/<int:pk>/', views.DayDetailView.as_view(), name='day-detail'),
    path('', views.apicalltest, name='apicalltest')
]
