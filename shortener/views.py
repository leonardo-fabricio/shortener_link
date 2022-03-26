from django.conf import settings
from django.shortcuts import redirect, render

# Create your views here.
def return_for_domain(request):
    return redirect(settings.RETURN_URL)