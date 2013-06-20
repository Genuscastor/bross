from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Account(models.Model):
        user         = models.OneToOneField(User)
        email        = models.CharField(max_length=100)
        name         = models.CharField(max_length=100)

        def __unicode__(self):
                return self.name

#create our user object to attach to our user object
def create_account_user_callback(sender, instance, **kwargs):
	account, new = Account.objects.get_or_create(user=instance)
post_save.connect(create_account_user_callback, User)