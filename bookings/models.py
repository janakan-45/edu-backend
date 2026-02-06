from django.db import models
from wagtail.admin.panels import FieldPanel

class Booking(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)
    destination = models.CharField(max_length=100)
    start_date = models.CharField(max_length=100)
    office = models.CharField(max_length=100)
    counselling_mode = models.CharField(max_length=100)
    
    created_at = models.DateTimeField(auto_now_add=True)

    panels = [
        FieldPanel('first_name'),
        FieldPanel('last_name'),
        FieldPanel('email'),
        FieldPanel('phone_number'),
        FieldPanel('destination'),
        FieldPanel('start_date'),
        FieldPanel('office'),
        FieldPanel('counselling_mode'),
    ]

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.destination}"
