from django.contrib import admin
from .models import *


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(ReadBooks, ArticleAdmin)
admin.site.register(UnreadBooks, ArticleAdmin)
admin.site.register(Category, ArticleAdmin)
admin.site.register(Year)

