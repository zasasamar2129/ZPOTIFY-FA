from run import Button


class Buttons:
    source_code_button = [
        Button.url(" کد منبع", url="https://github.com/zasasamar2129/ZPOTIFY-FA.git")]

    main_menu_buttons = [
        [Button.inline("دستورالعمل ها", b"instructions"), Button.inline("تنظیمات", b"setting")],
        source_code_button,
        [Button.url("ارتباط ادمین", url="https://t.me/Itachi2129")],
    ]

    back_button = Button.inline("<< بازگشت به منوی ", b"back")

    setting_button = [
        [Button.inline("پیش فرض", b"setting/core")],
        [Button.inline("کیفیت", b"setting/quality")],
        [Button.inline("ضبط توییت", b"setting/TweetCapture")],
        [Button.inline("اشتراک", b"setting/subscription")],
        [back_button]
    ]

    back_button_to_setting = Button.inline("<< برگشت", b"setting/back")

    cancel_broadcast_button = [Button.inline("لغو پخش", data=b"admin/cancel_broadcast")]

    admins_buttons = [
        [Button.inline("پخش", b"admin/broadcast")],
        [Button.inline("آمار", b"admin/stats")],
        [Button.inline("لغو", b"cancel")]
    ]

    broadcast_options_buttons = [
        [Button.inline("پخش برای همه اعضا", b"admin/broadcast/all")],
        [Button.inline("فقط برای مشترکین پخش شود", b"admin/broadcast/subs")],
        [Button.inline("فقط برای کاربران مشخص پخش شود", b"admin/broadcast/specified")],
        [Button.inline("لغو", b"cancel")]
    ]

    continue_button = [Button.inline("ادامه دهید", data='membership/continue')]

    cancel_subscription_button_quite = [Button.inline("لغو اشتراک", b"setting/subscription/cancel/quite")]

    cancel_button = [Button.inline("لغو", b"cancel")]

    @staticmethod
    def get_tweet_capture_setting_buttons(mode):
        match mode:
            case "0":
                return [
                    [Button.inline("🔹 حالت روز", data=b"setting/TweetCapture/mode/0")],
                    [Button.inline("حالت شب", data=b"setting/TweetCapture/mode/1")],
                    [Button.inline("حالت سیاه", data=b"setting/TweetCapture/mode/2")],
                    [Buttons.back_button, Buttons.back_button_to_setting]
                ]
            case "1":
                return [
                    [Button.inline("حالت روز", data=b"setting/TweetCapture/mode/0")],
                    [Button.inline("🔹 حالت شب", data=b"setting/TweetCapture/mode/1")],
                    [Button.inline("حالت سیاه", data=b"setting/TweetCapture/mode/2")],
                    [Buttons.back_button, Buttons.back_button_to_setting]
                ]
            case "2":
                return [
                    [Button.inline("حالت روز", data=b"setting/TweetCapture/mode/0")],
                    [Button.inline("حالت شب", data=b"setting/TweetCapture/mode/1")],
                    [Button.inline("🔹 حالت سیاه", data=b"setting/TweetCapture/mode/2")],
                    [Buttons.back_button, Buttons.back_button_to_setting]
                ]

    @staticmethod
    def get_subscription_setting_buttons(subscription):
        if subscription:
            return [
                [Button.inline("لغو اشتراک", data=b"setting/subscription/cancel")],
                [Buttons.back_button, Buttons.back_button_to_setting]
            ]
        else:
            return [
                [Button.inline("مشترک شوید", data=b"setting/subscription/add")],
                [Buttons.back_button, Buttons.back_button_to_setting]
            ]

    @staticmethod
    def get_core_setting_buttons(core):
        match core:
            case "Auto":
                return [
                    [Button.inline("🔸 خودکار", data=b"setting/core/auto")],
                    [Button.inline("YoutubeDL", b"setting/core/youtubedl")],
                    [Button.inline("SpotDL", b"setting/core/spotdl")],
                    [Buttons.back_button, Buttons.back_button_to_setting],
                ]
            case "SpotDL":
                return [
                    [Button.inline("خودکار", data=b"setting/core/auto")],
                    [Button.inline("YoutubeDL", b"setting/core/youtubedl")],
                    [Button.inline("🔸 SpotDL", b"setting/core/spotdl")],
                    [Buttons.back_button, Buttons.back_button_to_setting],
                ]
            case "YoutubeDL":
                return [
                    [Button.inline("خودکار", data=b"setting/core/auto")],
                    [Button.inline("🔸 YoutubeDL", b"setting/core/youtubedl")],
                    [Button.inline("SpotDL", b"setting/core/spotdl")],
                    [Buttons.back_button, Buttons.back_button_to_setting],
                ]

    @staticmethod
    def get_quality_setting_buttons(music_quality):
        if isinstance(music_quality['quality'], int):
            music_quality['quality'] = str(music_quality['quality'])

        match music_quality:
            case {'format': 'flac', 'quality': "693"}:
                return [
                    [Button.inline("◽️ Flac", b"setting/quality/flac")],
                    [Button.inline("Mp3 (320)", b"setting/quality/mp3/320")],
                    [Button.inline("Mp3 (128)", b"setting/quality/mp3/128")],
                    [Buttons.back_button, Buttons.back_button_to_setting],
                ]

            case {'format': "mp3", 'quality': "320"}:
                return [
                    [Button.inline("Flac", b"setting/quality/flac")],
                    [Button.inline("◽️ Mp3 (320)", b"setting/quality/mp3/320")],
                    [Button.inline("Mp3 (128)", b"setting/quality/mp3/128")],
                    [Buttons.back_button, Buttons.back_button_to_setting],
                ]

            case {'format': "mp3", 'quality': "128"}:
                return [
                    [Button.inline("Flac", b"setting/quality/flac")],
                    [Button.inline("Mp3 (320)", b"setting/quality/mp3/320")],
                    [Button.inline("◽️ Mp3 (128)", b"setting/quality/mp3/128")],
                    [Buttons.back_button, Buttons.back_button_to_setting],
                ]

    @staticmethod
    def get_search_result_buttons(sanitized_query, search_result, page=1) -> list:

        button_list = [
            [Button.inline(f"🎧 {details['track_name']} - {details['artist_name']} 🎧 ({details['release_year']})",
                           data=f"spotify/info/{details['track_id']}")]
            for details in search_result[(page-1) * 10:]
        ]

        if len(search_result) > 1:
            button_list.append([Button.inline("صفحه قبلی", f"prev_page/s/{sanitized_query}/page/{page - 1}"),
                                Button.inline("صفحه بعدی", f"next_page/s/{sanitized_query}/page/{page + 1}")])
        button_list.append([Button.inline("لغو ", b"cancel")])

        return button_list

    @staticmethod
    def get_playlist_search_buttons(playlist_id, search_result, page=1) -> list:
        button_list = [
            [Button.inline(f"🎧 {details['track_name']} - {details['artist_name']} 🎧 ({details['release_year']})",
                           data=f"spotify/info/{details['track_id']}")]
            for details in search_result[(page-1) * 10:]
        ]

        if len(search_result) > 1:
            button_list.append([Button.inline("صفحه قبلی", f"prev_page/p/{playlist_id}/page/{page - 1}"),
                                Button.inline("صفحه بعدی", f"next_page/p/{playlist_id}/page/{page + 1}")])
        button_list.append([Button.inline("لغو ", b"cancel")])

        return button_list
