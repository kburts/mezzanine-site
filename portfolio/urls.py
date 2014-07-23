from django.conf.urls import patterns, url
from .views import PortfolioListView

urlpatterns = patterns("",
    url(r'^$', PortfolioListView.as_view(), name='portfolio-list'),
)