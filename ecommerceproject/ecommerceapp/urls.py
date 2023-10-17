from django.urls import path
from . import views
app_name='ecommerceapp'

urlpatterns = [
    path('',views.allProductCat, name='allProductCat'),
    path('slug/',views.allProductCat, name='allProductCat'),
    path('slug/<slug:c_slug>/', views.allProductCat, name='product_by_category'),
    path('slug/<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='prodCatdetail')
]
