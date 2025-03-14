from django.urls import path
from . import views

urlpatterns = [
    path('home', views.HomeView.as_view(), name='home'),
    path('day/new/', views.DayCreateView.as_view(), name='day_new'),
    path('day/<int:pk>/', views.DayDetailView.as_view(), name='day_detail'),
    path('', views.SearchPageView.as_view(), name="actual-search"), #TODO: Fix the nonsensical urls
    path('search/', views.SearchView.as_view(), name='search'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('add_meal/<int>', views.MealCreateView.as_view(), name='add_meal_id'),
    path('add_meal/', views.MealCreateView.as_view(), name='add_meal'),
    path('profile/<int:pk>', views.ProfileDetailView.as_view(), name="profile")
]
