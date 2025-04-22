from django.contrib import admin
from .models import ContentCategory, Photo, Video, Career

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'upload_date', 'category', 'featured')
    list_filter = ('category', 'featured', 'upload_date')
    search_fields = ('title', 'description')

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'upload_date', 'category', 'featured')
    list_filter = ('category', 'featured', 'upload_date')
    search_fields = ('title', 'description')

class CareerAdmin(admin.ModelAdmin):
    list_display = ('title', 'career_type', 'year', 'is_special')
    list_filter = ('career_type', 'year', 'is_special')
    search_fields = ('title', 'description')

admin.site.register(ContentCategory)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Career, CareerAdmin)
