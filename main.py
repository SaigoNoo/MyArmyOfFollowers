import requests

key = "apiPerso"
channel = "UCTmzT0st55PREearcmcCnNQ"


def get_channel_stat() -> dict:
    url = f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={channel}&key={key}'
    jsonData = requests.get(url).json()
    return jsonData['items'][0]['statistics']

stats = get_channel_stat()
print(stats["subscriberCount"])
