# home/models.py

from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.api import APIField
from wagtail_headless_preview.models import HeadlessMixin

class HomePage(HeadlessMixin, Page):
    description = RichTextField(blank=True, help_text="Description of the website.")

    content_panels = Page.content_panels + [
        FieldPanel("description"),
    ]

    subpage_types = [
        "home.AboutPage",
        "home.SearchPage",
        "home.AccessibilityPage",
    ]

    api_fields = [
        APIField("description"),
    ]

class AboutPage(HeadlessMixin, Page):
    description = RichTextField(blank=True, help_text="About page description.")

    content_panels = Page.content_panels + [
        FieldPanel("description"),
    ]

    parent_page_types = ["home.HomePage"]
    subpage_types = []

    api_fields = [
        APIField("description"),
    ]


class SearchPage(HeadlessMixin, Page):
    description = RichTextField(blank=True, help_text="Search page description.")

    content_panels = Page.content_panels + [
        FieldPanel("description"),
    ]

    parent_page_types = ["home.HomePage"]
    subpage_types = []

    api_fields = [
        APIField("description"),
    ]


class AccessibilityPage(HeadlessMixin, Page):
    description = RichTextField(blank=True, help_text="Accessibility page description.")

    content_panels = Page.content_panels + [
        FieldPanel("description"),
    ]

    parent_page_types = ["home.HomePage"]
    subpage_types = []

    api_fields = [
        APIField("description"),
    ]
