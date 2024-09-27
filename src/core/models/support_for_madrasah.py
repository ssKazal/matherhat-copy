from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class SupportForMadrasah(models.Model):
    bank_acc_name = models.CharField(max_length=1000, blank=True, null=True)
    bank_acc_name_bn = models.CharField(max_length=1000, blank=True, null=True)
    bank_acc_no = models.CharField(max_length=1000, blank=True, null=True)
    bank_acc_no_bn = models.CharField(max_length=1000, blank=True, null=True)
    bank_branch = models.CharField(max_length=1000, blank=True, null=True)
    bank_branch_bn = models.CharField(max_length=1000, blank=True, null=True)
    bkash_number = models.CharField(max_length=1000, blank=True, null=True)
    bkash_number_bn = models.CharField(max_length=1000, blank=True, null=True)
    rocket_number = models.CharField(max_length=1000, blank=True, null=True)
    rocket_number_bn = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'support for madrasah'

    def __str__(self):
        return str(self.id)

    def clean(self):
        all_of_the_bank_info = (self.bank_acc_name and self.bank_acc_name_bn and self.bank_acc_no and self.bank_acc_no_bn and self.bank_branch and self.bank_branch_bn)
        none_of_the_bank_info = (self.bank_acc_name or self.bank_acc_name_bn or self.bank_acc_no or self.bank_acc_no_bn or self.bank_branch or self.bank_branch_bn)
        
        if all_of_the_bank_info or not none_of_the_bank_info:
            return super().clean()
        else:
            raise ValidationError(_("If one or multiple bank info is provided than all bank information is required."))