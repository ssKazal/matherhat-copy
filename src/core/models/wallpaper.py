from django.db import models
from core.utils import generate_uids
import datetime


class Wallpaper(models.Model):

    def _upload_to(self, filename):
        uid = generate_uids()
        now_time = datetime.datetime.now()
        return 'wallpaper/id-'+uid+"/"+ str(now_time.strftime("%Y-%m-%d"))+"/"+filename

    background_image = models.ImageField(upload_to=_upload_to, null=True)
    text = models.TextField(max_length=2000, null=True)
    text_bn = models.TextField(max_length=2000, null=True)

    def __str__(self):
        return str(self.id)