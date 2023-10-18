from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("↯︙ انشاء كود بايروجرام .", callback_data="generate")]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("↯︙المطور .", url="https://t.me/wwMww"),
        ],
    ]

    START = """
↯︙اهلا بك عزيزي المواطن  في بوت انشاء كود بايروجرام تم صنع البوت منقبل المطور كرستال @wwMww .

↯︙ يمكنك انشاء كود بايروجرام بسهولة .

↯︙يتم ارسال الكود في الرسائل المحفوضة .
    """
