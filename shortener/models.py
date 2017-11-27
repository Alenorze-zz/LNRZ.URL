from django.db import models
from django.conf import settings

from .utils import code_generator, create_shortcode
from .validators import validate_url, validate_dot_com

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)


class LnrzUrlManager(models.Manager):
    def all(self, *args, **kwargs):
        qs = super(LnrzUrlManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=False)
        return qs
    
    def refresh_shortcodes(self, items=None):
        qs = KirrURL.objects.filter(id__gte=1)
        if items is not None and isinstance(items, int):
            qs = qs.order_by('-id')[:items]
        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            print(q.id)
            q.save()
            new_codes += 1
        return "New codes made: {i}".format(i=new_codes)


class LnrzUrl(models.Model):
    url       = models.CharField(max_length=220, validators=[validate_url, validate_dot_com])
    shortcode = models.CharField(max_length=15, unique=True, blank=True)
    update    = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active    = models.BooleanField(default=True)
    objects   = LnrzUrlManager()

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == '':
            self.shortcode = create_shortcode(self)
        super(LnrzUrl, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return srt(self.str)
