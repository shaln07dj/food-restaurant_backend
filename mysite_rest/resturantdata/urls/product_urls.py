from django.urls import path

from resturantdata.views import product_views as views


urlpatterns=[
    

     path('', views.GetProducts.as_view()),
   
     path('<str:pk>/', views.getProduct.as_view()),
]