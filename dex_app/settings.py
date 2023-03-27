from pydexcom import Dexcom



def create_dexcom_session(user):
    dexcom = Dexcom(user.dexcom_username, user.dexcom_password)
    dexcom.create_session()
    return dexcom


# dexcom = Dexcom(DEXCOM_USERNAME, DEXCOM_PASSWORD)
