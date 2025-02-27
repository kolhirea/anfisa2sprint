from django.shortcuts import render

from ice_cream.models import IceCream, Category


def index(request):
    template = 'homepage/index.html'
    ice_cream_list = IceCream.objects.values(
       'id', 'title', 'description').filter(is_on_main=True)
    context = {
        'ice_cream_list': ice_cream_list,
        }
    return render(request, template, context)
