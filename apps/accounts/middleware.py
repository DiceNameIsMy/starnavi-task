from django.contrib.auth import get_user_model
from django.utils.timezone import datetime, make_aware

# Probably would be better to use some 
# kind of caching instead of always calling db
class WriteUserActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user and request.user.is_authenticated:
            print(request.user.last_active)
            request.user.last_active = make_aware(datetime.now())
            request.user.save()
            print(request.user.last_active)

        
        response = self.get_response(request)
        return response