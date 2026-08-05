from django import forms

from .models import Payment


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ["patient_name", "email", "amount", "payment_method"]
        widgets = {
            "patient_name": forms.TextInput(attrs={"id": "patientName"}),
            "email": forms.EmailInput(attrs={"id": "email"}),
            "amount": forms.NumberInput(attrs={"id": "amount", "step": "0.01"}),
            "payment_method": forms.Select(attrs={"id": "paymentMethod"}),
        }
