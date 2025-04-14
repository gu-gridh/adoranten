from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ArticlePage
from .serializers import ArticlePageSerializer


class ArticleListView(APIView):
    def get(self, request):
        tag = request.GET.get('tag')
        articles = ArticlePage.objects.live().public()

        if tag:
            articles = articles.filter(tags__name=tag)

        serializer = ArticlePageSerializer(articles, many=True)
        return Response(serializer.data)
