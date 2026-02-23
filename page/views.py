from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from page.models import Page
from page.serializers import PageSerializer


# Create your views here.
class PageViewSet(viewsets.ModelViewSet):
    ##queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):

        return Page.objects.filter(author=self.request.user)
""""""