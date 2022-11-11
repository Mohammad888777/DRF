from urllib import request
from django.shortcuts import render,redirect,get_object_or_404
from .serializers import ArticleSerializer, AuthorSerializer,UserSerializer
from blog.models import Article
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveUpdateDestroyAPIView
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAdminUser,IsAuthenticated,IsAuthenticatedOrReadOnly
from .permissions import IsSuperUser,IsStaffOrReadOnly,IsAuthorOrReadOnly,IsSuperUserOrStaffReadOnly
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveAPIView





class UserViewForHyperLink(RetrieveAPIView):

    serializer_class=AuthorSerializer
    def get_queryset(self):
        return get_user_model().objects.all()    












class AticlesWithModeViewSet(ModelViewSet):

    queryset=Article.objects.all()
    serializer_class=ArticleSerializer
    filterset_fields=["slug","author__username","status"]
    search_fields=["title","content"]
    # ordering_fields=["-id"]
    ordering=["-id"]



    # def get_queryset(self):

    #     query=Article.objects.all()
    #     slug=self.request.query_params.get("slug")
    #     if slug is not None:
    #         query=Article.objects.filter(
    #             slug__icontains=slug
    #         )
    #     return query
    
        
    

    def get_permissions(self):

        if self.action in ["list","create"]:

            permission_classes=[IsStaffOrReadOnly]
        else:
            permission_classes=[IsAuthorOrReadOnly,IsStaffOrReadOnly]

        return [permission() for permission in permission_classes ]

        
        




class UserWithModelViewSet(ModelViewSet):

    queryset=get_user_model().objects.all()
    serializer_class=UserSerializer
    permission_classes=[IsSuperUserOrStaffReadOnly]




    














class ArticleList(ListCreateAPIView):

    # queryset=Article.objects.all()
    serializer_class=ArticleSerializer
    permission_classes=[IsStaffOrReadOnly,IsAuthorOrReadOnly]

    def get_queryset(self):
        print(self.request.auth)
        print(self.request.user)

        return Article.objects.all()





class ArticleDetail(RetrieveUpdateDestroyAPIView):

    serializer_class=ArticleSerializer
    queryset=Article.objects.all()
    lookup_field='slug'
    permission_classes=[IsStaffOrReadOnly,IsAuthorOrReadOnly]






class UserList(ListCreateAPIView):

    queryset=get_user_model().objects.all()
    serializer_class=UserSerializer
    permission_classes=[IsSuperUserOrStaffReadOnly]




class UsereDetail(RetrieveUpdateDestroyAPIView):

    serializer_class=UserSerializer
    queryset=get_user_model().objects.all()
    permission_classes=[IsSuperUserOrStaffReadOnly]





class RevokeToken(APIView):

    permission_classes=[IsAuthenticated]
    
    # def get(self,request):
        
    #     return Response({"message":"okay"})

    # def post(self,request):
    #     pass
    
    # def put(self,request):
    #     pass

    def delete(self,request):

        self.request.auth.delete()


        return Response(status=status.HTTP_404_NOT_FOUND)

    