# home/models.py
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
)
from wagtail.api import APIField
from wagtail import blocks, images
from wagtail_headless_preview.models import HeadlessMixin
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.contrib.forms.panels import FormSubmissionsPanel
from rest_framework import serializers


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = images.get_image_model()
        fields = ['title', 'file', 'width', 'height']


class APIPageChooserBlock(blocks.PageChooserBlock):
    def get_api_representation(self, value, context=None):
        if value:
            return {
                "id": value.id,
                "title": value.title,
                "image": ImageSerializer(context=context).to_representation(value.image),
            }


class HomePage(HeadlessMixin, Page):
    description = RichTextField(blank=True, help_text="Description of the website.", features=['h2', 'h3', 'bold', 'italic', 'link'])
    latest_issue = StreamField([
        ("heading", blocks.CharBlock(form_classname="title")),
        ("issue", APIPageChooserBlock(page_type="journal.IssuePage")),
    ], blank=True,
       block_counts={
       "heading": {"max_num": 1},
       "issue": {"max_num": 1},
    })
    article_highlights = StreamField([
        ("heading", blocks.CharBlock(form_classname="title")),
        ("article_list", blocks.ListBlock(
            (APIPageChooserBlock(page_type="journal.ArticlePage")), min_num=3, max_num=3)),
    ], blank=True,
       block_counts={
       "heading": {"max_num": 1},
       "article_list": {"max_num": 1},
    })

    content_panels = Page.content_panels + [
        FieldPanel("description"),
        FieldPanel("latest_issue"),
        FieldPanel("article_highlights"),
    ]

    subpage_types = [
        "home.AboutPage",
        "home.SearchPage",
        "home.AccessibilityPage",
        "home.FormPage",
        "journal.Publications",
    ]

    api_fields = [
        APIField("description"),
        APIField("latest_issue"),
        APIField("article_highlights"),
    ]


class AboutPage(HeadlessMixin, Page):
    description = RichTextField(blank=True, help_text="About page description.", features=['h2', 'h3', 'bold', 'italic', 'link'])

    content_panels = Page.content_panels + [
        FieldPanel("description"),
    ]

    parent_page_types = ["home.HomePage"]
    subpage_types = []

    api_fields = [
        APIField("description"),
    ]


class SearchPage(HeadlessMixin, Page):
    description = RichTextField(blank=True, help_text="Search page description.", features=['h2', 'h3', 'bold', 'italic', 'link'])

    content_panels = Page.content_panels + [
        FieldPanel("description"),
    ]

    parent_page_types = ["home.HomePage"]
    subpage_types = []

    api_fields = [
        APIField("description"),
    ]


class AccessibilityPage(HeadlessMixin, Page):
    description = RichTextField(blank=True, help_text="Accessibility page description.", features=['h2', 'h3', 'bold', 'italic', 'link'])

    content_panels = Page.content_panels + [
        FieldPanel("description"),
    ]

    parent_page_types = ["home.HomePage"]
    subpage_types = []

    api_fields = [
        APIField("description"),
    ]


class FormField(AbstractFormField):
    page = ParentalKey('FormPage', on_delete=models.CASCADE, related_name='form_fields')


class FormPage(AbstractEmailForm):
    intro = RichTextField(blank=True, features=['h2', 'h3', 'bold', 'italic', 'link'])
    thank_you_text = RichTextField(blank=True, features=['h2', 'h3', 'bold', 'italic', 'link'])

    content_panels = AbstractEmailForm.content_panels + [
        FormSubmissionsPanel(),
        FieldPanel('intro'),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address'),
                FieldPanel('to_address'),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]

    api_fields = [
        APIField("intro"),
        APIField("thank_you_text"),
        APIField("from_address"),
        APIField("to_address"),
        APIField("subject"),
        APIField("form_fields"),
    ]
