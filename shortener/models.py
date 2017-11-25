from django.db import models
import random



def code_generator(size=6, chars='abcdtyuiopf'):
    return ''.join(random.choice(chars) for _ in range (size))
    

class LnrzUrl(models.Model):
    url = models.CharField(max_length=220)
    shortcode = models.CharField(max_length=15, unique=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.shortcode = code_generator()
        super(LnrzUrl, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return srt(self.str)
