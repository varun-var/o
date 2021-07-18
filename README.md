# tuya-cloud-dimming-lights #

This project is developed using Tuya SDK, which enables you to quickly develop smart devices, branded APP, cloud development project, etc.

For more information, please check Tuya Developer Click and Connect Challenge https://pages.tuya.com/develop/ClickAndConnect_TuyaDeveloper?_source=e9684c7ca6b31e7221c8420f5af94631


---
## Installation
Install or upgrade tuya-bulb-control:
```
$ pip install tuya-bulb-control --upgrade
```
<br>

Demo code:
```Python
from tuya_bulb_control import Bulb

CLIENT_ID = ''
SECRET_KEY = ''
DEVICE_ID = ''
REGION_KEY = 'in'

lights = Bulb(
    client_id=CLIENT_ID,
    secret_key=SECRET_KEY,
    device_id=DEVICE_ID,
    region_key=REGION_KEY
)


# Turn on the dimming-lights
lights.turn_on()


# Turn off the dimming-lights
lights.turn_off()


# Toggle the dimming-lights
lights.set_toggle()


# Turn off the dimming-lights after 5 minutes
lights.set_toggle_timer(value=5)


#Other functions used
#depends on the bulb used
#check the bulb and its functions in api of the project
```
<br>


<h3>Functions:</h3>
Check the functions depending on the type of light you are using, incase of error use different version of the function <br>

Dimming lights: on, off, brightness, etc
<br>
<br>

<h3>Important:</h3>
client_id, client_key,device_id are required for the project to work.
<br>
<br>

## Procedure:
#### Step 1: CLIENT_ID and SECRET_KEY
- Register or Login on <a href="https://auth.tuya.com" target="_blanck">Tuya</a>.
1. Create a cloud development project <a href="https://iot.tuya.com/cloud" target="_blanck">Cloud -> Project</a>.
2. After successful creation, you will receive the **Client ID** and **Secret Key**.


#### Step 2: DEVICE_ID
1. Install **Tuya Smart** app or **Smart Life** app on your mobile phone.
2. Go to <a href="https://iot.tuya.com/cloud/appinfo/cappId/device" target="_blanck">Cloud -> Link Devices</a> page.
3. Selecting a tab **Link Devices by App Account**.
4. Click **Add App Account** and scan the QR code with **Tuya Smart** app or **Smart Life** app.
5. Now you can go to devices <a href="https://iot.tuya.com/cloud/appinfo/cappId/deviceList" target="_blanck">Cloud -> Device List</a> and copy **Device ID**.
    * Notes: Try to select a your region if devices are not displayed.


#### Step 3: Request access to API calls
Go to <a href="https://iot.tuya.com/cloud/appinfo/cappId/setting" target="_blanck">Cloud -> API Group</a> and enable **Authorization management**, **Device Management** and **Device Control**.
<br>
<br>
<h3>Note:</h3>
Install the requirements files libraies incase of errors, chaneg versions of function based on error and function used.
