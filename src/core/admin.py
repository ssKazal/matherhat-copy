from django.contrib import admin
from django.db.models import F
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _

from .models import *


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        if self.model.objects.filter()[1:]:
            return super().has_add_permission(request)
        return False

    def logo_url(self, obj):
        if obj.logo:
            return format_html('<a target="_blank" href="{0}">{0}</a>&nbsp;', obj.logo.url)

    logo_url.short_description = 'logo'
    logo_url.allow_tags = True

    list_display = ['id', 'logo_url']


@admin.register(Wallpaper)
class WallpaperAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        if self.model.objects.filter()[1:]:
            return super().has_add_permission(request)
        return False

    def background_image_url(self, obj):
        if obj.background_image:
            return format_html('<a target="_blank" href="{0}">{0}</a>&nbsp;', obj.background_image.url)

    background_image_url.short_description = 'background image'
    background_image_url.allow_tags = True

    list_display = ['id', 'background_image_url', 'text', 'text_bn']


@admin.register(SummarySlider)
class SummarySliderAdmin(admin.ModelAdmin):
    def slider_image_url(self, obj):
        if obj.slider_image:
            return format_html('<a target="_blank" href="{0}">{0}</a>&nbsp;', obj.slider_image.url)

    slider_image_url.short_description = 'slider image'
    slider_image_url.allow_tags = True

    list_display = ['id', 'slider_image_url', 'title', 'title_bn', 'description', 'description_bn']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    def delete_queryset(self, request, queryset):
        qs = Teacher.objects.all().order_by('rank').exclude(id__in=queryset)
        teacher_list = []
        for index, teacher in enumerate(qs):
            teacher.rank = index + 1
            teacher_list.append(teacher)
        Teacher.objects.bulk_update(teacher_list, ['rank'])
        return super().delete_queryset(request, queryset)

    def delete_model(self, request, obj):
        Teacher.objects.all().order_by('-rank').filter(rank__gt=obj.rank).update(rank=F('rank') - 1)
        return super().delete_model(request, obj)
    
    def teacher_image_url(self, obj):
        if obj.teacher_image:
            return format_html('<a target="_blank" href="{0}">{0}</a>&nbsp;', obj.teacher_image.url)

    teacher_image_url.short_description = 'teacher image'
    teacher_image_url.allow_tags = True

    list_display = ['id', 'teacher_image_url', 'name', 'name_bn', 'position', 'position_bn', 'description', 'description_bn', 'rank']


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    def image_url(self, obj):
        if obj.image:
            return format_html('<a target="_blank" href="{0}">{0}</a>&nbsp;', obj.image.url)

    image_url.short_description = 'image'
    image_url.allow_tags = True

    list_display = ['id', 'image_url', 'text', 'text_bn']


@admin.register(MadrasahFigure)
class MadrasahFigureAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        if self.model.objects.filter()[1:]:
            return super().has_add_permission(request)
        return False
    
    list_display = ['id', 'teacher', 'teacher_bn', 'student', 'student_bn', 'staff', 'staff_bn', 'active_year', 'active_year_bn']


@admin.register(NoticeBoard)
class NoticeBoardAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'text_bn', 'pub_date']


@admin.register(SupportForMadrasah)
class SupportForMadrasahAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        if self.model.objects.filter()[1:]:
            return super().has_add_permission(request)
        return False

    list_display = ['id', 'bank_acc_name', 'bank_acc_name_bn', 'bank_acc_no', 'bank_acc_no_bn', 'bank_branch', 'bank_branch_bn', 'bkash_number', 'bkash_number_bn', 'rocket_number', 'rocket_number_bn']


@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        if self.model.objects.filter()[1:]:
            return super().has_add_permission(request)
        return False

    def logo_url(self, obj):
        if obj.logo:
            return format_html('<a target="_blank" href="{0}">{0}</a>&nbsp;', obj.logo.url)

    logo_url.short_description = 'logo'
    logo_url.allow_tags = True

    def address_image_url(self, obj):
        if obj.address_image:
            return format_html('<a target="_blank" href="{0}">{0}</a>&nbsp;', obj.address_image.url)

    address_image_url.short_description = 'address image'
    address_image_url.allow_tags = True

    list_display = ['id', 'logo_url', 'email', 'phone_no', 'phone_no_bn', 'fb_page_url', 'address_text', 'address_text_bn', 'address_link', 'address_image_url']


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'country', 'phone', 'subject', 'message']
