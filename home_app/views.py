from django.shortcuts import render
import json, os
from django.conf import settings

def get_data():
    data_path = os.path.join(settings.BASE_DIR, 'data.json')
    if os.path.exists(data_path):
        with open(data_path, 'r') as f:
            return json.load(f)
    return {}

from django.shortcuts import render
from gallery_app.models import GalleryItem
from .models import Convenor
def home(request):
    convenor = Convenor.objects.first()

    latest_posts = GalleryItem.objects.order_by('-date_captured')[:3]

    context = {
        'convenor': convenor,
        'posts': latest_posts,
    }

    return render(
        request,
        'home_app/home.html',
        context
    )
