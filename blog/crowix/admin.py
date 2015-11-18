from django.contrib import admin
from .models import artical

class articalAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'tag','slug')

# Register your models here.
admin.site.register(artical, articalAdmin)