from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext as _, activate, get_language
from django.conf import settings
import json


def home(request):
    """Main homepage view with professional Egyptian-friendly content"""
    from django.utils import translation
    
    # Get language from session and activate it
    session_lang = request.session.get('django_language', 'en')
    translation.activate(session_lang)
    
    
    context = {
        'current_time': timezone.now(),
        'page_title': _('Accurra - We Build Apps That Don\'t Just Work... They Flex'),
        'site_name': _('Accurra'),
        'current_language': session_lang,
        'is_arabic': session_lang == 'ar',
    }
    return render(request, 'main/home.html', context)


@csrf_exempt
def contact(request):
    """Handle contact form submissions"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name', '')
            email = data.get('email', '')
            message = data.get('message', '')
            
            # Send email (in production, use proper email backend)
            send_mail(
                f'New Contact from {name}',
                f'Name: {name}\nEmail: {email}\nMessage: {message}',
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )
            
            return JsonResponse({'status': 'success', 'message': 'Message sent successfully!'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    return render(request, 'main/contact.html')


def set_language(request, language):
    """Switch language view"""
    if language in ['en', 'ar']:
        # Set the language in the session first
        request.session['django_language'] = language
        request.session.save()  # Force save the session
        
        # Activate the language for this request
        from django.utils.translation import activate
        activate(language)
        
        
        # Redirect to the same page
        next_url = request.META.get('HTTP_REFERER', '/')
        return redirect(next_url)
    
    return redirect('/')


