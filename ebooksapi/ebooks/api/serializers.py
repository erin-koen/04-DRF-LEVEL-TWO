from rest_framework import serializers
from ebooks.models import Ebook, Review


class ReviewSerializer(serializers.ModelSerializer):
    # binding the review_author that's passed to the serializer to the
    # review record that will be created
    review_author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        # need to exclude this for creation process...why?

        exclude = ("ebook",)
        # fields = "__all__"


class EbookSerializer(serializers.ModelSerializer):
    # make relationships between the two models explicit
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Ebook
        fields = "__all__"
