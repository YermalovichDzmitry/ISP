from django.contrib import admin
from .models import Articles, Category, Author, Address


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ['title', "date", "cat"]
    list_editable = ['date', "cat"]


admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Address)
