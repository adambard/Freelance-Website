from annoying.decorators import render_to, ajax_request
from freelance.core.models import PortfolioItem
from freelance.core.forms import ContactForm
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect

from django.conf import settings

@render_to('core/index.html')
def index(request):
	"Show the frontpage, with only frontpage-flagged portfolio items"
	
	portfolio_items = PortfolioItem.objects.filter(frontpage=True)
	return {"portfolio_items": portfolio_items}

@render_to('core/portfolio.html')
def portfolio(request):
	"Show all items in the portfolio."
	
	portfolio_items = PortfolioItem.objects.all()
	return {"portfolio_items": portfolio_items}

@render_to('core/portfolio.html')
def tag(request, tag):
	"Show all items in a portfolio view, filtered by tag."
	
	portfolio_items = PortfolioItem.objects.filter(tag__name__iexact=tag)
	return {"portfolio_items": portfolio_items, "tag": tag}

@render_to('core/contact_form.html')
def contact_form(request):
	"Show a contact form that emails the admin list"

	if request.method == "POST":
		form = ContactForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			desc = form.cleaned_data['description']

			# Send me an email
			subject = "Quote request from %s" % name
			message = "Name: %s\nEmail: %s\n\n%s\n" % (name, email, desc)

			
			email_message = EmailMessage(
					u'%s%s' % (settings.EMAIL_SUBJECT_PREFIX, subject),
					message, settings.SERVER_EMAIL, [a[1] for a in settings.ADMINS],
					connection=None, headers={'Reply-To': email})

			email_message.send(fail_silently=True)

			return HttpResponseRedirect("/thanks/")
	else:
		form = ContactForm()

	return {"form": form}
