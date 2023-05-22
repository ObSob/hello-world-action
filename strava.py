# %%
from stravalib import Client

MY_STRAVA_CLIENT_ID = "1762629204@qq.com"
MY_STRAVA_CLIENT_SECRET = "wbh673406316"
code = "114514"

client = Client()
token_response = client.exchange_code_for_token(client_id=MY_STRAVA_CLIENT_ID,
                                              client_secret=MY_STRAVA_CLIENT_SECRET,
                                              code=code)
# %%
from stravalib.client import Client

client = Client()
authorize_url = client.authorization_url(client_id=1234, redirect_uri='http://localhost:8282/authorized')
# %%
code = requests.get('code') # or whatever your framework does
token_response = client.exchange_code_for_token(client_id=1234, client_secret='asdf1234', code=code)
# %%
