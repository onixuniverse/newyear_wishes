from random import choice

from django.shortcuts import render

from wishes.models import Wishes


def index(request):
    wishes = choice(Wishes.objects.all())

    return render(request, 'wishes.html',
                  context={'random_wish': wishes})
