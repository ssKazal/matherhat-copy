from django.db import models
from core.utils import generate_uids
import datetime


class SummarySlider(models.Model):

    def _upload_to(self, filename):
        uid = generate_uids()
        now_time = datetime.datetime.now()
        return 'summary_slider/id-'+uid+"/"+ str(now_time.strftime("%Y-%m-%d"))+"/"+filename

    slider_image = models.ImageField(upload_to=_upload_to, null=True)
    title = models.CharField(max_length=1000, null=True)
    title_bn = models.CharField(max_length=1000, null=True)
    description = models.TextField(max_length=2000, blank=True, null=True)
    description_bn = models.TextField(max_length=2000, blank=True, null=True)

    class Meta:
        verbose_name = 'summary slider'
        verbose_name_plural = 'summary sliders'

    def __str__(self):
        return str(self.id)