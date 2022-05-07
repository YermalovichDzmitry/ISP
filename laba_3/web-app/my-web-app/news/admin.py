from django.contrib import admin
from .models import Articles, Category, Author, Address

admin.site.register(Articles)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Address)
