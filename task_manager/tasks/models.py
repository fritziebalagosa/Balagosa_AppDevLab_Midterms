from django.db import models
from datetime import date

class Task(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Overdue', 'Overdue'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, editable=False)  # Auto-set status
    is_completed = models.BooleanField(default=False)  # Checkbox for marking as "Done"

    def save(self, *args, **kwargs):
        """Automatically update status based on due_date and completion state."""
        today = date.today()

        if self.is_completed:
            self.status = 'Completed'
        else:
            if self.due_date < today:
                self.status = 'Overdue'
            else:
                self.status = 'Pending'
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} - {self.status} (Due: {self.due_date})"
