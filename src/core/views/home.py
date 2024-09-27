from django.shortcuts import render

from core.models import *
from core.utils import COUNTRY, SUBJECT

def home(request):
    menu = Menu.objects.first()
    wallpaper = Wallpaper.objects.first()
    summary_sliders = SummarySlider.objects.all().order_by('-id')
    principal = Teacher.objects.order_by('rank').first()
    teachers = Teacher.objects.all().order_by('rank')[1:]
    galleries = Gallery.objects.all().order_by('-id')
    madrasah_figure = MadrasahFigure.objects.first()
    notices = NoticeBoard.objects.all().order_by('-pub_date')
    donation = SupportForMadrasah.objects.first()
    footer = Footer.objects.first()
    
    context: dict = {
        'menu': menu,
        'wallpaper': wallpaper,
        'summary_sliders': summary_sliders,
        'principal': principal,
        'teachers': teachers,
        'galleries': galleries,
        'madrasah_figure': madrasah_figure,
        'notices': notices,
        'donation': donation,
        'footer': footer,
        'subject': SUBJECT,
        'country': COUNTRY,
    }
    return render(request, "home/home.html", context)



