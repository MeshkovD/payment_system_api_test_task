from django.contrib import admin

from cartapp.models import Item


class ImpressionAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'price']


admin.site.register(Item, ImpressionAdmin)