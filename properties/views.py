
from django.shortcuts import render, get_object_or_404
from .models import Property
from django.db.models import Q

def home(request):
    featured_properties = Property.objects.filter(
        is_published=True,
        is_featured=True
    )

    return render(request, 'home.html', {
        'featured_properties': featured_properties
    })


def rent(request):
    properties = Property.objects.filter(
        category='rent',
        availability='available',
        is_published=True
    )

    return render(request, 'rent.html', {
        'properties': properties
    })


def sales(request):
    properties = Property.objects.filter(
        category='sale',
        availability='available',
        is_published=True
    )

    return render(request, 'sales.html', {
        'properties': properties
    })


def commercial(request):
    properties = Property.objects.filter(
        category='commercial',
        availability='available',
        is_published=True
    )

    return render(request, 'commercial.html', {
        'properties': properties
    })


def plots(request):
    properties = Property.objects.filter(
        category='plot',
        availability='available',
        is_published=True
    )

    return render(request, 'plotland.html', {
        'properties': properties
    })


def interior(request):
    properties = Property.objects.filter(
        category='interior',
        availability='available',
        is_published=True
    )

    return render(request, 'interior.html', {
        'properties': properties
    })


# UNIVERSAL PROPERTY DETAIL PAGE
def property_detail(request, pk):

    property = get_object_or_404(
        Property,
        pk=pk,
        is_published=True
    )

    gallery_images = property.images.all()

    return render(request, 'property_detail.html', {
        'property': property,
        'gallery_images': gallery_images
    })



def search_properties(request):
    keyword = (
        request.GET.get('keyword')
        or request.GET.get('q')
        or ''
    ).strip()

    location = request.GET.get('location', '').strip()

    properties = Property.objects.filter(
        is_published=True,
        availability='available'
    )

    if keyword:
        properties = properties.filter(
            Q(title__icontains=keyword) |
            Q(location__icontains=keyword)
        )

    if location:
        properties = properties.filter(
            location__icontains=location
        )

    properties = properties.distinct()

    context = {
        'properties': properties,
        'query': keyword,
        'location': location,
        'result_count': properties.count(),
    }

    return render(request, 'search_results.html', context)



def about(request):
    return render(request, "about.html")