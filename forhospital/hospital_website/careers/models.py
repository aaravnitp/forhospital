from django.db import models


class CareerApplication(models.Model):
    """A job application submitted through the careers page."""

    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField(help_text="Cover letter")
    resume_note = models.CharField(
        max_length=300,
        blank=True,
        help_text="Paste your resume text or note the filename you have ready.",
    )
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-submitted_at"]

    def __str__(self):
        return f"{self.full_name} <{self.email}>"
