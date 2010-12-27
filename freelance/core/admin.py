from django.contrib.admin import site
from freelance.core.models import PortfolioItem, PortfolioTag

site.register(PortfolioItem)
site.register(PortfolioTag)
