from django.contrib import admin

from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("patient_name", "email", "amount", "payment_method", "submitted_at")
    list_filter = ("payment_method",)
    search_fields = ("patient_name", "email")
    readonly_fields = ("submitted_at",)
