from rest_framework.exceptions import ValidationError
from urllib.parse import urlparse

def validate_youtube_link(value):
    parsed_url = urlparse(value)
    if parsed_url.netloc != 'www.youtube.com' and parsed_url.netloc != 'youtube.com':
        raise ValidationError("Ссылка должна указывать только на видео YouTube.")
