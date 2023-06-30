from django.db.models import Min, Max
from django.shortcuts import render, get_object_or_404
from tours import models

dep = {'moscow': 'Москвы', 'peterburg': 'Петербурга', 'novosibirsk': 'Новосибирска', 'yekaterinburg': 'Екатеринбурга',
       'kazan': 'Казани'}


def index(request):
    label = models.Tour.objects.all()
    return render(request, 'tours/index.html', context={
        'label': label,
    })


def departure(request, departure):
    info = models.Tour.objects.filter(city=departure)

    image_ulr = ''
    for image in info:
        image_ulr += image.image

    return render(request, 'tours/departure.html', context={
        'departure': dep[departure],
        'url_address': departure.upper(),
        'quantity': info.count(),
        'val_min': info.aggregate(min_price=Min('price'))['min_price'],
        'val_max': info.aggregate(max_price=Max('price'))['max_price'],
        'nights_min': info.aggregate(min_nights=Min('nights'))['min_nights'],
        'nights_max': info.aggregate(max_nights=Max('nights'))['max_nights'],
        'info': info,
    })


def tour(request, id, departure):
    tour_page = get_object_or_404(models.Tour, id=id)
    return render(request, 'tours/tour.html', context={
        'name_hotel': tour_page.hotel_title,
        'stars': tour_page.star,
        'country': tour_page.in_city,
        'departure': dep[departure],
        'nights': tour_page.nights,
        'url_image': tour_page.image,
        'description': tour_page.description,
        'price': tour_page.price,

    })
