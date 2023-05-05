from django.contrib import admin
from mainapp.models import rate

class rate_admin(admin.ModelAdmin):
    list_display=['name','quantity','taste','color','price']
admin.site.register(rate,rate_admin)

