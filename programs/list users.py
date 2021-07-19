import logging
from tuya_iot import TuyaOpenAPI, tuya_logger

from env import *

tuya_logger.setLevel(logging.DEBUG)
openapi = TuyaOpenAPI(ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.login(USERNAME, PASSWORD)

# Get asset list of the user
openapi.get('/v1.0/iot-03/users/assets', {
  'parent_asset_id': '',
  'page_no': 0,
  'page_size': 100,
})
