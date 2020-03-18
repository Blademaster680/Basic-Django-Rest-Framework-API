from django.urls import path, include
from .views import article_list, article_detail, ArticleAPIView, ArticleDetailsView

urlpatterns = [
    #path('api/', article_list),
    path('api/', ArticleAPIView.as_view()),
    path('detail/<int:id>/', ArticleDetailsView.as_view()),
]