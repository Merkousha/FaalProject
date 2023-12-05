from django.db import models

class Faal(models.Model):
    title = models.CharField(max_length=255)
    full_title = models.CharField(max_length=255)
    html_text = models.TextField()
    mp3_url = models.URLField()

    def __str__(self):
        return self.title
