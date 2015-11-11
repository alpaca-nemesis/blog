from django.db import models

# Create your models here.
class artical(models.Model):
	title = models.CharField(u'title',max_length=80)
	content = models.TextField(u'content')
	tag = models.CharField(u'tag',max_length=20)

	def __unicode__(self):
		return self.title