from django.urls import path
from ebooks.api.views import EbookListCreateAPIViews

urlpatterns = [
    path('ListCreateAPI/', EbookListCreateAPIViews.as_view(), name='ListCreateAPI'),
]
