import asyncio
import time
from telethon import TelegramClient
import json
from telethon.tl.types import InputPeerUser

with open('data.json') as f:
    data = json.load(f)

# api_id =
# api_hash = ''
# phone = ''
# name = ''
# limit =
# channel = ''
# all_participants = []
# message = "hello"


# receiver = 837259163
async def main():
    started = await TelegramClient(name, api_id, api_hash).start()

    if not isinstance(started, TelegramClient):
        raise ValueError(f"Unexpected client: {started}")

    async with started as client:
        for USERS in data:
            receiver = InputPeerUser(USERS['userID'], USERS['accessHash'])
            print("start send")
            try:
                await client.send_message(receiver, message="hello")
                print("send")
                time.sleep(15)
            except:
                pass
asyncio.run(main())
