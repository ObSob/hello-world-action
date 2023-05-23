# %%
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import requests

url = "https://www.strava.com/athlete/training_activities?keywords=&activity_type=&workout_type=&commute=&private_activities=&trainer=&gear=&search_session_id=8d37d30f-b8e6-4438-af98-35fc247c697b&new_activity_only=false"
cookie = "xp_session_identifier=3c6885111f8808bba1bcb069f7dd7752; sp=cb45f1da-9169-4947-967d-9a6811f0ac04; _strava_cbv3=true; _gcl_au=1.1.29122092.1684742252; _gid=GA1.2.614165531.1684742252; explore_activity_type=Ride; _sp_ses.047d=*; strava_wv2_fonts_loaded=1; sid-verificationId=646c727d234d5a23ab0c9886; _strava4_session=9j8j3l8hid06pabq6p5hlvc4n8got1gi; strava_remember_id=102218532; strava_remember_token=eyJzaWduaW5nX2tleSI6InYxIiwiZW5jcnlwdGlvbl9rZXkiOiJ2MSIsIml2Ijoiak12b0xPMTBGeS8xWWtLUEVSY25mQT09XG4iLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjb20uc3RyYXZhLmF0aGxldGVzIiwic3ViIjoxMDIyMTg1MzIsImlhdCI6MTY4NDgyOTAxNSwiZXhwIjoxNjg3NDIxMDE1LCJlbWFpbCI6ImhwUGNPVTgyVk5RMi9BVHE5RXpJMzFjU09mbDZwR2hyZllrOVhpRFJaOC9xK1VIZUFISnRwbFVXVUdwRlxucmpSRnBFMFUzSC9vdit6WVRkQXdCcUdkS0E9PVxuIn0.d-18xA-_h_3J1nKlQIxd1Swu4exdEsvjvHqFWVOJ7v4; _dc_gtm_UA-6309847-24=1; _ga=GA1.1.36167699.1684742252; _ga_ESZ0QKJW56=GS1.1.1684826169.6.1.1684829559.60.0.0; _sp_id.047d=587d28e1-dfe8-42ee-b05d-8c784ca5d86c.1684829018.7.1684829561..01b54973-bb82-4087-88a9-74970a406a5b"

headers = {
    'path' : '/athlete/training_activities?keywords=&activity_type=&workout_type=&commute=&private_activities=&trainer=&gear=&search_session_id=8d37d30f-b8e6-4438-af98-',
    'cookie' : cookie,
    'X-Requested-With' : 'XMLHttpRequest'
}

req = requests.request('GET', url=url, headers=headers)

# %%
traces_need_upload = [
    {
        'id': 130820975,
        'title': '2023-05-20 上午 骑行',
    }
]
url_gpx = "https://www.imxingzhe.com/xing/{}/gpx/".format(traces_need_upload[0]['id'])
resp_gpx = requests.request('GET', url=url_gpx, headers={
    'cookie' : "Hm_lvt_7b262f3838ed313bc65b9ec6316c79c4=1684148879; rd=Z8fo; csrftoken=Axm0qgLHkJzDdTYV02i4x9nfOqA0Hozn; sessionid=m4qcgavk9ly4zenslby1zcorot4j9cp9; Hm_lpvt_7b262f3838ed313bc65b9ec6316c79c4=1684746367",

})
# %%
import io

resp_upload = requests.request('POST', url='https://www.strava.com/upload/files',
    headers={
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'Referer' : 'https://www.strava.com/upload/select',
        'path' : '/upload/files',
        'cookie' : cookie,
    'X-Requested-With' : 'XMLHttpRequest'
    },
    files={
        'file' : ('行者记录.gpx', io.BytesIO(resp_gpx.content), 'application/gpx+xml'),
    }
)
print(resp_upload.text)
# %%
## 限制太严格辣
## 试了很多参数，都没办法传
## 以后有空再试试stravalib好了