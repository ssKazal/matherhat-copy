from django.db import models


class NoticeBoard(models.Model):
    text = models.TextField(max_length=2000, null=True)
    text_bn = models.TextField(max_length=2000, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Notices'

    def __str__(self):
        return str(self.id)