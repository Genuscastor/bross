from django.db import models

class BrossContent(models.Model):
    author = models.ForeignKey(BrossUser)
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    template = models.CharField(max_length=255)
    content = models.TextField()
    location = models.CharField(max_length=255)
    hasparent = models.IntergetField(max_length=11)
    partent = models.ManyToMAnyField(BrossContent)
    menu = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.title

class BrossUser(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    permissions = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class BrossOptions(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name