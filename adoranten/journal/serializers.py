from wagtail.api.v2.serializers import PageSerializer
from .models import ArticlePage


class ArticlePageSerializer(PageSerializer):
    meta_fields = '__all__'

    class Meta:
        model = ArticlePage
        fields = ['id', 'title', 'pdf_file',
                  'author', 'page_range', 'citation', 'tags']
