from django.contrib import admin

# Register your models here.
from page.models import Page


# Register your models here.
@admin.register(Page)
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','subject','content','author']
    list_filter=['author','subject','content']
    search_fields=['subject','content']
#    autocomplete_fields=['subject']
    list_editable=['content']
    list_per_page=20
    ordering=['subject']
