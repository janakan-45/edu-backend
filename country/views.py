from django.http import JsonResponse
from .models import Country

def country_list(request):
    countries = Country.objects.all()
    data = []
    for country in countries:
        guide_pages_data = []
        if country.guide_pages:
            for block in country.guide_pages:
                content = {}
                if block.block_type == 'cover':
                    content = {
                        'title': block.value['title'],
                        'subtitle': block.value['subtitle']
                    }
                elif block.block_type == 'text':
                    content = {
                        'heading': block.value['heading'],
                        'content': block.value['content'],
                        'icon': block.value['icon']
                    }
                elif block.block_type == 'image':
                    img_obj = block.value['image']
                    img_url = None
                    if img_obj:
                         img_url = request.build_absolute_uri(img_obj.file.url)
                    
                    content = {
                        'heading': block.value['heading'],
                        'image': img_url,
                        'caption': block.value['caption']
                    }
                elif block.block_type == 'end':
                    content = {
                        'content': block.value['content']
                    }
                
                guide_pages_data.append({
                    'type': block.block_type,
                    **content
                })

        gallery_images = []
        for img in country.gallery_images.all():
            if img.image:
                gallery_images.append({
                     'image': request.build_absolute_uri(img.image.url),
                     'caption': img.caption
                })

        data.append({
            'name': country.name,
            'slug': country.slug,
            'image': request.build_absolute_uri(country.image.url) if country.image else None,
            'description': country.description,
            'gallery': gallery_images,
            'guide': {
                'title': country.guide_title,
                'pages': guide_pages_data
            }
        })
    return JsonResponse(data, safe=False)
