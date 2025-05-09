from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from taggit.models import Tag


class TagsSnippetViewSet(SnippetViewSet):
    panels = [FieldPanel("name")]
    model = Tag
    icon = "tag"
    add_to_admin_menu = True
    menu_label = "Keywords"
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    list_display = ["name", "slug"]
    search_fields = ("name",)


register_snippet(TagsSnippetViewSet)
