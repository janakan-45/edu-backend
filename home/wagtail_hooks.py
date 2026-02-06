from wagtail import hooks
from wagtail.admin.menu import MenuItem
from django.urls import reverse
@hooks.register('register_admin_menu_item')
def register_dashboard_menu_item():
    return MenuItem('Dashboard', reverse('wagtailadmin_home'), classname='icon icon-home', order=0)

