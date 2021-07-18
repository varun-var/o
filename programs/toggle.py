from tuya_bulb_control import Bulb

CLIENT_ID = ''  #see the steps in readme to get the id
SECRET_KEY = '' #see the steps in readme to get the id
DEVICE_ID = ''  #see the steps in readme to get the id
REGION_KEY = '' #region from which bulb is being operated

bulb = Bulb(
    client_id=CLIENT_ID,
    secret_key=SECRET_KEY,
    device_id=DEVICE_ID,
    region_key=REGION_KEY
)


# Turn off the light bulb after 5 minutes
bulb.set_toggle()