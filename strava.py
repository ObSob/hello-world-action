# %%
from stravalib import Client

MY_STRAVA_CLIENT_ID = "1762629204@qq.com"
MY_STRAVA_CLIENT_SECRET = "wbh673406316"
code = "114514"

client = Client()
token_response = client.exchange_code_for_token(client_id=MY_STRAVA_CLIENT_ID,
                                              client_secret=MY_STRAVA_CLIENT_SECRET,
                                              code=code)
