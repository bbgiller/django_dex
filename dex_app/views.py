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
