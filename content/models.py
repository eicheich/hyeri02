from django.db import models
from django.utils import timezone

# Create your models here.
class ContentCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Content Categories"

class Photo(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='photos/')
    upload_date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(ContentCategory, on_delete=models.SET_NULL, blank=True, null=True, related_name='photos')
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title if self.title else f"Photo {self.id}"

class Video(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    video_file = models.FileField(upload_to='videos/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to='video_thumbnails/', blank=True, null=True)
    upload_date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(ContentCategory, on_delete=models.SET_NULL, blank=True, null=True, related_name='videos')
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title if self.title else f"Video {self.id}"

    def has_video(self):
        return bool(self.video_file or self.video_url)

class Career(models.Model):
    CAREER_TYPES = (
        ('film', 'Film'),
        ('drama', 'Drama'),
        ('variety', 'Variety Show'),
        ('music', 'Music'),
        ('victory', 'Victory/Award'),
        ('other', 'Other'),
    )

    title = models.CharField(max_length=200)
    career_type = models.CharField(max_length=20, choices=CAREER_TYPES)
    year = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_special = models.BooleanField(default=False)
    image = models.ImageField(upload_to='career/', blank=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.get_career_type_display()})"

    class Meta:
        verbose_name_plural = "Career Entries"
        ordering = ['-year', 'title']
