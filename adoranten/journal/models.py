# journal/models.py

from django.db import models
from wagtail.api import APIField
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page
from wagtail_headless_preview.models import HeadlessMixin

class IssuePage(HeadlessMixin, Page):
    issue_name = models.CharField(max_length=255)
    issue_year = models.IntegerField()
    cover_image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+'
    )
    pdf_file = models.FileField(
        upload_to='journal/issues/',
        null=True,
        blank=True,
        help_text="Upload the PDF for the entire issue."
    )

    content_panels = Page.content_panels + [
        FieldPanel("issue_name"),
        FieldPanel("issue_year"),
        FieldPanel("cover_image"),
        FieldPanel("pdf_file"),
    ]

    # This page may have ArticlePages as children
    subpage_types = ['ArticlePage']

    api_fields = [
        APIField("issue_name"),
        APIField("issue_year"),
        APIField("cover_image"),
        APIField("pdf_file"),
    ]

class ArticlePage(HeadlessMixin, Page):
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+'
    )
    article_title = models.CharField(max_length=255)
    article_description = RichTextField(blank=True)
    pdf_file = models.FileField(
        upload_to='journal/articles/',
        null=True,
        blank=True,
        help_text="Upload the PDF for this specific article."
    )

    content_panels = Page.content_panels + [
        FieldPanel("image"),
        FieldPanel("article_title"),
        FieldPanel("article_description"),
        FieldPanel("pdf_file"),
    ]

    parent_page_types = ['IssuePage']  # Must live under an IssuePage
    subpage_types = []                 # No children

    api_fields = [
        APIField("image"),
        APIField("article_title"),
        APIField("article_description"),
        APIField("pdf_file"),
    ]
