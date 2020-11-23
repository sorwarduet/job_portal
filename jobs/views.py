from django.shortcuts import render

from .models import Job, Category
from django.views.generic import TemplateView, ListView
# Create your views here.


class HomeView(ListView):
    template_name = "index.html"
    model= Job
    context_object_name= 'jobs'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()

        return context

