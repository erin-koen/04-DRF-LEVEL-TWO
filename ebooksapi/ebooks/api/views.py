from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework import permissions

from ebooks.models import Ebook, Review
from ebooks.api.serializers import EbookSerializer, ReviewSerializer
from ebooks.api.permissions import IsAdminUserOrReadOnly


# with Concrete view classes, you get all of the commented out view in 3lines.
class EbookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    # object-level permissions
    permission_classes = [IsAdminUserOrReadOnly]


class EbookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # to connect to an ebook instance, we need to overwrite perform_create()

    def perform_create(self, serializer):
        ebook_pk = self.kwargs.get("ebook_pk")
        ebook = get_object_or_404(Ebook, pk=ebook_pk)
        # link occurs below
        serializer.save(ebook=ebook)


class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# in order to provide behavior functionalities to our classes, we need
# to pass in our mixins with the genericAPIView class
# class EbookListCreateAPIView(generics.GenericAPIView,
#                              mixins.CreateModelMixin,
#                              mixins.ListModelMixin):

#     queryset = Ebook.objects.all()
#     serializer_class = EbookSerializer

#     def get(self, request, *args, **kwargs):
#         # convention that we use to tell our functions that they might need
#         # to manage a variable number of arguments and kwargs without
#         # needing to know exactly what it's going to require
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
