from rest_framework import serializers
from blog.models import Article
from django.contrib.auth import get_user_model




class UserSerializer(serializers.ModelSerializer):

    article_set=serializers.StringRelatedField(many=True,read_only=True)
    # password=serializers.CharField(write_only=True)
    # password2=serializers.CharField(write_only=True)

    class Meta:

        model=get_user_model()
        # fields=["first_name","last_name","is_staff","is_superuser","article_set","username","email",'password','password2']
        fields="__all__"




class AuthorSerializer(serializers.ModelSerializer):

    class Meta:

        model=get_user_model()
        fields=["username","first_name","last_name","email"]











class ArticleSerializer(serializers.ModelSerializer):

    # au=AuthorSerializer(source="author")

    def get_author_first_name_with_method(self,obj):
        return obj.author.username

    auth_first_name=serializers.SerializerMethodField(method_name="get_author_first_name_with_method")

    auth=serializers.HyperlinkedIdentityField(source="author",view_name="with_hyper_link")
    auth_username=serializers.CharField(source="author.username")


    class Meta:

        model=Article

        exclude=["created","updated"]

    
    def validate(self, attrs):

        fils=["js","python","ruby","c++","c","solidity","go"]
        if not attrs["title"] in fils:
            raise serializers.ValidationError("not allowed to send other title")
        return attrs



