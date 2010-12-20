from django.db import models
import datetime

class TimeStampedField(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

class PortfolioItem(models.Model):
	"""
	A single item in the portfolio
	"""
	title = models.CharField(max_length=200)
	image = models.ImageField(upload_to="portfolio_images/%Y")
	description = models.TextField()
	date = models.DateTimeField()
	link = models.URLField(blank=True, null=True, verify_exists=True)
