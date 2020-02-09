from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django.contrib.auth.models import User


class Reviews(models.Model):
    review = models.TextField()
    rating = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])
    datetime = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
