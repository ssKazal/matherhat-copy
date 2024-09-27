from rest_framework import serializers
from core.models import ContactUs


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ('id', 'name', 'email', 'country', 'phone', 'subject', 'message')
        extra_kwargs = {
            'name': {'required': True, 'allow_null': False},
            'message': {'required': True, 'allow_null': False},
            'country': {'required': True, 'allow_null': False},
            'subject': {'required': True, 'allow_null': False},
		}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].error_messages['required'] = ('%s is required to fill'%field.replace('_',' '))
            self.fields[field].error_messages['blank'] = ('%s can not be blank'%field.replace('_',' '))
            self.fields[field].error_messages['null'] = ('%s can not be null'%field.replace('_',' '))
    

    def validate(self, data):
        instance = ContactUs(**data)
        instance.full_clean()
        return data
      
