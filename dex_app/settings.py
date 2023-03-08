from pydexcom import Dexcom
# DEXCOM_USERNAME = "bbgiller1"
# DEXCOM_PASSWORD = "Xcommyy1"


def create_dexcom_session(user):
    dexcom = Dexcom(user.dexcom_username, user.dexcom_password)
    dexcom.create_session()
    return dexcom


# dexcom = Dexcom(DEXCOM_USERNAME, DEXCOM_PASSWORD)
