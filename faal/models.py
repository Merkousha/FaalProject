from django.db import models

class Faal(models.Model):
    title = models.CharField(max_length=255)
    full_text = models.TextField(default='')
    faal_text = models.TextField(default='')
    mp3_url = models.URLField()

    def __str__(self):
        return self.title
