from django.conf.urls import patterns, url
from .views import PortfolioListView, PortfolioDetailView

urlpatterns = patterns("",
    url(r'^$', PortfolioListView.as_view(), name='portfolio-list'),
    url(r'^(?P<pk>\d+)/$', PortfolioDetailView.as_view(), name='portfolio-detail'),
)