from django.urls import reverse
from django.core.mail import send_mail, EmailMultiAlternatives

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from core.models import ContactUs

from core.api.serializers import ContactUsSerializer

from matherhatmadrasah.settings import EMAIL_HOST_USER, EMAIL_TO_GO, DOMAIN


class ContactUsViewSet(viewsets.ViewSet):
    def list(self, request):
        contacts = ContactUs.objects.all().order_by('-id')
        serializer = ContactUsSerializer(contacts, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ContactUsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            path = reverse('admin:core_contactus_change', args=[serializer.data['id']])
            url = 'http://{domain}{path}'.format(domain=DOMAIN, path=path)
            subject, from_email, to = 'Matherhatmadrasah', EMAIL_HOST_USER, EMAIL_TO_GO
            text_content = 'Assalamualaikum, \
                        You website matherhatmadrasah.com got a new message. \
                        Visit LINK to view. \
                        Salam \
                        Team Vaid Tech Services'
            html_content = f'<h4>Assalamualaikum,</h4><p>You website matherhatmadrasah.com got a new message. <br> \
                            Visit <a href="{ url }">LINK</a> to view.<p>Salam<br>Team Vaid Tech Services</p>'
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)