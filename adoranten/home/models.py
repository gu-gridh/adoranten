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

    subpage_types = ['journal.IssuePage']

    api_fields = [
        APIField("description"),
    ]
