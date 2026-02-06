from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from .models import University

class UniversityViewSet(SnippetViewSet):
    model = University
    menu_label = 'Universities'
    icon = 'group' # Using 'group' or similar as a placeholder for university icon
    list_display = ('name', 'country', 'location', 'ranking')
    list_filter = ('country',)
    list_export = ('name', 'country', 'location', 'ranking', 'website', 'description')
    search_fields = ('name', 'location')
    add_to_admin_menu = True

register_snippet(UniversityViewSet)
