from rest_framework import serializers

from page.models import Page


class PageSerializer(serializers.ModelSerializer):
    author_username=serializers.CharField(source='author.username',read_only=True)
    class Meta:
        model=Page
        fields=['id','subject','content','author_username']
        read_only_fields=['author']