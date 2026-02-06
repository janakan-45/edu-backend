from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from .models import Country

class CountryViewSet(SnippetViewSet):
    model = Country
    menu_label = 'Countries'
    icon = 'globe'
    list_display = ('name', 'slug', 'guide_title')
    list_filter = ('name',)
    list_export = ('name', 'slug', 'description', 'guide_title')
    search_fields = ('name',)
    add_to_admin_menu = True

register_snippet(CountryViewSet)
