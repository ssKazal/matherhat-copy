from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from core.utils import COUNTRY, SUBJECT


class ContactUs(models.Model):
    name = models.CharField(max_length=256, null=True)
    email = models.EmailField(max_length=256, blank=True, null=True)
    country = models.CharField(max_length=10, null=True, choices=COUNTRY)
    phone = models.CharField(max_length=50, blank=True, null=True)
    subject = models.CharField(max_length=10, choices=SUBJECT, default=1)
    message = models.TextField(max_length=2000, null=True)

    class Meta:
        verbose_name_plural = 'contacts'

    def __str__(self):
        return self.name

    def clean(self):
        if not (self.name and self.message):
            raise ValidationError("Name and Message required")
        elif not (self.email or self.phone):
            raise ValidationError("Atleast 1 required in Email and Phone")