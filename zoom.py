import requests
import json
from base64 import b64encode
from http import HTTPStatus
from time import time
from datetime import datetime
import os

from dotenv import load_dotenv

load_dotenv()

account_id = os.getenv('ACCOUNT_ID')
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
HOSTS = os.getenv('HOSTS')

# create a function to generate a token
# using the pyjwt library

def generateToken():
    url = f"https://zoom.us/oauth/token?grant_type=account_credentials&account_id={account_id}"
    b64_client = f"{client_id}:{client_secret}".encode()
    b64_client = b64encode(b64_client).decode()
    headers = {"Authorization": f"Basic {b64_client}", }

    r = requests.post(url=url, headers=headers)
    if r.status_code == HTTPStatus.OK:
        return r.json()["access_token"]
    else:
        raise Exception("failed to generate token")
  
  
# create json data for post requests

meetingdetails = {"topic": "Engineering Meeting",
                  "type": 2,
                  "start_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                  "duration": "120",
                  "timezone": "US/Pacific",
                  "agenda": "",
  
                  "recurrence": {"type": 1,
                                 "repeat_interval": 1
                                 },
                  "settings": {"host_video": "false",
                               #"alternative_hosts": HOSTS,
                               "participant_video": "false",
                               "join_before_host": "false",
                               "mute_upon_entry": "true",
                               "waiting_room": "false",
                               "watermark": "true",
                               "audio": "voip",
                               "auto_recording": "none"
                               }
                  }
  
# send a request with headers including
# a token and meeting details
  
  
def createMeeting():
    headers = {'authorization': 'Bearer ' + generateToken(),
               'content-type': 'application/json'}
    r = requests.post(
        f'https://api.zoom.us/v2/users/me/meetings',
        headers=headers, data=json.dumps(meetingdetails))
  
    print("\n creating zoom meeting ... \n")
    # print(r.text)
    # converting the output into json and extracting the details
    y = json.loads(r.text)
    print(y)
    """
    join_URL = y["join_url"]
    meetingPassword = y["password"]
  
    print(
        f'\n here is your zoom meeting link {join_URL} and your \
        password: "{meetingPassword}"\n')
    """
  
  
# run the create meeting function
createMeeting()
