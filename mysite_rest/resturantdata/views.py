
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView


from resturantdata import models
from resturantdata.serializers import ProductSerializers
from rest_framework.response import Response

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
   
    def validate(self, attrs):

        data= super().validate(attrs)
        data["username"]=self.user.username
        data["email"]=self.user.email


        return data
      
        
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the Rest index.")
    
class GetProducts(APIView):
    def get(self,request):
        products=models.Products.objects.all()
        response=ProductSerializers(products,many=True)
        return Response(response.data)

    def post(self,request):
        product_requset=request.data
        product_data=ProductSerializers(data=product_requset)
        if product_data.is_valid():
            product_data.save()
            return Response({
                'msg':"recived"
            })
        else:
            return Response({'error':'product_data.errors'})
class getProduct(APIView):
    def get(self,requset,id):
        product=models.Products.objects.get(id=id)
        response=ProductSerializers(product,many=False)
        return Response(response.data)
        




