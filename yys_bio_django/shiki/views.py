from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.db.models import Q

from .models import Role, Lane, Shiki


class IndexView(generic.ListView):
    template_name = "shiki/index.html"
    context_object_name = "most_favorite_shiki"

    def get_queryset(self):
        return Shiki.objects.all().order_by("-fav_point")


class DetailView(generic.DetailView):
    model = Shiki
    template_name = "shiki/detail.html"


def search(request):
    template = "shiki/index.html"

    query = request.GET.get('q')

    result = Shiki.objects.filter(Q(name__icontains=query))
    context = {'shikis': result}
    return render(request, template, context)
