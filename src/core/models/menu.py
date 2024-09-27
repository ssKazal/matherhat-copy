from django.db import models
from core.utils import generate_uids
import datetime


class Menu(models.Model):

    def _upload_to(self, filename):
        uid = generate_uids()
        now_time = datetime.datetime.now()
        return 'menu/id-'+uid+"/"+ str(now_time.strftime("%Y-%m-%d"))+"/"+filename

    logo = models.ImageField(upload_to=_upload_to, null=True)

    def __str__(self):
        return str(self.id)