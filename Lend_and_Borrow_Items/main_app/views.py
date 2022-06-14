import json
from django.http import HttpResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import Product
from .serializers import ProductSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
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
        "msg": "List of the products",
        "products": ProductSerializer(instance=products, many=True).data
    }
    return Response(dataResponse)

@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
#@permission_classes([IsAuthenticated])
def delete_product(request: Request, product_id):

    user:User = request.user
    product = Product.objects.get(id=product_id) 

    if not request.user.is_authenticated :#or not request.user.has_perm('main.app.delete_product'):
        return Response({"msg": "Not Allowed, login before"}, status=status.HTTP_401_UNAUTHORIZED)

    elif user != product.user:
        return Response({"msg": "You can delete products that added by your only"}, status=status.HTTP_401_UNAUTHORIZED)

    product = Product.objects.get(id=product_id)
    product.delete()
    return Response({"msg": "Deleted Successfully"})


@api_view(['PUT'])
def update_product(request: Request, product_id):
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed, login before"}, status=status.HTTP_401_UNAUTHORIZED)
    product = Product.objects.get(id=product_id)

    updated_product = ProductSerializer(instance=product, data=request.data)
    if updated_product.is_valid():
        updated_product.save()
        responseData = {
            "msg": "updated successfully"
        }

        return Response(responseData)
    else:
        print(updated_product.errors)
        return Response({"msg": "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)