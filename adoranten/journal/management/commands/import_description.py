from django.core.management.base import BaseCommand
from journal.models import ArticlePage
# python manage.py import_description --settings=adoranten.settings.production


class Command(BaseCommand):
    help = 'Update the description fields of multiple Wagtail pages'

    def handle(self, *args, **kwargs):
        updates = []
        # updates = [
        #    {'id': 80, 'description': """<p>In this article, ...</p>"""},
        #    {'id': 81, 'description': """<p>This article by ...</p>"""},
        # ]

        for update in updates:
            try:
                page = ArticlePage.objects.get(id=update['id']).specific
                page.description = update['description']
                page.save_revision().publish()
                self.stdout.write(self.style.SUCCESS(
                    f"Updated page ID {update['id']} successfully."
                ))
            except ArticlePage.DoesNotExist:
                self.stdout.write(self.style.ERROR(
                    f"Page with ID {update['id']} not found."
                ))
            except Exception as e:
                self.stdout.write(self.style.ERROR(
                    f"Error updating page ID {update['id']}: {str(e)}"
                ))
