from django.db import models


class Payment(models.Model):
    """A consultancy-fee payment submission."""

    CREDIT_CARD = "credit_card"
    PAYPAL = "paypal"
    METHOD_CHOICES = [
        (CREDIT_CARD, "Credit Card"),
        (PAYPAL, "PayPal"),
    ]

    patient_name = models.CharField(max_length=200)
    email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=METHOD_CHOICES)
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-submitted_at"]

    def __str__(self):
        return f"{self.patient_name} – {self.amount} ({self.get_payment_method_display()})"
