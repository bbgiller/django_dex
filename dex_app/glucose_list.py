# from .settings import dexcom
import datetime

def get_glucose_array(dexcom_session):
    bg_list = dexcom_session.get_glucose_readings(minutes=1440)
    bg_values = [{"glucose_value": bg.value, "time": bg.time.isoformat()}
                  for bg in bg_list]
    return bg_values
