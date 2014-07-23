from django.db import models

from mezzanine.pages.models import Page, Displayable
from mezzanine.core.models import RichText
# Create your models here.

class Item(Displayable):
    submitted = models.DateTimeField()

    projectName = models.TextField()
    published = models.BooleanField(default=True)
    projectDescription = models.TextField()
    source = models.URLField()

    def get_absolute_url(self):
        return "/portfolio/%i" %self.id