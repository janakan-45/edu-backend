from django.utils.html import format_html
from wagtail import hooks
from wagtail.admin.menu import MenuItem
from django.urls import reverse


@hooks.register('register_admin_menu_item')
def register_dashboard_menu_item():
    """Register custom Dashboard menu item."""
    return MenuItem('Dashboard', reverse('wagtailadmin_home'), classname='icon icon-home', order=0)


@hooks.register('construct_main_menu')
def customize_admin_menu(request, menu_items):
    """
    Customize Wagtail admin sidebar to show only specific menu items.
    Keeps: Dashboard, Countries, Universities, Bookings, Settings
    Removes: Pages, Images, Documents, Snippets, Search, and other default items
    """
    allowed_menu_items = [
        'dashboard',      # Home/Dashboard
        'countries',      # Country snippets
        'universities',   # University snippets
        'bookings',       # Booking snippets
        'settings',       # Settings menu
    ]

    # Filter menu items to keep only allowed ones
    menu_items[:] = [
        item for item in menu_items
        if item.name in allowed_menu_items
    ]


@hooks.register('construct_settings_menu')
def customize_settings_menu(request, menu_items):
    """
    Customize Settings submenu to show only Users and Groups.
    Removes: Sites, Redirects, and other settings items.
    """
    allowed_settings_items = [
        'users',   # Users management
        'groups',  # Groups management
    ]

    # Filter settings menu items to keep only Users and Groups
    menu_items[:] = [
        item for item in menu_items
        if item.name in allowed_settings_items
    ]


@hooks.register('insert_global_admin_css')
def global_admin_css():
    """
    Inject custom CSS to replace Wagtail magpie logos with custom logo.
    This replaces both the header logo and sidebar menu icons.
    """
    return '''
    <style>
        /* ============================================
           REPLACE WAGTAIL MAGPIE LOGO WITH CUSTOM LOGO
           ============================================ */
        
        /* --------------------------------------------
           1. HEADER TOP-LEFT LOGO (Wagtail branding)
           -------------------------------------------- */
        
        /* Hide the default Wagtail magpie SVG/icon completely */
        .sidebar-branding svg,
        .sidebar-branding .wagtail-icon,
        .sidebar-branding .icon-wagtail,
        .sidebar-branding .icon,
        .sidebar-branding [class*="wagtail"],
        .sidebar-branding [class*="icon"] {
            display: none !important;
            visibility: hidden !important;
            opacity: 0 !important;
            width: 0 !important;
            height: 0 !important;
        }
        
        /* Set custom logo as background on the branding container */
        .sidebar-branding {
            background-image: url('/static/img/logo-removebg-preview.png') !important;
            background-size: contain !important;
            background-repeat: no-repeat !important;
            background-position: center center !important;
            min-height: 60px !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            padding: 10px !important;
        }
        
        /* Make the link transparent but clickable */
        .sidebar-branding a,
        .sidebar-branding__logo {
            display: block !important;
            width: 100% !important;
            height: 100% !important;
            min-height: 50px !important;
            color: transparent !important;
            text-decoration: none !important;
            background: transparent !important;
        }
        
        /* --------------------------------------------
           2. SIDEBAR COLLAPSED MENU LOGO (Round icon)
           -------------------------------------------- */
        
        /* Hide magpie in collapsed sidebar toggle button */
        .sidebar-toggle svg,
        .sidebar-toggle .wagtail-icon,
        .sidebar-toggle .icon-wagtail,
        .sidebar-toggle [class*="wagtail"],
        .sidebar-toggle [class*="icon"] {
            display: none !important;
            visibility: hidden !important;
            opacity: 0 !important;
        }
        
        /* Replace with custom logo in collapsed state */
        .sidebar--collapsed .sidebar-branding,
        .sidebar-collapsed .sidebar-branding {
            background-image: url('/static/img/logo-removebg-preview.png') !important;
            background-size: 35px auto !important;
            min-height: 40px !important;
        }
        
        /* --------------------------------------------
           3. MENU ITEM ICONS (Countries, Universities, Bookings)
           -------------------------------------------- */
        
        /* Replace default icons with custom logo for specific menu items */
        .sidebar-menu-item a[href*="countries"] .icon::before,
        .sidebar-menu-item a[href*="universities"] .icon::before,
        .sidebar-menu-item a[href*="bookings"] .icon::before {
            content: "" !important;
            background-image: url('/static/img/logo-removebg-preview.png') !important;
            background-size: contain !important;
            background-repeat: no-repeat !important;
            background-position: center !important;
            width: 18px !important;
            height: 18px !important;
            display: inline-block !important;
        }
        
        /* --------------------------------------------
           4. MOBILE/RESPONSIVE LOGO
           -------------------------------------------- */
        
        /* Ensure logo displays correctly on mobile */
        @media (max-width: 768px) {
            .sidebar-branding {
                background-size: 70% auto !important;
                min-height: 50px !important;
            }
        }
        
        /* --------------------------------------------
           5. REMOVE SEARCH MENU (if still visible)
           -------------------------------------------- */
        
        /* Hide search menu item */
        .sidebar-menu-item a[href*="search"] {
            display: none !important;
        }
    </style>
    '''
