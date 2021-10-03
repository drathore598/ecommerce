from django.urls import path

from products.views import ProductListView, ProductDetailSlugView
from search.views import SearchProductView

urlpatterns = [
    path('', SearchProductView.as_view(), name='query'),
]
