from django.shortcuts import render
from django.http import JsonResponse
import datetime

# Create your views here.

def ping_view(request):
    """Return a simple JSON response with status and UTC timestamp."""
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    return JsonResponse({'status': 'OK', 'time': now})
