import asyncio
import sqlite3
import time

from telethon import TelegramClient
from telethon import functions, types
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch


# my_filter = types.ChannelParticipantsRecent()
#
# api_id = 16692973
# api_hash = '4688ac1027344e3d78b3bddf1ce739e8'
# phone = '+212666453758'
# name='Isma Isma'
# limit = 10000
# channel = ''
all_participants = []
def createdb():
    try:
        con = sqlite3.connect("database.db")
        curs = con.cursor()
        curs.execute("""CREATE TABLE accounts(
            id text NOT NULL PRIMARY KEY AUTOINCREMENT,
            name text NOT NULL,
            sent integer NOT NULL
        )""")
        con.commit()
        con.close()
        print(f'[INFO] DATABASE CREATED')
    except sqlite3.OperationalError as e:
        print(e)
        print('DATABASE, operational')
def insertdb(name, sent):
    try:
        con = sqlite3.connect("database.db")
        curs = con.cursor()
        curs.execute("INSERT INTO accounts VALUES (?,?,?) ", (id, name, sent))
        con.commit()
        con.close()
        print(f'[INFO] Row Added To DATABASE, ID : {id}')
    except sqlite3.OperationalError as e:
        print(e)
async def main():
    started = await TelegramClient(name, api_id, api_hash).start()

    if not isinstance(started, TelegramClient):
        raise ValueError(f"Unexpected client: {started}")

    async with started as client:
        offset = 0
        listTele = []
        while True:
            print("here")
            participants = await client(functions.channels.GetParticipantsRequest(
                channel='bull100x_2th', filter=my_filter, offset=offset, limit=limit, hash=42
            ))
            if not participants.users:
                pass
            for user in participants.users:
                listTele.append(user.id)
                insertdb(f"{user.id}",0)
            offset += len(listTele)
            print(listTele)
            print(offset)
            print('waiting 30 secs')
            time.sleep(30)



asyncio.run(main())