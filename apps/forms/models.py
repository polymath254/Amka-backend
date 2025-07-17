from django.db import models

class FormType(models.Model):
    # E.g., "registration", "join", "contribution", "message"
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

class FormSubmission(models.Model):
    REGION_CHOICES = [
        ('nyanza', 'Nyanza'),
        ('nairobi', 'Nairobi'),
        ('eastern', 'Eastern'),
        ('north_eastern', 'North Eastern'),
        ('central', 'Central'),
        ('coast', 'Coast'),
        ('western', 'Western'),
    ]

    form_type = models.ForeignKey(FormType, on_delete=models.CASCADE, related_name="submissions")
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    region = models.CharField(
        max_length=30,
        choices=REGION_CHOICES,
        blank=True,  # Not required on all forms
        help_text="Only required for registration form"
    )
    content = models.TextField(blank=True, help_text="Message or extra info")
    data = models.JSONField(default=dict, blank=True)  # For any extra fields in the future
    is_approved = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)
    reviewed_at = models.DateTimeField(null=True, blank=True)
    reviewer = models.CharField(max_length=100, blank=True)  # Can store reviewer username/email

    class Meta:
        ordering = ['-submitted_at']

    def __str__(self):
        return f"{self.form_type} by {self.full_name}"

