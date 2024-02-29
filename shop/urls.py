"""
URL configuration for shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from product.views import hello_view,goodbye_view,current_date_view,main_view,products_view1,product__detail_view,category_view,products_view2,add_product_view,create_category_view,create_review_view
from user.views import register_view,login_view,profile_view,logout_view,confirmation_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/',hello_view),
    path('goodbye/',goodbye_view),
    path('current_date/',current_date_view),
    path('',main_view,name='home'),
    path('cate/',category_view),
    path('cate/products/<int:id>/',products_view1),
    path('cate/products/<int:id>/products/<int:prid>/',product__detail_view),
    path('products/products/<int:prid>/',product__detail_view),
    path('products/',products_view2),
    path('add/',add_product_view),
    path('create/',create_category_view),
    path('products/<int:prid>/create_review/',create_review_view),
    path('register/',register_view),
    path('login/',login_view),
    path('profile/',profile_view),
    path('logout/',logout_view),
    path('confirmation/',confirmation_view,name='confirm')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
