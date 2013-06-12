from django.db import models

TEMPLATE = (
        ('H', 'Home'),
        ('B', 'Blog'),
        ('P', 'Page'),
        ('M', 'Menu'),
        ('G', 'Gallery'),
        ('C', 'Contact'),
)

PERMISSIONS = (
            ('U', 'User'),
            ('S', 'Super'),
            ('A', 'Admin'),
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
    author = models.ForeignKey(BrossUser)
    title = models.CharField(max_length=255)
    url = models.SlugField(unique=True)
    datetime = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=255)
    template = models.CharField(max_length=1, choices=TEMPLATE)
    content = models.TextField()
    location = models.CharField(max_length=255)
    hasparent = models.IntegerField(max_length=11)
    parent = models.ForeignKey('self', null=True, blank=True)
    menu = models.IntegerField(max_length=11)
    status = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.title