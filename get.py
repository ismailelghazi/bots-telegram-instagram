from telethon import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.types import ChannelParticipantsSearch
import asyncio
import telethon.sync


api_id = 16692973
api_hash = '4688ac1027344e3d78b3bddf1ce739e8'
phone_number: str = '+212666453758'
################################################
channel_username = 'bull100x_2th'
################################################
name='Isma Isma'

async def main():
    # The first parameter is the .session file name (absolute paths allowed)
    started = await TelegramClient(name, api_id, api_hash).start()
    async with started as client:
        await client.send_code_request(phone_number)
        me =await client.sign_in(phone_number, input('Enter code: '))
    # ---------------------------------------
    offset = 0
    limit = 200
    my_filter = ChannelParticipantsSearch('')
    all_participants = []
    while_condition = True
    # ---------------------------------------
    channel = client(GetFullChannelRequest(channel_username))
    while while_condition:
        participants = client(GetParticipantsRequest(channel=channel_username, filter=my_filter, offset=offset, limit=limit, hash=0))
        all_participants.extend(participants.users)
        offset += len(participants.users)
        if len(participants.users) < limit:
             while_condition = False
asyncio.run(main())