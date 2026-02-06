from django.http import JsonResponse
from .models import University
from country.models import Country

def university_list(request):
    country_slug = request.GET.get('country')
    universities = University.objects.all()
    
    if country_slug:
        universities = universities.filter(country__slug=country_slug)

    data = []
    for uni in universities:
        gallery_images = []
        for img in uni.gallery_images.all():
            if img.image:
                gallery_images.append({
                     'image': request.build_absolute_uri(img.image.url),
                     'caption': img.caption
                })

        data.append({
            'name': uni.name,
            'location': uni.location,
            'image': request.build_absolute_uri(uni.image.url) if uni.image else None,
            'gallery': gallery_images,
            'description': uni.description,
            'ranking': uni.ranking,
            'website': uni.website,
            'country': uni.country.name,
            'country_slug': uni.country.slug,
        })
    return JsonResponse(data, safe=False)
