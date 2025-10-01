from django.utils import timezone
from django.conf import settings
import pytz


def egypt_time(request):
    """Add Egyptian time to context"""
    egypt_tz = pytz.timezone('Africa/Cairo')
    egypt_time = timezone.now().astimezone(egypt_tz)
    
    return {
        'egypt_time': egypt_time,
        'egypt_time_formatted': egypt_time.strftime('%Y-%m-%d %H:%M:%S'),
        'egypt_date': egypt_time.strftime('%A, %B %d, %Y'),
    }


def language_context(request):
    """Add language and professional Egyptian-friendly context"""
    from django.utils import translation
    
    # Get language from session
    session_lang = request.session.get('django_language', 'en')
    translation.activate(session_lang)
    
    current_lang = translation.get_language()
    is_arabic = current_lang == 'ar'
    
    return {
        'current_language': current_lang,
        'is_arabic': is_arabic,
        'site_name': 'Accurra',
        'tagline_en': 'We build apps that don\'t just work... they flex',
        'tagline_ar': 'بنبني تطبيقات مش بس تشتغل... بتفليكس',
    }
