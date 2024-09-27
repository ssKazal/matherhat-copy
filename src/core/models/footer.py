from django.db import models
from core.utils import generate_uids
import datetime


class Footer(models.Model):

    def _upload_to(self, filename):
        uid = generate_uids()
        now_time = datetime.datetime.now()
        return 'footer/id-'+uid+"/"+ str(now_time.strftime("%Y-%m-%d"))+"/"+filename

    logo = models.ImageField(upload_to=_upload_to, null=True)
    email = models.EmailField(max_length=256, blank=True, null=True)
    phone_no = models.CharField(max_length=256, blank=True, null=True)
    phone_no_bn = models.CharField(max_length=256, blank=True, null=True)
    fb_page_url = models.URLField(max_length=2000, blank=True, null=True)
    address_text = models.TextField(max_length=2000, blank=True, null=True)
    address_text_bn = models.TextField(max_length=2000, blank=True, null=True)
    address_link = models.TextField(max_length=2000, blank=True, null=True)
    address_image = models.ImageField(upload_to=_upload_to, blank=True, null=True)

    def __str__(self):
        return str(self.id)