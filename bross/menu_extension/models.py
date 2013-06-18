from django.db import models
from treemenus.models import MenuItem
from django.utils.translation import ugettext_lazy
from django.utils.translation import ugettext as _

class MenuItemExtension(models.Model):
    menu_item = models.OneToOneField (MenuItem, related_name="extension")
    published = models.BooleanField(ugettext_lazy('published'), default=False)