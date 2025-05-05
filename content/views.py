from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Photo, Video, ContentCategory, Career
import random

def index(request):
    """Home page with featured content"""
    # Get all photos to display on the landing page
    all_photos = Photo.objects.all().order_by('-upload_date')

    # No need for random selection if we want to show all photos
    # But ensure we have photos before proceeding
    if all_photos.exists():
        random_photos = all_photos
    else:
        random_photos = []

    # Still keeping featured content for other parts of the page
    featured_photos = Photo.objects.filter(featured=True).order_by('-upload_date')[:6]
    featured_videos = Video.objects.filter(featured=True).order_by('-upload_date')[:3]
    categories = ContentCategory.objects.all()

    context = {
        'featured_photos': featured_photos,
        'featured_videos': featured_videos,
        'categories': categories,
        'random_photos': random_photos,
    }

    return render(request, 'content/index.html', context)

def photo_gallery(request):
    """Photo gallery page with pagination"""
    category_id = request.GET.get('category')

    if category_id:
        photos = Photo.objects.filter(category_id=category_id).order_by('-upload_date')
        current_category = get_object_or_404(ContentCategory, id=category_id)
    else:
        photos = Photo.objects.all().order_by('-upload_date')
        current_category = None

    categories = ContentCategory.objects.all()
    paginator = Paginator(photos, 12)  # Show 12 photos per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'categories': categories,
        'current_category': current_category,
    }

    return render(request, 'content/photo_gallery.html', context)

def photo_detail(request, photo_id):
    """Detail view for a single photo"""
    photo = get_object_or_404(Photo, id=photo_id)
    related_photos = Photo.objects.filter(category=photo.category).exclude(id=photo.id).order_by('-upload_date')[:4]

    context = {
        'photo': photo,
        'related_photos': related_photos,
    }

    return render(request, 'content/photo_detail.html', context)

def video_gallery(request):
    """Video gallery page with pagination"""
    category_id = request.GET.get('category')

    if category_id:
        videos = Video.objects.filter(category_id=category_id).order_by('-upload_date')
        current_category = get_object_or_404(ContentCategory, id=category_id)
    else:
        videos = Video.objects.all().order_by('-upload_date')
        current_category = None

    categories = ContentCategory.objects.all()
    paginator = Paginator(videos, 9)  # Show 9 videos per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'categories': categories,
        'current_category': current_category,
    }

    return render(request, 'content/video_gallery.html', context)

def video_detail(request, video_id):
    """Detail view for a single video"""
    video = get_object_or_404(Video, id=video_id)
    related_videos = Video.objects.filter(category=video.category).exclude(id=video.id).order_by('-upload_date')[:3]

    context = {
        'video': video,
        'related_videos': related_videos,
    }

    return render(request, 'content/video_detail.html', context)

def about(request):
    """About Lee Hyeri page"""
    return render(request, 'content/about.html')

def career(request):
    """Career page with filmography and victories"""
    dramas = Career.objects.filter(career_type='drama').order_by('-year')
    films = Career.objects.filter(career_type='film').order_by('-year')
    variety_shows = Career.objects.filter(career_type='variety').order_by('-year')
    victories = Career.objects.filter(career_type='victory').order_by('-year')
    music = Career.objects.filter(career_type='music').order_by('-year')

    # Get special Friendly Rivalry entry
    friendly_rivalry = Career.objects.filter(title__icontains='Friendly Rivalry', is_special=True).first()

    context = {
        'dramas': dramas,
        'films': films,
        'variety_shows': variety_shows,
        'victories': victories,
        'music': music,
        'friendly_rivalry': friendly_rivalry,
    }

    return render(request, 'content/career.html', context)
