from django.contrib import admin

from .models import NewsModel,CategoryModel,ContactModel

admin.site.register(NewsModel)
admin.site.register(CategoryModel)
admin.site.register(ContactModel)