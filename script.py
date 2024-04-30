import os
import asyncio
from telethon import TelegramClient

async def main():
    api_id = int(os.environ.get('API_ID'))
    api_hash = os.environ.get('API_HASH')
    chat_id = int(os.environ.get('CHAT_ID'))

    async with TelegramClient('anon', api_id, api_hash) as client:
        await client.send_message(chat_id, 'Hello from GitHub Actions!')

if __name__ == '__main__':
    asyncio.run(main())
