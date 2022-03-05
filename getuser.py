import asyncio
from telethon import TelegramClient

# Use your own values from my.telegram.org
api_id = 16692973
api_hash = "4688ac1027344e3d78b3bddf1ce739e8"
phone = +212666453758
name="Isma Isma"

async def main():
    # The first parameter is the .session file name (absolute paths allowed)
    started = TelegramClient(name, api_id, api_hash).start()

    if not isinstance(started, TelegramClient):
        raise ValueError(f"Unexpected client: {started}")

    async with started as client:
        # Getting information about yourself
        me = await client.get_me()

        # "me" is a user object. You can pretty-print
        # any Telegram object with the "stringify" method:
        print(me.stringify())

        # When you print something, you see a representation of it.
        # You can access all attributes of Telegram objects with
        # the dot operator. For example, to get the username:
        username = me.username
        print(username)
        print(me.phone)
asyncio.run(main())