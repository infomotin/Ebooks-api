# For Generic Class
from rest_framework import generics
from rest_framework import mixins
# for database Class import

from ebooks.models import Ebook, Review

# for importing Serializer Class

from ebooks.api.serializers import EbookSerializer, ReviewSerializer


# Create API  Views as Like APIView

class EbookListCreateAPIViews(mixins.ListModelMixin,
                              mixins.CreateModelMixin,
                              generics.GenericAPIView):
    # queryset are Has Namings Conventions
    queryset = Ebook.objects.all()
    # serializer_class has Naming Conventions
    serializer_class = EbookSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# create Concrete views class
class EbookGenericListCreateAPIViews(generics.ListCreateAPIView):
    # queryset are Has Namings Conventions
    queryset = Ebook.objects.all()
    # serializer_class has Naming Conventions
    serializer_class = EbookSerializer


# create Concrete views class with Crud
class EbookDetailGenericListCreateAPIViews(generics.RetrieveDestroyAPIView):
    # queryset are Has Namings Conventions
    queryset = Ebook.objects.all()
    # serializer_class has Naming Conventions
    serializer_class = EbookSerializer


class ReviewDetailAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    # serializer_class has Naming Conventions
    serializer_class = ReviewSerializer
