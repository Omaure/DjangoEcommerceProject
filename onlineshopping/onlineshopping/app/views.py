from __future__ import unicode_literals

from django.views.generic import DetailView, TemplateView
from .models import Foo
from myshopping.models import Product


class FooView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        obj, created = self.model.objects.get_or_create(product_id='1')
        return obj


class SizesView(TemplateView):
    model = Foo
    template_name = 'sizes.html'

    def get_context_data(self, **kwargs):
        kwargs['sizes'] = {size: self.model.objects.get_or_create(bar=str(size))[0] for size in range(10, 40)}
        return super(SizesView, self).get_context_data(**kwargs)
