from django.contrib import admin
from .models import Contact, PhoneNumber

# Register your models here.

class PhoneNumberInline(admin.TabularInline):
    model = PhoneNumber
    extra = 1  # Show 1 empty phone number field by default


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'group', 'favourite', 'created_at']
    inlines = [PhoneNumberInline]
