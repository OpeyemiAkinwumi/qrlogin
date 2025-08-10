from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    class GroupChoices(models.TextChoices):
        FAMILY = 'Family'
        FRIENDS = 'Friends'
        WORK = 'Work'
        CLIENTS = 'Clients'
        OTHERS = 'Others'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts')
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    group = models.CharField(
        max_length=20,
        choices=GroupChoices.choices,
        default=GroupChoices.OTHERS,
        blank=True,
    ) # family, friends, work, clients, vendors
    favourite = models.BooleanField(default=False)
    image = models.ImageField(upload_to='contact_images', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-name']
        indexes = [
            models.Index(fields=['name', 'email', 'group', 'favourite'])
        ]

    def __str__(self):
        return self.name

class PhoneNumber(models.Model):        
    class LabelChoices(models.TextChoices):
        MOBILE = 'Mobile'
        HOME = 'Home'
        WORK = 'Work'
        WHATSAPP = 'WhatsApp'
        OTHER = 'Other'

    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='phone_numbers')
    number = models.CharField(max_length=20)
    label = models.CharField(
        max_length=20,
        choices=LabelChoices.choices,
        default=LabelChoices.MOBILE,
        blank=True,
    ) # home, work, mobile, whatsapp etc

    def __str__(self):
        return f"{self.label}: {self.number}"