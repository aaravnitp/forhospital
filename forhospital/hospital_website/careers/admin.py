from django.contrib import admin

from .models import CareerApplication


@admin.register(CareerApplication)
class CareerApplicationAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "submitted_at")
    search_fields = ("full_name", "email")
    readonly_fields = ("submitted_at",)
