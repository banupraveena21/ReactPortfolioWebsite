from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "message", "created_at")  # shows columns in list
    search_fields = ("name", "email", "message")   # search bar
    list_filter = ("created_at",)                  # filter by date
    ordering = ("-created_at",)                    # latest first
