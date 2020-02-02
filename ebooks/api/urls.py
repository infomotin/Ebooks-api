from django.urls import path
from ebooks.api.views import (EbookListCreateAPIViews,
                              EbookGenericListCreateAPIViews,
                              EbookDetailGenericListCreateAPIViews)

urlpatterns = [
    path('ListCreateAPI/', EbookListCreateAPIViews.as_view(), name='ListCreateAPI'),
    #for EbookGenericListCreateAPIViews
    path('EbookGenericListCreateAPIViews/', EbookGenericListCreateAPIViews.as_view(), name='EbookGenericListCreateAPIViews'),
    #for EbookDetailGenericListCreateAPIViews
    path('EbookDetailGenericListCreateAPIViews/', EbookDetailGenericListCreateAPIViews.as_view(), name='EbookDetailGenericListCreateAPIViews'),

]
