from django.db import models

from shortener.models import LnrzUrl



class ClickEventManager(models.Manager):
    def create_event(self, lnrzInstance):
        if isinstance(lnrzInstance, LnrzUrl):
            obj = self.get_or_create(lnrz_url=lnrzInstance)
            obj.count += 1
            obj.save()
            return obj.count
        return None


class ClickEvent(models.Model):
    lnrz_url  = models.OneToOneField(LnrzUrl)
    count     = models.IntegerField(default=0)
    update    = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ClickEventManager()

    def __str__(self):
        return "{i}".format(i=self.count)
