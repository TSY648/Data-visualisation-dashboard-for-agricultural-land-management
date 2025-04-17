"""
URL configuration for dashboard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app01 import views

urlpatterns = [
    #path("admin/", admin.site.urls),
    path("home/", views.home),
    path("cost_analysis_ARHAR/", views.cost_analysis_ARHAR),
    path("cost_analysis_COTTON/", views.cost_analysis_COTTON),
    path("cost_analysis_GRAM/", views.cost_analysis_GRAM),
    path("cost_analysis_GROUNDNUT/", views.cost_analysis_GROUNDNUT),
    path("cost_analysis_MAIZE/", views.cost_analysis_MAIZE),
    path("cost_analysis_MOONG/", views.cost_analysis_MOONG),
    path("cost_analysis_PADDY/", views.cost_analysis_PADDY),
    path("cost_analysis_RAPESEED/", views.cost_analysis_RAPESEED),
    path("cost_analysis_SUGARCANE/", views.cost_analysis_SUGARCANE),
    path("cost_analysis_WHEAT/", views.cost_analysis_WHEAT),
    path("cost_cultivation_crop_ARHAR/", views.cost_cultivation_crop_ARHAR),
    path("cost_cultivation_crop_COTTON/", views.cost_cultivation_crop_COTTON),
    path("cost_cultivation_crop_GRAM/", views.cost_cultivation_crop_GRAM),
    path("cost_cultivation_crop_GROUNDNUT/", views.cost_cultivation_crop_GROUNDNUT),
    path("cost_cultivation_crop_MAIZE/", views.cost_cultivation_crop_MAIZE),
    path("cost_cultivation_crop_MOONG/", views.cost_cultivation_crop_MOONG),
    path("cost_cultivation_crop_PADDY/", views.cost_cultivation_crop_PADDY),
    path("cost_cultivation_crop_RAPESEED/", views.cost_cultivation_crop_RAPESEED),
    path("cost_cultivation_crop_SUGARCANE/", views.cost_cultivation_crop_SUGARCANE),
    path("cost_cultivation_crop_WHEAT/", views.cost_cultivation_crop_WHEAT),
    path("cost_production_crop_ARHAR/", views.cost_production_crop_ARHAR),
    path("cost_production_crop_COTTON/", views.cost_production_crop_COTTON),
    path("cost_production_crop_GRAM/", views.cost_production_crop_GRAM),
    path("cost_production_crop_GROUNDNUT/", views.cost_production_crop_GROUNDNUT),
    path("cost_production_crop_MAIZE/", views.cost_production_crop_MAIZE),
    path("cost_production_crop_MOONG/", views.cost_production_crop_MOONG),
    path("cost_production_crop_PADDY/", views.cost_production_crop_PADDY),
    path("cost_production_crop_RAPESEED/", views.cost_production_crop_RAPESEED),
    path("cost_production_crop_SUGARCANE/", views.cost_production_crop_SUGARCANE),
    path("cost_production_crop_WHEAT/", views.cost_production_crop_WHEAT),
    path("yield_crop_ARHAR/", views.yield_crop_ARHAR),
    path("yield_crop_COTTON/", views.yield_crop_COTTON),
    path("yield_crop_GRAM/", views.yield_crop_GRAM),
    path("yield_crop_GROUNDNUT/", views.yield_crop_GROUNDNUT),
    path("yield_crop_MAIZE/", views.yield_crop_MAIZE),
    path("yield_crop_MOONG/", views.yield_crop_MOONG),
    path("yield_crop_PADDY/", views.yield_crop_PADDY),
    path("yield_crop_RAPESEED/", views.yield_crop_RAPESEED),
    path("yield_crop_SUGARCANE/", views.yield_crop_SUGARCANE),
    path("yield_crop_WHEAT/", views.yield_crop_WHEAT),
    path("cost_cultivation_state_Andhra_Pradesh/", views.cost_cultivation_state_Andhra_Pradesh),
    path("cost_cultivation_state_Bihar/", views.cost_cultivation_state_Bihar),
    path("cost_cultivation_state_Gujarat/", views.cost_cultivation_state_Gujarat),
    path("cost_cultivation_state_Haryana/", views.cost_cultivation_state_Haryana),
    path("cost_cultivation_state_Karnataka/", views.cost_cultivation_state_Karnataka),
    path("cost_cultivation_state_Madhya_Pradesh/", views.cost_cultivation_state_Madhya_Pradesh),
    path("cost_cultivation_state_Maharashtra/", views.cost_cultivation_state_Maharashtra),
    path("cost_cultivation_state_Orissa/", views.cost_cultivation_state_Orissa),
    path("cost_cultivation_state_Punjab/", views.cost_cultivation_state_Punjab),
    path("cost_cultivation_state_Rajasthan/", views.cost_cultivation_state_Rajasthan),
    path("cost_cultivation_state_Tamil_Nadu/", views.cost_cultivation_state_Tamil_Nadu),
    path("cost_cultivation_state_Uttar_Pradesh/", views.cost_cultivation_state_Uttar_Pradesh),
    path("cost_cultivation_state_West_Bengal/", views.cost_cultivation_state_West_Bengal),
    path("cost_production_state_Andhra_Pradesh/", views.cost_production_state_Andhra_Pradesh),
    path("cost_production_state_Bihar/", views.cost_production_state_Bihar),
    path("cost_production_state_Gujarat/", views.cost_production_state_Gujarat),
    path("cost_production_state_Haryana/", views.cost_production_state_Haryana),
    path("cost_production_state_Karnataka/", views.cost_production_state_Karnataka),
    path("cost_production_state_Madhya_Pradesh/", views.cost_production_state_Madhya_Pradesh),
    path("cost_production_state_Maharashtra/", views.cost_production_state_Maharashtra),
    path("cost_production_state_Orissa/", views.cost_production_state_Orissa),
    path("cost_production_state_Punjab/", views.cost_production_state_Punjab),
    path("cost_production_state_Rajasthan/", views.cost_production_state_Rajasthan),
    path("cost_production_state_Tamil_Nadu/", views.cost_production_state_Tamil_Nadu),
    path("cost_production_state_Uttar_Pradesh/", views.cost_production_state_Uttar_Pradesh),
    path("cost_production_state_West_Bengal/", views.cost_production_state_West_Bengal),
    path("yield_state_Andhra_Pradesh/", views.yield_state_Andhra_Pradesh),
    path("yield_state_Bihar/", views.yield_state_Bihar),
    path("yield_state_Gujarat/", views.yield_state_Gujarat),
    path("yield_state_Haryana/", views.yield_state_Haryana),
    path("yield_state_Karnataka/", views.yield_state_Karnataka),
    path("yield_state_Madhya_Pradesh/", views.yield_state_Madhya_Pradesh),
    path("yield_state_Maharashtra/", views.yield_state_Maharashtra),
    path("yield_state_Orissa/", views.yield_state_Orissa),
    path("yield_state_Punjab/", views.yield_state_Punjab),
    path("yield_state_Rajasthan/", views.yield_state_Rajasthan),
    path("yield_state_Tamil_Nadu/", views.yield_state_Tamil_Nadu),
    path("yield_state_Uttar_Pradesh/", views.yield_state_Uttar_Pradesh),
    path("yield_state_West_Bengal/", views.yield_state_West_Bengal),
    path("area_production/", views.area_production),
    path("area_yield/", views.area_yield),
    path("production_yield/", views.production_yield),
    path("bubble/", views.bubble),
]
