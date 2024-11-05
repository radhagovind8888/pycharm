from django.contrib import admin
from MyApps1.models import Company
# Register your models here.
class Companyadmin(admin.ModelAdmin):
    list_display=['name','location','ceo'];
admin.site.register(Company,Companyadmin)