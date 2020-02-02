from rest_framework import serializers
from ebooks.models import Ebook, Review


# Models based Serializer class create
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class EbookSerializer(serializers.ModelSerializer):
    # Reletions Between Reviews and Ebook's
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Ebook
        fields = "__all__"
