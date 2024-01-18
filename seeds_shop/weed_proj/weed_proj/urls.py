"""
URL configuration for weed_proj project.

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
from django.contrib.auth.views import LoginView
from django.urls import path

from weed_site.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin),
    path('', home),
    path('catalog/', catalog, name='catalog'),
    path('catalog/page_<int:page>', catalog, name='catalog'),
    path('catalog/<str:word>', catalog, name='catalog'),
    path('sales_delivery/', sales_delivery),
    path('legal/', legal),
    path('reviews/', reviews),
    path('basket/', basket),
    path('confirm_order/<int:order_id>', confirm_order),
    path('login/', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', reg_view, name='reg'),
    path('profile/', profile, name='profile'),
    path('add_basket/<int:prod_id>', add_basket),
    path('del_basket/<int:prod_id>', del_basket),
    path('add_product/', add_product),
    path('product/<int:prod_id>', product),
    path('update_product/<int:prod_id>', update_product),
    path('delete_product/<int:prod_id>', delete_product),
    path('admins_list/', admins_list),
    path('del_admin/<int:adm_id>', delete_admin),
    path('all_orders/', all_orders),
    path('change_order/<int:order_id>', change_order),
    path('del_review/<int:rev_id>', del_review),
    path('create_article/', create_article),
    path('all_articles/', all_articles),
    path('all_articles/page_<int:page>', all_articles),
    path('article/<int:art_id>', article),
    path('del_article/<int:art_id>', del_article),
    path('change_article/<int:art_id>', change_article),
]
