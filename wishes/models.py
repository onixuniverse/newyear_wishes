from django.db import models
from django.urls import reverse


class Wishes(models.Model):
    wish_text = models.TextField()

    class Meta:
        ordering = ["-wish_text"]
        verbose_name = "Wish Text"

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.wish_text
