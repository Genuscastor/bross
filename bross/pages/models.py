from django.db import models

TEMPLATE = (
        ('H', 'Home'),
        ('B', 'Blog'),
        ('P', 'Page'),
        ('G', 'Gallery'),
        ('C', 'Contact'),
        ('M', 'Menu'),
)

PERMISSIONS = (
            ('U', 'User'),
            ('S', 'Super'),
            ('A', 'Admin'),
)

MENU_CHOICES = (
        #dik automatisch gegenereerde lijst met menus
        ('1', 'Menu 1'),
        ('2', 'Menu 2'),
)

STATUS_CHOICES = (
        ('P', 'Published'),
        ('O', 'Offline'),
) 

class BrossUser(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    permissions = models.CharField(max_length=1, choices=PERMISSIONS)

    def __unicode__(self):
        return self.name

class BrossOption(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name
        
class BrossContent(models.Model):
    #TODO linken aan account en deze dan mee posten.
    author = models.ForeignKey(BrossUser)
    title = models.CharField(max_length=255)
    #TODO - url automatisch genereren, nu moet je het zelf invullen in add_page.html
    url = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=255)
    template = models.CharField(max_length=1, choices=TEMPLATE)
    content = models.TextField(blank=True)
    useSidebar = models.BooleanField()
    sidebarTitle = models.CharField(max_length=100, blank=True)
    sidebar = models.TextField(blank=True)
    location = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True)
    menu        = models.CharField(max_length=1, choices=MENU_CHOICES)
    status      = models.CharField(max_length=1, choices=STATUS_CHOICES)
    
    def __unicode__(self):
        return self.title
