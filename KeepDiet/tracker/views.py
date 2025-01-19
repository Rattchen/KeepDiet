import os
from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse, Http404
from django.views.generic import DetailView, TemplateView, View
from fatsecret import Fatsecret
from .models import DaySummary
from .dto import ProductDTO

FS_CONSUMER = str(os.getenv('FS_CONSUMER'))
FS_SECRET = str(os.getenv('FS_SECRET'))


class DayDetailView(DetailView):
    model = DaySummary
    template_name = 'tracker/index.html'
    context_object_name = 'day'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["meals"] = self.object.meals.all()
        return context

class SearchPageView(TemplateView):
    template_name = "tracker/search.html"

class SearchView(View):
    def get(self, request):
        query = request.GET.get('search', '')
        fs = Fatsecret(FS_CONSUMER, FS_SECRET)
        result = fs.foods_search(query)
        result_html = render_to_string('tracker/partials/search_results.html', {'results':result})
        print(result)
        return HttpResponse(result_html)

class ProductDetailView(DetailView):
    template_name = 'tracker/product_details.html'
    context_object_name = 'product'

    def get_object(self):
        product_id = self.kwargs["pk"]
        fs = Fatsecret(FS_CONSUMER, FS_SECRET)
        result = fs.food_get_v2(product_id)
        return ProductDTO.from_json(result)
