from django.contrib import admin
from .models import Reserve

# Register your models here.
class reserveAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'date', 'time', 'level')
   
admin.site.register(Reserve, reserveAdmin)