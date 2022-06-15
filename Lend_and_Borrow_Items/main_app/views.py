import json
from operator import contains
from turtle import title
from django.http import HttpResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import Product, Review, Profile
from .serializers import ProductSerializer, ReviewSerializer, ProfileSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

'''
API Product model
'''
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def add_product(request: Request):
    '''
    this API used by user to add product
    '''

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
    '''
    this API used from anyone to list all products
    '''
    products = Product.objects.all()

    dataResponse = {
        "msg": "List of the products",
        "products": ProductSerializer(instance=products, many=True).data
    }
    return Response(dataResponse)

@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_product(request: Request, product_id):
    '''
    this API used by user to delete specific product (only added by this user)
    '''

    user:User = request.user
    product = Product.objects.get(id=product_id) 

    if not request.user.is_authenticated or not request.user.has_perm('main_app.delete_product'):
        return Response({"msg": "Not Allowed, login before"}, status=status.HTTP_401_UNAUTHORIZED)

    elif user != product.user:
        return Response({"msg": "You can delete products that added by your only"}, status=status.HTTP_401_UNAUTHORIZED)

    product = Product.objects.get(id=product_id)
    product.delete()
    return Response({"msg": "Deleted Successfully"})


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
def update_product(request: Request, product_id):
    '''
    this api used by user to update specific product (only added by this user)
    '''
    user:User = request.user
    product = Product.objects.get(id=product_id) 

    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed, login before"}, status=status.HTTP_401_UNAUTHORIZED)

    elif user != product.user:
        return Response({"msg": "You can update products that added by your only"}, status=status.HTTP_401_UNAUTHORIZED)

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


@api_view(['GET'])
def search_product(request: Request, product_title):
    '''
    this API used from anyone to list all products
    '''
    product = Product.objects.filter(title = product_title)
    dataResponse = {
        "msg": "list products:",
        "product": ProductSerializer(instance=product, many=True).data
    }
    return Response(dataResponse)






'''
API Review model
'''
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def add_review(request: Request):
    '''
    this API used by user to add review
    '''

    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed, login before"}, status=status.HTTP_401_UNAUTHORIZED)

    new_review = ReviewSerializer(data=request.data)
    if new_review.is_valid():
        new_review.save()
        dataResponse = {
            "msg": "Created Successfully",
            "review": new_review.data
        }
        return Response(dataResponse)

    else:
        print(new_review.errors)
        dataResponse = {"msg": "couldn't create a review"}
        return Response(dataResponse, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_reviews(request: Request):
    '''
    this API used from anyone to list all reviews
    '''
    reviews = Review.objects.all()

    dataResponse = {
        "msg": "List of the reviews",
        "reviews": ReviewSerializer(instance=reviews, many=True).data
    }
    return Response(dataResponse)

@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_review(request: Request, review_id):
    '''
    this API used by user to delete specific review (only added by this user)
    '''

    user:User = request.user
    review = Review.objects.get(id=review_id) 

    if not request.user.is_authenticated or not request.user.has_perm('main_app.delete_review'):
        return Response({"msg": "Not Allowed, login before"}, status=status.HTTP_401_UNAUTHORIZED)

    elif user != review.user:
        return Response({"msg": "You can delete reviews that added by your only"}, status=status.HTTP_401_UNAUTHORIZED)

    review = Review.objects.get(id=review_id)
    review.delete()
    return Response({"msg": "Deleted Successfully"})


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
def update_review(request: Request, review_id):
    '''
    this api used by user to update specific review (only added by this user)
    '''
    user:User = request.user
    review = Review.objects.get(id=review_id) 

    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed, login before"}, status=status.HTTP_401_UNAUTHORIZED)

    elif user != review.user:
        return Response({"msg": "You can update reviews that added by your only"}, status=status.HTTP_401_UNAUTHORIZED)

    updated_review = ReviewSerializer(instance=review, data=request.data)
    if updated_review.is_valid():
        updated_review.save()
        responseData = {
            "msg": "updated successfully"
        }

        return Response(responseData)
    else:
        print(updated_review.errors)
        return Response({"msg": "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)





'''
API Profile model
'''
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def add_profile(request: Request):
    '''
    this API used by user to add profile
    '''

    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed, login before"}, status=status.HTTP_401_UNAUTHORIZED)

    new_profile = ProfileSerializer(data=request.data)
    if new_profile.is_valid():
        new_profile.save()
        dataResponse = {
            "msg": "Created Successfully",
            "profile": new_profile.data
        }
        return Response(dataResponse)

    else:
        print(new_profile.errors)
        dataResponse = {"msg": "couldn't create a profile"}
        return Response(dataResponse, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_profiles(request: Request):
    '''
    this API used from anyone to list all profiles
    '''
    profiles = Profile.objects.all()

    dataResponse = {
        "msg": "List of the profiles",
        "profiles": ProfileSerializer(instance=profiles, many=True).data
    }
    return Response(dataResponse)


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
def update_profile(request: Request, profile_id):
    '''
    this api used by user to update user profile
    '''
    user:User = request.user
    profile = Profile.objects.get(id=profile_id) 

    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed, login before"}, status=status.HTTP_401_UNAUTHORIZED)

    elif user != profile.user:
        return Response({"msg": "You can update profiles that added by your only"}, status=status.HTTP_401_UNAUTHORIZED)

    updated_profile = ProfileSerializer(instance=profile, data=request.data)
    if updated_profile.is_valid():
        updated_profile.save()
        responseData = {
            "msg": "updated successfully"
        }

        return Response(responseData)
    else:
        print(updated_profile.errors)
        return Response({"msg": "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)

