from telethon import TelegramClient, events
from config import Config

class TelegramBot:
    def __init__(self):
        self.client = TelegramClient('session', Config.TELEGRAM_API_ID, Config.TELEGRAM_API_HASH)

    async def start(self):
        await self.client.start(bot_token=Config.TELEGRAM_BOT_TOKEN)

    async def stop(self):
        await self.client.disconnect()

    def add_message_handler(self, handler):
        @self.client.on(events.NewMessage(pattern='/start'))
        async def start_handler(event):
            await event.reply('Welcome to the Signal Copier Bot!')

        @self.client.on(events.NewMessage)
        async def message_handler(event):
            await handler(event)

    async def send_message(self, chat_id, message):
        await self.client.send_message(chat_id, message)