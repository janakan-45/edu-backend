from django.db import models
from django.utils.text import slugify
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.panels import FieldPanel, InlinePanel
from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey
from wagtail.models import Orderable

class CoverBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    subtitle = blocks.CharBlock()

    class Meta:
        icon = 'title'

class TextBlock(blocks.StructBlock):
    heading = blocks.CharBlock()
    content = blocks.TextBlock()
    icon = blocks.ChoiceBlock(choices=[
        ('sun', 'Sun'),
        ('landmark', 'Landmark'),
        ('globe', 'Globe'),
        ('coffee', 'Coffee'),
        ('graduation-cap', 'Graduation Cap'),
        ('music', 'Music'),
        ('book-open', 'Book Open'),
        ('briefcase', 'Briefcase'),
    ], required=False)

    class Meta:
        icon = 'doc-full'

class ImageContentBlock(blocks.StructBlock):
    heading = blocks.CharBlock()
    image = ImageChooserBlock()
    caption = blocks.CharBlock(required=False)

    class Meta:
        icon = 'image'

class EndBlock(blocks.StructBlock):
    content = blocks.TextBlock()

    class Meta:
        icon = 'tick'

class Country(ClusterableModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='country_images/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    guide_title = models.CharField(max_length=255, blank=True, null=True, help_text="Title for the country guide")
    guide_pages = StreamField([
        ('cover', CoverBlock()),
        ('text', TextBlock()),
        ('image', ImageContentBlock()),
        ('end', EndBlock()),
    ], use_json_field=True, blank=True, null=True)

    panels = [
        FieldPanel('name'),
        FieldPanel('image'),
        FieldPanel('description'),
        InlinePanel('gallery_images', label="Gallery Images"),
        FieldPanel('guide_title'),
        FieldPanel('guide_pages'),
    ]

    class Meta:
        verbose_name_plural = 'Countries'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class CountryGalleryImage(Orderable):
    country = ParentalKey(Country, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ImageField(upload_to='country_gallery/', blank=True, null=True)
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]
