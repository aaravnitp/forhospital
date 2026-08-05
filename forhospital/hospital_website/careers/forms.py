from django import forms

from .models import CareerApplication


class CareerApplicationForm(forms.ModelForm):
    class Meta:
        model = CareerApplication
        fields = ["full_name", "email", "resume_note", "message"]
        widgets = {
            "full_name": forms.TextInput(attrs={"id": "fullName"}),
            "email": forms.EmailInput(attrs={"id": "email"}),
            "resume_note": forms.TextInput(attrs={"id": "resume"}),
            "message": forms.Textarea(attrs={"id": "message", "rows": 4}),
        }
