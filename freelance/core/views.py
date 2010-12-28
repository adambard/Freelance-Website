from annoying.decorators import render_to
from freelance.core.models import PortfolioItem

@render_to('core/index.html')
def index(request):
	portfolio_items = PortfolioItem.objects.filter(frontpage=True)
	return {"portfolio_items": portfolio_items}

@render_to('core/portfolio.html')
def portfolio(request):
	portfolio_items = PortfolioItem.objects.all()
	return {"portfolio_items": portfolio_items}

@render_to('core/portfolio.html')
def tag(request, tag):
	portfolio_items = PortfolioItem.objects.filter(tag__name__iexact=tag)
	return {"portfolio_items": portfolio_items, "tag": tag}
