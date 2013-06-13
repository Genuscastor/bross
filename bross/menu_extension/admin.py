from django.contrib import admin
from bross.treemenus.admin import MenuAdmin, MenuItemAdmin
from bross.treemenus.models import Menu
from bross.menu_extension.models import MenuItemExtension

class MenuItemExtensionInline(admin.StackedInline):
    model = MenuItemExtension
    max_num = 1

class CustomMenuItemAdmin(MenuItemAdmin):
    inlines = [MenuItemExtensionInline,]

class CustomMenuAdmin(MenuAdmin):
    menu_item_admin_class = CustomMenuItemAdmin

admin.site.unregister(Menu) # Unregister the standard admin options
admin.site.register(Menu, CustomMenuAdmin) # Register the new, customized, admin options