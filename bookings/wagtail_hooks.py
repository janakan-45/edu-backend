from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail.permission_policies import ModelPermissionPolicy
from .models import Booking

class BookingPermissionPolicy(ModelPermissionPolicy):
    def user_has_permission(self, user, action):
        if action == 'add':
            return False
        return super().user_has_permission(user, action)

class BookingViewSet(SnippetViewSet):
    model = Booking
    menu_label = 'Bookings'
    icon = 'mail'
    list_display = ('first_name', 'last_name', 'email', 'destination', 'created_at')
    list_filter = ('destination', 'office', 'created_at')
    list_export = ('first_name', 'last_name', 'email', 'phone_number', 'destination', 'start_date', 'office', 'counselling_mode', 'created_at')
    search_fields = ('first_name', 'last_name', 'email')
    add_to_admin_menu = True
    permission_policy = BookingPermissionPolicy(Booking)

register_snippet(BookingViewSet)
