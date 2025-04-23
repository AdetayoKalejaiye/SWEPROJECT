from datetime import date, timedelta
from django.utils.deprecation import MiddlewareMixin
from .models import Profile

class UpdateStreakMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            profile, _ = Profile.objects.get_or_create(user=request.user)
            today = date.today()

            if profile.last_login_date != today:
                if profile.last_login_date == today - timedelta(days=1):
                    profile.streak += 1
                else:
                    profile.streak = 1

                profile.points += 5
                profile.last_login_date = today
                profile.save()

        return self.get_response(request)
