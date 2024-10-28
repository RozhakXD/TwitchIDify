import requests
import json
import re

def get_id_twitch(username: str) -> dict:
    with requests.Session() as session:
        session.headers.update(
            {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'en-US,en;q=0.9',
                'Host': 'www.twitch.tv',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Site': 'none',
                'Sec-Fetch-User': '?1',
                'Sec-Fetch-Mode': 'navigate',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
            }
        )
        response = session.get(f'https://www.twitch.tv/{username}', allow_redirects=True, verify=True)

        clientId = re.search(r'clientId="(\w+)"', response.text).group(1)

        data = [
            {
                "operationName": "ChannelAvatar",
                "variables": {
                    "channelLogin": f"{username}",
                    "includeIsDJ": True
                },
                "extensions": {
                    "persistedQuery": {
                        "version": 0,
                        "sha256Hash": "12575ab92ea9444d8bade6de529b288a05073617f319c87078b3a89e74cd783a"
                    }
                }
            }
        ]
        session.headers.update(
            {
                'Content-Length': f'{len(str(data))}',
                'Accept-Language': 'en-US',
                'Accept': '*/*',
                'Sec-Fetch-Dest': 'empty',
                'Host': 'gql.twitch.tv',
                'Sec-Fetch-Site': 'same-site',
                'Sec-Fetch-Mode': 'cors',
                'Client-Id': f'{clientId}',
                'Content-Type': 'application/json',
            }
        )
        response2 = session.post('https://gql.twitch.tv/gql', data=json.dumps(data), verify=True)
        if '"id":' in response2.text:
            response2_json = json.loads(response2.text)[0]
            followers = response2_json['data']['user']['followers']['totalCount']
            user_id = response2_json['data']['user']['id']
            return (
                {
                    "user": {
                        "id": user_id,
                        "followers": followers
                    }
                }
            )
        else:
            return (
                {
                    "error": "Pengguna tidak ditemukan!"
                }
            )