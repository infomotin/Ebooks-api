
#For Generic Class
from rest_framework import generics
from rest_framework import mixins
#for database Class import

from ebooks.models import Ebook,Review

#for impoting Serializer Class

from ebooks.api.serializers import EbookSerializer,ReviewSerializer