from django.http import HttpResponse

class CustomApiMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith("/api/") and not request.user.is_authenticated:
            return HttpResponse("You are not a logged-in user. Please log in first.")
        response = self.get_response(request)
        return response
    
