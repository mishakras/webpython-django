"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, re_path
from django.views.generic import TemplateView
from firstapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', views.products),  # маршрут по умолчанию
    path('products/<int:productid>/', views.products),
    path('students/', views.students),  # маршрут по умолчанию
    path('students/<int:studentid>/', views.students),
    path('users/<int:id_p>/<str:name>/', views.users),
    path('users/', views.users),  # маршрут по умолчанию
    path('', views.index, name="home"),
    path('template', views.template, name="home"),
    path('about/', TemplateView.as_view(template_name="firstapp/about.html")),
    path('contact/', TemplateView.as_view(template_name="firstapp/contact.html",
                                          extra_context={"work": "Разработка программных продуктов"})),
]
