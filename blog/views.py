from django.views.generic import ListView,DetailView
from .models import Article
from django.shortcuts import render,redirect,get_object_or_404




class ArticleList(ListView):

    template_name: str="blog/article_list.html"
    
    def get_queryset(self) :

        return Article.objects.all().filter(status=True)


class ArticleDetail(DetailView):

    template_name: str="blog/article_detail.html"

    def get_object(self):

        pk=self.kwargs.get("pk")
        art=get_object_or_404(Article,pk=pk)
        return art
    



