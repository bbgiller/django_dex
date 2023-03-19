from django.http import JsonResponse
from .settings import create_dexcom_session
from .glucose_list import get_glucose_array
from django.shortcuts import get_object_or_404
from django.core import serializers
from pydexcom import Dexcom
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from dex_app.models import User, Insulin
from django.core.cache import cache


dexcom_sessions = {}  # a dictionary to store Dexcom sessions by user id


def home(request):
    return JsonResponse({'message': 'Welcome to sugars'})
#Glucose

def current_glucose(request):
    id = request.GET.get('id')
    user = get_object_or_404(User, id=id)
   
    if user.id in dexcom_sessions:
        dexcom = dexcom_sessions[user.id]
    else:
        dexcom = create_dexcom_session(user)
        dexcom_sessions[user.id] = dexcom

    # make the current glucose request using the Dexcom session
    cg = dexcom.get_current_glucose_reading()
    if cg:
        response_body = {
            "glucose_value": cg.value,
            "mmol": cg.mmol_l,
            "time": cg.time.isoformat(),
            "trend": cg.trend,
            "trend_arrow": cg.trend_arrow,
            "trend_description": cg.trend_description,
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
    id = request.GET.get('id')
    user = get_object_or_404(User, id=id)
    if user.id in dexcom_sessions:
        dexcom = dexcom_sessions[user.id]
    else:
        dexcom = create_dexcom_session(user)
        dexcom_sessions[user.id] = dexcom

    bg_list = get_glucose_array(dexcom_session=dexcom)
    response_body = {
        "glucose_list": bg_list
    }
    return JsonResponse(response_body)


@csrf_exempt

#Users
def get_user(request,id):
  
    user = get_object_or_404(User, id=id)
    user_data = serializers.serialize('json', [user])
    user = get_object_or_404(User, id=id)
    user_data = serializers.serialize('json', [user])
    return JsonResponse(user_data, safe=False)



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


@csrf_exempt
def create_insulin(request):
    if request.method == 'POST':
        # Parse the request body
        user_id = request.POST.get('user_id')
        dose = request.POST.get('dose')
        time = request.POST.get('time')
        type = request.POST.get('type')

        user = get_object_or_404(User, id=user_id)

        # Create a new Insulin object
        insulin = Insulin.objects.create(
            user=user,
            dose=dose,
            time=time,
            type=type
        )

        # Return a JSON response with the new insulin object's ID
        return JsonResponse({'id': insulin.id})
    else:
        # Return a 405 Method Not Allowed response for unsupported methods
        return JsonResponse({}, status=405)
