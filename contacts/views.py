from .serializers import PhoneNumberSerializer, ContactSerializer
from .models import Contact, PhoneNumber

from rest_framework import generics

from rest_framework.permissions import IsAuthenticated


# Create your views here.

class UserContactsView(generics.ListCreateAPIView):
    queryset = Contact.objects.prefetch_related('phone_numbers')
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)