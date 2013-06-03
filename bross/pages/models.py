from django.db import models

class Pages(models.Model):
        # author       = models.OneToOneField(User)
        title        = models.CharField(max_length=100)
        content      = models.CharField(max_length=9999)

        def __unicode__(self):
                return self.title