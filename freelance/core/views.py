from annoying.decorators import render_to
from freelance.core.models import PortfolioItem

@render_to('core/index.html')
def index(request):
	portfolio_items = PortfolioItem.objects.order_by('-date')
	return {"portfolio_items": portfolio_items}

