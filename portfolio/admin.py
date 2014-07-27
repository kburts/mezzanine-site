from django.contrib import admin
from mezzanine.pages.admin import DisplayableAdmin
from .models import Item

from copy import deepcopy
# Register your models here.


class PortfolioItemAdmin(DisplayableAdmin):
    """
    Admin class for portfolio items
    """
    fieldsets = (
        deepcopy(DisplayableAdmin.fieldsets[0]),
        ("Project Details",
            {"fields":
                 ("projectName", "projectDescription", "published", "source",)
            }
        ),
        deepcopy(DisplayableAdmin.fieldsets[1]),
    )


admin.site.register(Item, PortfolioItemAdmin)