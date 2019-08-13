from django.contrib import admin

# Register your models here.
from .models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "by", "points", "comments", "sentiment",)

admin.site.register(News, NewsAdmin)