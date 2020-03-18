from django.urls import path, include
from .views import article_list, article_detail, ArticleAPIView, ArticleDetailsView, GenericAPIView

urlpatterns = [
    #path('api/', article_list),
    path('api/', ArticleAPIView.as_view()),
    path('detail/<int:id>/', ArticleDetailsView.as_view()),
    path('generic/api/<int:id>/', GenericAPIView.as_view()),
]