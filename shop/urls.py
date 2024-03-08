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
from product.views import ProductListView, ProductDetailView, ProductCreateView, CategoryCreateView, CategoryListView, \
    ReviewCreateView
from user.views import register_view,login_view,profile_view,logout_view,confirmation_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('cate/',CategoryListView.as_view()),
    path('products/products/<int:prid>/',ProductDetailView.as_view()),
    path('products/',ProductListView.as_view()),
    path('add/',ProductCreateView.as_view()),
    path('create/', CategoryCreateView.as_view()),
    path('products/<int:prid>/create_review/',ReviewCreateView.as_view()),
    path('register/',register_view),
    path('login/',login_view),
    path('profile/',profile_view),
    path('logout/',logout_view),
    path('confirmation/',confirmation_view,name='confirm')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
