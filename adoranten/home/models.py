# home/models.py
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.api import APIField
from wagtail import blocks
from wagtail_headless_preview.models import HeadlessMixin


class APIPageChooserBlock(blocks.PageChooserBlock):
    def get_api_representation(self, value, context=None):
        if value:
            return {
                "id": value.id,
                "title": value.title
            }


class HomePage(HeadlessMixin, Page):
    description = RichTextField(blank=True, help_text="Description of the website.")
    latest_issues = StreamField([
        ("heading", blocks.CharBlock(form_classname="title")),
        ("issue_list", blocks.ListBlock(
            (APIPageChooserBlock(page_type="journal.IssuePage")))),
    ], blank=True,
       block_counts={
       "heading": {"max_num": 1},
       "issue_list": {"max_num": 3},
    })
    article_highlights = StreamField([
        ("heading", blocks.CharBlock(form_classname="title")),
        ("article_list", blocks.ListBlock(
            (APIPageChooserBlock(page_type="journal.ArticlePage")))),
    ], blank=True,
       block_counts={
       "heading": {"max_num": 1},
       "article_list": {"max_num": 3},
    })

    content_panels = Page.content_panels + [
        FieldPanel("description"),
        FieldPanel("latest_issues"),
        FieldPanel("article_highlights"),
    ]

    subpage_types = [
        "home.AboutPage",
        "home.SearchPage",
        "home.AccessibilityPage",
        "journal.Publications",
    ]

    api_fields = [
        APIField("description"),
        APIField("latest_issues"),
        APIField("article_highlights"),
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
