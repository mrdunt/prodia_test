from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def thumbnail_generator(image: str = "", size: str = "", page: str = "") -> str:
    key_prefix = "size_"
    try:
        if image:
            if size == key_prefix + '120x120':
                image = image.thumbnails.size_120x120.url
            elif size == key_prefix + '375x270':
                image = image.thumbnails.size_375x270.url
            elif size == key_prefix + '500x500':
                image = image.thumbnails.size_500x500.url
            elif size == 'original':
                image = image.url
        else:
            if page == 'profile':
                image = f'{settings.STATIC_URL}assets/images/dummy-avatar.jpg'
            else:
                image = f'{settings.STATIC_URL}assets/images/logo/logo.png'
    except (AttributeError, OSError, ValueError):
        if page == 'profile':
            image = f'{settings.STATIC_URL}assets/images/dummy-avatar.jpg'
        else:
            image = f'{settings.STATIC_URL}assets/images/logo/logo.png'
    return image
