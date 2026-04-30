from django.shortcuts import render
from django.core.paginator import Paginator
from .models import GalleryItem

def gallery(request):
    category = request.GET.get('category', 'All')

    if category == 'All':
        qs = GalleryItem.objects.order_by('-date_captured')  
    else:
        qs = GalleryItem.objects.filter(category=category).order_by('-date_captured')

    paginator = Paginator(qs, 12)
    page_number = request.GET.get('page')
    items = paginator.get_page(page_number)

    return render(request, 'gallery_app/gallery.html', {
        'items': items,
        'active_category': category
    })
