from rest_framework import serializers
from blog.models import Article
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    article_set=serializers.StringRelatedField(many=True,read_only=True)
    # password=serializers.CharField(write_only=True)
    # password2=serializers.CharField(write_only=True)

    class Meta:

        model=User
        # fields=["first_name","last_name","is_staff","is_superuser","article_set","username","email",'password','password2']
        fields="__all__"



class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model=Article

        # fields=["title","author","slug","id","content","publish","statuss"]
        exclude=["created","updated"]
        # fields="__all__"



