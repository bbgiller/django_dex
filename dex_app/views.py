from django.http import JsonResponse
from .settings import dexcom
from .glucose_list import get_glucose_array

def home(request):
    return JsonResponse({'message': 'Welcome to sugars'})


def current_glucose(request):
    ng = dexcom.get_current_glucose_reading()
    if ng:
        response_body = {
            "glucose_value": ng.value,
            "mmol": ng.mmol_l,
            "time": ng.time,
            "trend": ng.trend,
            "trend_arrow": ng.trend_arrow,
            "trend_description": ng.trend_description,
        }
    else:
        response_body = {
            "glucose_value": 115,
            "mmol": 5.9,
            "time": "Wed, 15 Feb 2023 10:15:56 GMT",
            "trend": 4,
            "trend_arrow": "\u2192",
            "trend_description": "steady"
        }

    return JsonResponse(response_body)


def glucose_readings_list(request):
    bg_list = get_glucose_array()
    response_body = {
        "glucose_list": bg_list
    }
    return JsonResponse(response_body)

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from dex_app.models import User

@csrf_exempt
def get_user(request,id):
    try:
        user = User.objects.get(id= id) or User.objects.get(dexcom_id = id)
        return JsonResponse({
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'firebase_id': user.firebase_id,
            'dexcom_id': user.dexcom_id,
        })
    except User.DoesNotExist:
        # Return a 404 Not Found response if the user is not found
        return JsonResponse({}, status=404)




@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        # Parse the request body
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        firebase_id = request.POST.get('firebase_id')

        # Create a new User object
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            firebase_id=firebase_id,
        )

        # Return a JSON response with the new user's ID
        return JsonResponse({'id': user.id})
    else:
        # Return a 405 Method Not Allowed response for unsupported methods
        return JsonResponse({}, status=405)
