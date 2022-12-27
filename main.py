import pandas as pd
import requests

key = "TYPE YOUR TOKEN HERE AND ENABLE YouTube API V3"
channel = "UCTmzT0st55PREearcmcCnNQ"


def get_channel_stat() -> dict:
    url = f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={channel}&key={key}'
    print(url)

    r = requests.get(url)
    data = r.json()
    return data['items'][0]['statistics']


stats = get_channel_stat()
pd.DataFrame([stats])
