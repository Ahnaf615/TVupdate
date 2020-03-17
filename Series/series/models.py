from django.db import models
from django.utils import timezone


# Create your models here.
class Series(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='gallery')
    time_posted = models.DateTimeField(default=timezone.now, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name_plural = "Series"


class Seasons(models.Model):
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    content = models.TextField(max_length=2000)
    image = models.ImageField(default='default.jpeg', upload_to='gallery')
    time_posted = models.DateTimeField(default=timezone.now, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name_plural = "Seasons"


class Episodes(models.Model):
    season = models.ForeignKey(Seasons, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    content = models.TextField(max_length=2000)
    image = models.ImageField(default='default.jpeg', upload_to='gallery')
    time_posted = models.DateTimeField(default=timezone.now, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name_plural = "Episodes"
