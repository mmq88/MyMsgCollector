import requests

from local.logger import APP_LOGGER

def fetch_discord_messages(user_token: str, channel_id: str, limit: int, tag: str) -> str:
    '''Fetch messages from a Discord channel'''

    try:
        headers = {
            'Authorization': user_token,
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
        }

        url = f'https://discord.com/api/v9/channels/{channel_id}/messages?limit={limit}'

        response = requests.get(url, headers=headers)
        msg = None

        if response.status_code == 200:
            data = response.json()
            msg = f"FROM [{tag}]: {data[0]['content']}"
            APP_LOGGER.info(f"Fetch from [{tag}] successfully: {data[0]['content']}")
        else:
            msg = f"FROM [{tag}]: Error: {response.text}"
            APP_LOGGER.info(f"Fetch from [{tag}] successfully: {data[0]['content']}")
        
        return msg
    except Exception as e:
        APP_LOGGER.error(f"Fetch from [{tag}] failed with exception: {e}")
        return f"FROM [{tag}]: Exception: {e}"

def send_by_webhook(url: str, content: str) -> None:
    '''Send message by webhook'''
    data = {
        'content': content
    }

    response = requests.post(url, json=data)

    if response.status_code == 204:
        APP_LOGGER.info(f"Message sent: {content}")
    else:
        APP_LOGGER.error(f"{response.text}")
