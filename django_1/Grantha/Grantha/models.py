from django.db import models
from django.db.models.signals import pre_save
from django.template.defaultfilters import slugify
from autoslug import AutoSlugField


class Books(models.Model):
    book_id = models.IntegerField()
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    avg_rating = models.DecimalField(max_digits=3, decimal_places=2)
    isbn = models.CharField(max_length=11, null=True)
    isbn13 = models.CharField(null=True, max_length=13)
    slug = models.SlugField(max_length=250,blank=True)
    language = models.CharField(max_length=8)
    pages = models.IntegerField(null=True)
    rating_count = models.IntegerField(null=True)
    reviews_count = models.IntegerField(null=True)


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        slug_str = '%s-%s-%s-%s' % (instance.title, instance.author, instance.isbn, instance.book_id)
        instance.slug = slugify(slug_str)


pre_save.connect(slug_generator, sender=Books)
