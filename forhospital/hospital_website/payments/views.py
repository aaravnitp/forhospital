from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import PaymentForm


def payments(request):
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Payment submitted successfully!")
            return redirect("payments")
    else:
        form = PaymentForm()

    return render(request, "paymentshome.html", {"form": form})
