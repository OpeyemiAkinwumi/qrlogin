from .models import PhoneNumber, Contact
from rest_framework import serializers



class PhoneNumberSerializer(serializers.ModelSerializer):
    # contact = ContactSerializer(read_only=True)
    class Meta:
        model = PhoneNumber
        fields = ['number', 'label']

class ContactSerializer(serializers.ModelSerializer):
    phone_numbers = PhoneNumberSerializer(many=True)
    class Meta:
        model = Contact
        fields = ['id', 'name', 'email','group', 'favourite', 'phone_numbers']
