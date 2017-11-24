from django.db import models


class LnrzUrl(models.Model):
    url = models.CharField(max_length=220)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return srt(self.str)
