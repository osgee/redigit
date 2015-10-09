from django.conf import settings
import re
import mdetect

class MobileDetectionMiddleware(object):
    """
    Useful middleware to detect if the user is
    on a mobile device.
    """
    def process_request(self, request):
        is_mobile = False
        is_tablet = False
        is_phone = False

        user_agent = request.META.get("HTTP_USER_AGENT")
        http_accept = request.META.get("HTTP_ACCEPT")
        if user_agent and http_accept:
            agent = mdetect.UAgentInfo(userAgent=user_agent, httpAccept=http_accept)
            is_tablet = agent.detectTierTablet()
            is_phone = agent.detectTierIphone()
            is_mobile = is_tablet or is_phone or agent.detectMobileQuick()

        request.is_mobile = is_mobile
        request.is_tablet = is_tablet
        request.is_phone = is_phone
        
        
class MobileTemplatesMiddleware(object):
    """Determines which set of templates to use for a mobile site"""

    ORIG_TEMPLATE_DIRS = settings.TEMPLATE_DIRS

    def process_request(self, request):
        # sets are used here, you can use other logic if you have an older version of Python
        MOBILE_SUBDOMAINS = set(['m', 'mobile'])
        domain = set(request.META.get('HTTP_HOST', '').split('.'))

        if request.is_mobile:
            settings.TEMPLATE_DIRS = settings.MOBILE_TEMPLATE_DIRS + self.ORIG_TEMPLATE_DIRS
        else:
            settings.TEMPLATE_DIRS = settings.DESKTOP_TEMPLATE_DIRS + self.ORIG_TEMPLATE_DIRS