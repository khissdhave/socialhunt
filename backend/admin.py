from django.contrib import admin
from .models import SearchRecord

# Register your models here.

@admin.register(SearchRecord)
class SearchLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'username', 'search_time')

