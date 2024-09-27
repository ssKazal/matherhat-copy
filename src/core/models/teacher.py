from django.db import models
from django.db.models import F
from core.utils import generate_uids
from django.core.validators import MinValueValidator
import datetime


class Teacher(models.Model):

    def _upload_to(self, filename):
        uid = generate_uids()
        now_time = datetime.datetime.now()
        return 'teacher/id-'+uid+"/"+ str(now_time.strftime("%Y-%m-%d"))+"/"+filename

    teacher_image = models.ImageField(upload_to=_upload_to, blank=True, null=True)
    name = models.CharField(max_length=256, null=True)
    name_bn = models.CharField(max_length=256, null=True)
    position = models.CharField(max_length=1000, null=True, default='Teacher')
    position_bn = models.CharField(max_length=1000, null=True, default='শিক্ষক')
    description = models.TextField(max_length=2000, null=True)
    description_bn = models.TextField(max_length=2000, null=True)
    rank = models.IntegerField(null=True, validators=[MinValueValidator(1)])

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        teachers_qs = Teacher.objects.all()
        requested_rank = self.rank
        
        if teachers_qs:
            max_rank = teachers_qs.latest('rank').rank      # get current highest rank
            current_rank = None
            if not self.id:     # while add new teacher 
                rank_is_exist = teachers_qs.filter(rank=requested_rank).exists()
                if not rank_is_exist:
                    if requested_rank > max_rank:       # rank's order should not be absent
                        requested_rank = max_rank + 1
                else:
                    current_rank = max_rank + 1
            else:       # while update teachers
                current_rank = teachers_qs.get(id=self.id).rank
                if requested_rank > max_rank:       # rank's order should not be absent
                    requested_rank = max_rank 
                    
            if current_rank:
                self.rank_calculation(current_rank, requested_rank)

        else:
            requested_rank = 1
            
        self.rank = requested_rank
        super(Teacher, self).save(*args, **kwargs)

    def rank_calculation(self, current_rank, requested_rank):
        promotion_kwargs = {
            'rank__gte':requested_rank, 
            'rank__lte':current_rank
        }

        demotion_kwargs  = {
            'rank__lte':requested_rank,
            'rank__gte':current_rank
        }

        if current_rank > requested_rank:
            kwargs = promotion_kwargs
            update_expression = +1
        elif current_rank < requested_rank:
            kwargs = demotion_kwargs
            update_expression = -1
        else:
            return requested_rank

        Teacher.objects.filter(**kwargs).update(rank=F('rank') + update_expression)
