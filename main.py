import asyncio

from local.data import DataManager
from local.logger import APP_LOGGER

from task.task import fetch_discord_messages, send_by_webhook

DATA_MANAGER = DataManager()
LATEST_MESSAGE = None

async def do_task(interval: int) -> None:
    global LATEST_MESSAGE
    while True:
        msg = fetch_discord_messages(
            DATA_MANAGER.data["DC"]["USER_TOKEN_MMQ"], 
            DATA_MANAGER.data["DC"]["TRACK_CHANNEL_ID_SHDW"], 
            1, 
            "SHDW"
        )

        if msg != LATEST_MESSAGE:
            send_by_webhook(DATA_MANAGER.data["OUTPUT"]["WEBHOOK_URL"], msg)
            LATEST_MESSAGE = msg
        await asyncio.sleep(interval)

def main():
    APP_LOGGER.info("Initialized successfully...")
    APP_LOGGER.info("Starting task...")
    try:
        asyncio.run(do_task(DATA_MANAGER.data["APP"]["TASK_INTERVAL"]))
    except KeyboardInterrupt:
        APP_LOGGER.info("Exited by user.")
        exit(0)
    except Exception as e:
        APP_LOGGER.error(f"Exception: {e}")
        exit(1)

if __name__ == '__main__':
    main()