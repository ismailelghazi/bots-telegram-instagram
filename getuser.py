import asyncio
from telethon import TelegramClient
from telethon import functions, types
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch


my_filter = types.ChannelParticipantsRecent()

api_id = 16692973
api_hash = '4688ac1027344e3d78b3bddf1ce739e8'
phone = '+212666453758'
name='Isma Isma'
limit = 5
channel = 'bull100x_2th'
all_participants = []
async def main():
    started = await TelegramClient(name, api_id, api_hash).start()

    if not isinstance(started, TelegramClient):
        raise ValueError(f"Unexpected client: {started}")

    async with started as client:
        me = await client.get_me()
        print(me.stringify())
        result = await client(functions.contacts.GetStatusesRequest())
        for x in result:
            print(x)

        username = me.username
        print(username)
        print(me.phone)

        offset = 0

    while True:
        print("here")
        participants = await client(functions.channels.GetParticipantsRequest(
            channel='bull100x_2th', filter=my_filter, offset=offset, limit=limit, hash=0
        ))
        if not participants.users:
            break
        await all_participants.extend(participants.users)
        offset += len(participants.users)


asyncio.run(main())