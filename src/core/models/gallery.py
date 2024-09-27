from django.db import models
from core.utils import generate_uids
import datetime


class Gallery(models.Model):

    def _upload_to(self, filename):
        uid = generate_uids()
        now_time = datetime.datetime.now()
        return 'gallery/id-'+uid+"/"+ str(now_time.strftime("%Y-%m-%d"))+"/"+filename

    image = models.ImageField(upload_to=_upload_to, null=True)
    text = models.TextField(max_length=2000, blank=True, null=True)
    text_bn = models.TextField(max_length=2000, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'galleries'

    def __str__(self):
        return str(self.id)