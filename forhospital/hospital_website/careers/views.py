from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import CareerApplicationForm


def career(request):
    if request.method == "POST":
        form = CareerApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Application submitted successfully!")
            return redirect("career")
    else:
        form = CareerApplicationForm()

    return render(request, "careershome.html", {"form": form})
