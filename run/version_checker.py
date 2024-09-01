from utils import db


async def update_bot_version_user_season(event) -> bool:
    user_id = event.sender_id
    if not await db.check_username_in_database(user_id):
        await event.respond("ما ربات را به‌روزرسانی کرده‌ایم، لطفاً استفاده از آن را دوباره شروع کنید /start فرمان.")
        await db.set_user_updated_flag(user_id, 0)
        return False
    await db.set_user_updated_flag(user_id, 1)
    return True
