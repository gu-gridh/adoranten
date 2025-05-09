from django.urls import include, path
from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from search import views as search_views
from journal import views as journal_views
from home import views as home_views
from .api import api_router


urlpatterns = [
    path("django-admin/", admin.site.urls),
    path("wagtail/documents/", include(wagtaildocs_urls)),
    path("wagtail/search/", search_views.search, name="search"),
    path("wagtail/api/v2/articles/", journal_views.ArticleListView.as_view(), name="articles-list"),
    path("wagtail/api/v2/form-submit/<int:page_id>/", home_views.SubmitFormAPIView.as_view(), name="form_submit"),
    path("wagtail/api/v2/", api_router.urls),
    path("wagtail/", include(wagtailadmin_urls)),
]


#if settings.DEBUG:
#    from django.conf.urls.static import static
#    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
#    urlpatterns += staticfiles_urlpatterns()
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    path("", include(wagtail_urls)),
    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    path("pages/", include(wagtail_urls)),
]
