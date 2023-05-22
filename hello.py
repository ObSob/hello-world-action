# %%
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import requests

url = "http://www.imxingzhe.com/api/v4/user_month_info/?user_id=2321482&year=2023&month=5"
cookie = "Hm_lvt_7b262f3838ed313bc65b9ec6316c79c4=1684148879; rd=Z8fo; csrftoken=Axm0qgLHkJzDdTYV02i4x9nfOqA0Hozn; sessionid=m4qcgavk9ly4zenslby1zcorot4j9cp9; Hm_lpvt_7b262f3838ed313bc65b9ec6316c79c4=1684746367"

headers = {
    'cookie' : cookie,
}

req = requests.request('GET', url=url, headers=headers)
traces = req.json()['data']['wo_info']

# %%
tz=ZoneInfo("Asia/Shanghai")
upper = datetime.now(tz=tz).replace(minute=0, second=0, microsecond=0)
lower = upper - timedelta(hours=1)
print(lower, upper)

traces_need_upload = []

# for t in traces:
#     time = datetime.fromisoformat(t['upload_time']).replace(tzinfo=tz)
#     if lower <= time < lower:
#         record = {
#             'id' : t['id'],
#             'title' : t['title']
#         }
#         traces_need_upload.append(record)

print(traces_need_upload)

# %%
traces_need_upload = [
    {
        'id': 130931351,
        'title': '2023-05-20 上午 骑行',
    }
]
url_gpx = "https://www.imxingzhe.com/xing/{}/gpx/".format(traces_need_upload[0]['id'])
resp_gpx = requests.request('GET', url=url_gpx, headers=headers)

# %%
