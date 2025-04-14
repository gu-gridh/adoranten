# journal/models.py

from django.db import models
from django.core.exceptions import ValidationError
from wagtail.api import APIField
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page
from wagtail_headless_preview.models import HeadlessMixin
from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase


class Publications(HeadlessMixin, Page):
    parent_page_types = ["home.HomePage"]
    subpage_types = ["journal.IssuePage"]


class IssuePage(HeadlessMixin, Page):
    issue_year = models.IntegerField()

    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='+'
    )

    pdf_file = models.FileField(
        upload_to='journal/issues/',
        null=False,
        blank=True,
        default="",
        help_text="Upload the PDF for the entire issue."
    )

    content_panels = Page.content_panels + [
        FieldPanel("issue_year"),
        FieldPanel("image"),
        FieldPanel("pdf_file"),
    ]

    # IssuePage under Publications
    parent_page_types = ["journal.Publications"]

    # This page may have ArticlePages as children
    subpage_types = ['ArticlePage']

    api_fields = [
        APIField("issue_year"),
        APIField("image"),
        APIField("pdf_file"),
    ]

    def clean(self):
        """Ensure image is not empty."""
        if not self.image:
            raise ValidationError({'image': "An image is required."})


class ArticlePageTag(TaggedItemBase):
    content_object = ParentalKey('journal.ArticlePage', on_delete=models.CASCADE, related_name='tagged_items')


class ArticlePage(HeadlessMixin, Page):
    tags = ClusterTaggableManager(through=ArticlePageTag, blank=True)

    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+'
    )
    article_description = RichTextField(blank=True, features=['h3', 'bold', 'italic', 'link'])
    author = models.CharField(blank=True)
    page_range = models.CharField(blank=True)
    citation = RichTextField(blank=True, features=['bold', 'italic', 'link'])

    pdf_file = models.FileField(
        upload_to='journal/articles/',
        null=False,
        blank=False,
        default="",
        help_text="Upload the PDF for this specific article."
    )

    content_panels = Page.content_panels + [
        FieldPanel("image"),
        FieldPanel("article_description"),
        FieldPanel("author"),
        FieldPanel("page_range"),
        FieldPanel("pdf_file"),
        FieldPanel("citation"),
        FieldPanel('tags'),
    ]

    parent_page_types = ['IssuePage']  # Must live under an IssuePage
    subpage_types = []                 # No children

    api_fields = [
        APIField("image"),
        APIField("article_description"),
        APIField("pdf_file"),
        APIField("author"),
        APIField("page_range"),
        APIField("citation"),
        APIField("tags"),
    ]

    def clean(self):
        """Ensure pdf_file are not empty."""
        if not self.pdf_file:
            raise ValidationError({'pdf_file': "A PDF file is required."})
