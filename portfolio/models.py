from urlparse import urlparse

from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from mezzanine.pages.models import Displayable
from mezzanine.core.models import RichText, Slugged
from mezzanine.utils.models import upload_to

from taggit.managers import TaggableManager

class Item(Displayable, RichText):
    projectName = models.TextField()
    featured = models.BooleanField(default=False)
    projectDescription = models.TextField()
    source = models.URLField(blank=True)

    tags = TaggableManager()

    class Meta:
        verbose_name = _("Portfolio item")
        verbose_name_plural = _("Portfolio item")
        ordering = ("-featured",)

    def get_absolute_url(self):
        return reverse('portfolio-detail', args=[self.slug])

    def get_source_repo(self):
        return urlparse(self.source).netloc or "not available"

    def __unicode__(self):
        return self.projectName

class PortfolioImage(models.Model):
    # mostly from mezzanine/galleries/models.py
    portfolioItem = models.ForeignKey("Item", related_name="Images")
    description = models.CharField(_("Description"), max_length=1000, blank=True)
    # changed from image > file
    file = models.FileField(_("File"), max_length=200,
                             upload_to=upload_to("portfolio.images.file", "portfolio"))

    class Meta:
        verbose_name = _("Portfolio image")
        verbose_name_plural = _("Portfolio images")

    def __unicode__(self):
        return self.description

