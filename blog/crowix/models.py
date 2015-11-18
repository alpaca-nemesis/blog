from django.db import models

# Create your models here.
class artical(models.Model):
	title = models.CharField(u'title',max_length=80)
	content = models.TextField(u'content')
	tag = models.CharField(u'tag',max_length=20)
	slug = models.CharField(u'slug', max_length=256, db_index=True)

	def __unicode__(self):
		return self.title


class message(models.Model):
	name = models.CharField(u'name',max_length=50)
	mail = models.CharField(u'mail',max_length=30)
	phone = models.CharField(u'phone',max_length=30)
	content = models.TextField(u'content')

	def __unicode__(self):
		return self.name