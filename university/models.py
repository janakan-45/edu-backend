from django.db import models
from wagtail.admin.panels import FieldPanel, InlinePanel
from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey
from wagtail.models import Orderable

class University(ClusterableModel):
    name = models.CharField(max_length=255)
    country = models.ForeignKey('country.Country', on_delete=models.CASCADE, related_name='universities')
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='university_images/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    ranking = models.CharField(max_length=255, blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    panels = [
        FieldPanel('name'),
        FieldPanel('country'),
        FieldPanel('location'),
        FieldPanel('image'),
        InlinePanel('gallery_images', label="Gallery Images"),
        FieldPanel('description'),
        FieldPanel('ranking'),
        FieldPanel('website'),
    ]

    class Meta:
        verbose_name_plural = 'Universities'

    def __str__(self):
        return self.name

class UniversityGalleryImage(Orderable):
    university = ParentalKey(University, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ImageField(upload_to='university_gallery/', blank=True, null=True)
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]
