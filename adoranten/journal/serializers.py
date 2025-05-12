from wagtail.api.v2.serializers import PageSerializer
from wagtail.images.api.fields import ImageRenditionField
from .models import ArticlePage


class ArticlePageSerializer(PageSerializer):
    meta_fields = '__all__'
    # TODO: Choose thumbnail size instead?
    image = ImageRenditionField('original')

    class Meta:
        model = ArticlePage
        fields = ['id', 'title', 'pdf_file', 'image',
                  'author', 'page_range', 'citation', 'tags', 'issue_id']
