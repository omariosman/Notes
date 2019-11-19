from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils.text import slugify
# Create your models here.


class Profile(models.Model):
    user       = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(blank=True, max_length=100)
    last_name  = models.CharField(blank=True, max_length=100)
    slug       = models.SlugField()
    headline   = models.CharField(blank=True, max_length=100)
    bio        = models.CharField(blank=True, max_length=100)
    img        = models.ImageField(upload_to='profile_img')
    join_date  = models.DateTimeField(blank=True, default=datetime.datetime.now)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.first_name)
        super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return self.user
