from django.urls import path

from resturantdata import views


urlpatterns=[
     path('users/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
     path('',views.index),
     path('get-products', views.GetProducts.as_view()),
      path('get-product/<int:id>/', views.getProduct.as_view()),
]