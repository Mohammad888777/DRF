from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers

from . import views



router=routers.SimpleRouter()
router.register("user_with_modelViewSet",views.UserWithModelViewSet,basename="arts")
router.register("article_with_modelViewSet",views.AticlesWithModeViewSet,basename="users")





urlpatterns=[

    path("",views.ArticleList.as_view(),name="article_list_api"),
    path("user_list_api/",views.UserList.as_view(),name="user_list_api"),
    path("article_detail_api/<str:slug>/",views.ArticleDetail.as_view(),name="article_detail_api"),
    path("user_detail_api/<str:pk>/",views.UsereDetail.as_view(),name="user_detail_api"),
    path('api_token_auth/', obtain_auth_token,name="login"),
    path('revoke_token/', views.RevokeToken.as_view(),name="revoke_token"),
    path('dj_rest_auth/', include('dj_rest_auth.urls')),
    path('dj_rest_auth/registration/', include('dj_rest_auth.registration.urls')),
    path("",include(router.urls)),
    path("with_hyper_link/<str:pk>/",views.UserViewForHyperLink.as_view(),name="with_hyper_link"),

     
]

