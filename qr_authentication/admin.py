from django.contrib import admin
from .models import TemporaryId

# Register your models here.

@admin.register(TemporaryId)
class TemporyIdAdmin(admin.ModelAdmin):
    list_display = ["temp_id", "created_at"]



