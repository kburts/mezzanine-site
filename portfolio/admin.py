from django.contrib import admin
from mezzanine.pages.admin import DisplayableAdmin
from mezzanine.core.admin import TabularDynamicInlineAdmin
from .models import Item, PortfolioImage

from copy import deepcopy
# Register your models here.

class PortfolioImageInline(TabularDynamicInlineAdmin):
    model = PortfolioImage

class PortfolioItemAdmin(DisplayableAdmin):
    """
    Admin class for portfolio items
    """
    fieldsets = (
        deepcopy(DisplayableAdmin.fieldsets[0]),
        ("Project Details",
            {"fields":
                 ("projectName", "projectDescription", "featured", "source", "tags",)
            }
        ),
        deepcopy(DisplayableAdmin.fieldsets[1]),
    )
    inlines = (PortfolioImageInline,)


admin.site.register(Item, PortfolioItemAdmin)