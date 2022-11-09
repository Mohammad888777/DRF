from django.shortcuts import render,redirect,get_object_or_404
from .serializers import ArticleSerializer,UserSerializer
from blog.models import Article
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveUpdateDestroyAPIView
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser,IsAuthenticated,IsAuthenticatedOrReadOnly
from .permissions import IsSuperUser,IsStaffOrReadOnly,IsAuthorOrReadOnly,IsSuperUserOrStaffReadOnly
from rest_framework.views import APIView
from rest_framework import status













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

    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[IsSuperUserOrStaffReadOnly]




class UsereDetail(RetrieveUpdateDestroyAPIView):

    serializer_class=UserSerializer
    queryset=User.objects.all()
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

    