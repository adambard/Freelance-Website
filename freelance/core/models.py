from django.db import models
import datetime

class TimeStampedModel(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

class PortfolioItem(TimeStampedModel):
	"""
	A single item in the portfolio
	"""
	title = models.CharField(max_length=200)
	image = models.ImageField(upload_to="portfolio_images/%Y")
	description = models.TextField()
	date = models.DateField()
	link = models.URLField(blank=True, null=True, verify_exists=True)
	tag = models.ManyToManyField('PortfolioTag', null=True, blank=True)
	frontpage = models.BooleanField(default=False)
	class Meta:
		ordering = ('-date',)

	def __unicode__(self):
		return self.title

class PortfolioTag(TimeStampedModel):
	name = models.CharField(max_length=64)
	class Meta:
		ordering = ('name',)

	def __unicode__(self):
		return self.name

	@models.permalink
	def get_absolute_url(self):
		return ('tag', [self.name])
