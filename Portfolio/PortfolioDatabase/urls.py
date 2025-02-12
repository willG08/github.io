from django.urls import path
from . import views

app_name = 'PortfolioDatabase'
urlpatterns = [
    path('', views.home, name='Home'),
    path('hobbies/', views.hobbies, name='Hobbies'),
    path('portfolio/', views.portfolio, name='Portfolio'),
    path('contact/', views.contact, name='Contact'),
    path('<int:hobby_id>/', views.details, name='Details'),
    path('portfolio/<int:portfolio_id>/', views.portfolioDetails, name='PortfolioDetails'),
]