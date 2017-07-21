from django.contrib import admin
from .models import  Blog,Category,Day,Tag,Photo,PhotoItem

class PhotoInline(admin.TabularInline):
    model = Photo

class PhotoItemAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]

admin.site.register(PhotoItem, PhotoItemAdmin)    
admin.site.register(Photo)
admin.site.register([Category,Blog,Tag])
admin.site.register(Day)
