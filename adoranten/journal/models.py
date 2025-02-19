from django.db import models
from wagtail.api import APIField
from wagtail.admin.panels import (
    FieldPanel,
)
from wagtail.fields import RichTextField
from wagtail.models import (
    Page
)

# Create your models here.
class StandardPage(Page):
    """
    Standard default page
    """

    intro = models.CharField(help_text="Short intro text", blank=True, max_length=250)
    body = RichTextField(help_text="Text to describe the page", blank=True)
    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        FieldPanel("body"),
    ]

    api_fields = [
        APIField("intro"),
        APIField("body"),
    ]
