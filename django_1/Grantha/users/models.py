from django.db import models

from django.contrib.auth.models import User
from PIL import Image
from django.core.validators import MaxValueValidator
from django.utils import timezone
from Grantha.models import Books


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        rgb_img = img.convert('RGB')
        if rgb_img.height > 250 or rgb_img.width > 250:
            save_size = (250, 250)
            rgb_img.thumbnail(save_size)
            rgb_img.save(self.image.path)


class BooksN(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    avg_rating = models.PositiveIntegerField(null=True, validators=[MaxValueValidator(5)])


class Reviews(models.Model):
    comment = models.ForeignKey(Books, on_delete=models.CASCADE, related_name="comment")
    review = models.TextField(null=True)
    rating_choices = (
        ('1', 'waste of time'),
        ('2', 'Not good'),
        ('3', 'good'),
        ('4', 'Great'),
        ('5', 'Masterpiece')
    )
    rating = models.PositiveIntegerField(null=True, choices=rating_choices, validators=[MaxValueValidator(5)])
    datetime = models.DateTimeField(default=timezone.now, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
