from ..telegram_client import TelegramBot

class NotificationService:
    @staticmethod
    async def send_telegram_notification(user_id, message):
        bot = TelegramBot()
        await bot.start()
        await bot.send_message(user_id, message)
        await bot.stop()

    @staticmethod
    def send_email_notification(user_email, subject, body):
        # Implement email sending logic here
        pass