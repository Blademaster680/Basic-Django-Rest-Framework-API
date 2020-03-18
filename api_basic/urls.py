from django.urls import path, include
from .views import article_list, article_detail, ArticleAPIView, ArticleDetailsView, GenericAPIView, ArticleViewSetView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('article', ArticleViewSetView, basename='article')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    path('api/', ArticleAPIView.as_view()),
    path('detail/<int:id>/', ArticleDetailsView.as_view()),
    path('generic/api/<int:id>/', GenericAPIView.as_view()),
]