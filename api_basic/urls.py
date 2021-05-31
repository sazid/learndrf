from django.urls import path
from .views import article_list, article_detail # normal function based views
from .views import ArticleAPIView, ArticleDetails # APIView
from .views import GenericAPIView # generic views

urlpatterns = [
    # path('article/', article_list),
    # path('detail/<int:pk>/', article_detail),

    path('article/', ArticleAPIView.as_view()),
    path('detail/<int:pk>/', ArticleDetails.as_view()),

    # notice that we're routing to the same view, but one which have no pk
    # another which have pk
    path('generic/article/', GenericAPIView.as_view()),
    path('generic/article/<int:pk>/', GenericAPIView.as_view()),
]
