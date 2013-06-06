from django.db import models

class Menu(models.Model):
	name            = models.CharField(max_length=200)
	parent          = models.ForeignKey('Parent')
	description     = models.TextField(blank=True)

        def __unicode__(self):
                return self.name

class Parent(models.Model):
        name            = models.CharField(max_length=200)
        description     = models.TextField(blank=True)

        def __unicode__(self):
                return self.name