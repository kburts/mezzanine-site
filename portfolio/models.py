from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from mezzanine.pages.models import Displayable
from mezzanine.core.models import RichText, Slugged
# Create your models here.

class Item(Displayable, RichText):
    projectName = models.TextField()
    published = models.BooleanField(default=True)
    projectDescription = models.TextField()
    source = models.URLField(blank=True)

    class Meta:
        verbose_name = _("Portfolio item")
        verbose_name_plural = _("Portfolio item")
        ordering = ("-publish_date",)

    def get_absolute_url(self):
        return "/portfolio/%i" %self.id