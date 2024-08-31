from .glob_variables import BotState
from .buttons import Buttons
from utils import db, TweetCapture
from telethon.errors.rpcerrorlist import MessageNotModifiedError


class BotMessageHandler:
    start_message = """
به **ZPOTIFY خود خوش آمدید!** 🎧

نام آهنگ یا هنرمندی را برای من بفرستید تا آهنگ قابل دانلود را پیدا کنم و برایتان ارسال کنم. 🎶

برای دیدن کارهایی که می توانم انجام دهم، تایپ کنید: /help
یا به سادگی روی دکمه دستورالعمل زیر کلیک کنید. 👇
"""

    instruction_message = """
    🎧 **ZPOTIFY** 🎧
    ——————————————————
    🎧 **دانلود موسیقی** 🎧
 ——————————————————
 **1.** لینک آهنگ Spotify را به اشتراک بگذارید. 🔗
 **2.** منتظر تایید دانلود باشید. 📣
 **3.** پس از آماده شدن فایل آهنگ را برای شما ارسال می کنم. 💾
 **4.** همچنین می توانید با یک نمونه آهنگ پیام صوتی ارسال کنید.
 من بهترین تطابق را پیدا می کنم و جزئیات را برای شما ارسال می کنم. 🎤🔍📩
 **5.** اشعار موسیقی، اطلاعات هنرمند و موارد دیگر را دریافت کنید فقط بپرسید. 📜👨‍🎤

 💡 **نکته**: بر اساس عنوان، اشعار یا جزئیات دیگر نیز جستجو کنید!

 📸 ** دانلودر اینستاگرام ** 📸
 ——————————————————
 **1.** پست اینستاگرام، حلقه یا لینک IGTV را ارسال کنید. 🔗
 **2.** دانلود محتوا را شروع می کنم. ⏳
 **3.** وقتی فایل آماده شد براتون میفرستم. 📤

 🐦 **TweetCapture** 🐦
 ——————————————————
 **1.** لینک توییت را ارائه دهید. 🔗
 **2.** از توییت اسکرین شات می گیرم و شروع به دانلود می کنم. 📸
 **3.** وقتی اسکرین شات آماده شد برایتان ارسال می کنم. 🖼️
 **4.** برای دانلود محتوای رسانه ای از توییت،
 بعد از آن روی دکمه "دانلود رسانه" کلیک کنید
 دریافت اسکرین شات 📥

 ——————————————————
 با پیروی از دستورالعمل ها از هر سرویسی استفاده کنید!
 اگر سوالی دارید،
 در صورت تمایل از @Itachi2129 بپرسید.
        """

    search_result_message = """🎵 نتایج جستجوی زیر با درخواست شما مطابقت دارد:
"""

    core_selection_message = """🎵 هسته دانلود دلخواه خود را انتخاب کنید 🎵

"""
    JOIN_CHANNEL_MESSAGE = """به نظر می رسد شما هنوز عضو کانال ما نیستید.
لطفا برای ادامه عضو شوید."""

    search_playlist_message = """لیست پخش شامل این آهنگ ها است:"""

    @staticmethod
    async def send_message(event, text, buttons=None):
        chat_id = event.chat_id
        user_id = event.sender_id
        await BotState.initialize_user_state(user_id)
        await BotState.BOT_CLIENT.send_message(chat_id, text, buttons=buttons)

    @staticmethod
    async def edit_message(event, message_text, buttons=None):
        user_id = event.sender_id

        await BotState.initialize_user_state(user_id)
        try:
            await event.edit(message_text, buttons=buttons)
        except MessageNotModifiedError:
            pass

    @staticmethod
    async def edit_quality_setting_message(e):
        music_quality = await db.get_user_music_quality(e.sender_id)
        if music_quality:
            message = (f"تنظیمات کیفیت: \nFormat: {music_quality['format']}\nQuality: {music_quality['quality']}"
                       f"\n\nAvailable Qualities :")
        else:
            message = "تنظیمات کیفیت یافت نشد."
        await BotMessageHandler.edit_message(e, message, buttons=Buttons.get_quality_setting_buttons(music_quality))

    @staticmethod
    async def edit_core_setting_message(e):
        downloading_core = await db.get_user_downloading_core(e.sender_id)
        if downloading_core:
            message = BotMessageHandler.core_selection_message + f"\nCore: {downloading_core}"
        else:
            message = BotMessageHandler.core_selection_message + "\nNo core setting found."
        await BotMessageHandler.edit_message(e, message, buttons=Buttons.get_core_setting_buttons(downloading_core))

    @staticmethod
    async def edit_subscription_status_message(e):
        is_subscribed = await db.is_user_subscribed(e.sender_id)
        message = f"Subscription settings:\n\nYour Subscription Status: {is_subscribed}"
        await BotMessageHandler.edit_message(e, message,
                                             buttons=Buttons.get_subscription_setting_buttons(is_subscribed))

    @staticmethod
    async def edit_tweet_capture_setting_message(e):
        night_mode = await TweetCapture.get_settings(e.sender_id)
        mode = night_mode['night_mode']
        mode_to_show = "Light"
        match mode:
            case "1":
                mode_to_show = "Dark"
            case "2":
                mode_to_show = "Black"
        message = f"Tweet capture settings:\n\nYour Night Mode: {mode_to_show}"
        await BotMessageHandler.edit_message(e, message, buttons=Buttons.get_tweet_capture_setting_buttons(mode))
