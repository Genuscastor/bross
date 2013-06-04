from django.db import models

TEMPLATE_CHOICES = (
		('L', 'Landing'),
		('B', 'Blog'),
		('G', 'Gallery'),
		('C', 'Contact'),
)

PARENT_CHOICES = (
		#dik automatisch gegenereerde lijst met parents
		('1', 'Parent 1'),
		('2', 'Parent 2'),
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

class Page(models.Model):
        # author		= models.OneToOneField(User)
        # lastEdit		= models.OneToOneField(Edit) ofzo
        title		= models.CharField(max_length=100)
        url			= models.SlugField(unique=True)
        dateTime	= models.DateTimeField(auto_now=True)
        description	= models.CharField(max_length=300)
        content     = models.TextField()
        location	= models.CharField(max_length=100)
        template    = models.CharField(max_length=1, choices=TEMPLATE_CHOICES)
        parent		= models.CharField(max_length=1, choices=PARENT_CHOICES)
        menu		= models.CharField(max_length=1, choices=MENU_CHOICES)
        status		= models.CharField(max_length=1, choices=STATUS_CHOICES)

        def __unicode__(self):
                return self.title