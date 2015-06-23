#-*- coding:utf-8 -*-

from django.http import Http404
from django.shortcuts import redirect, get_object_or_404, render

from banner_rotator.models import Banner, Place


def click(request, banner_id):
    banner = get_object_or_404(Banner, pk=banner_id)
    banner.click(request)

    return redirect(banner.url)

def banner_per_place(request, place_slug):
    place = get_object_or_404(Place, slug=place_slug)

    try:
        banner_obj = Banner.objects.biased_choice(place)
        banner_obj.view()
    except Banner.DoesNotExist:
        raise Http404

    print banner_obj, type(banner_obj), place
    ctx = {
        'banner': banner_obj,
        'banner_place': place,
    }
    return render(request, 'banner_rotator/place.html', ctx)
