from rest_framework.decorators import api_view, authentication_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import Product
from .serializers import ProductSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.

@api_view(['POST'])
def add_product(request: Request):
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed, login before"}, status=status.HTTP_401_UNAUTHORIZED)

    new_product = ProductSerializer(data=request.data)
    if new_product.is_valid():
        new_product.save()
        dataResponse = {
            "msg": "Created Successfully",
            "product": new_product.data
        }
        return Response(dataResponse)

    else:
        print(new_product.errors)
        dataResponse = {"msg": "couldn't create a product"}
        return Response(dataResponse, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_products(request: Request):
    products = Product.objects.all()

    dataResponse = {
        "msg": "List of the items",
        "products": ProductSerializer(instance=products, many=True).data
    }
    return Response(dataResponse)