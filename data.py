from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ", callback_data="generate")]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("sᴜᴩᴩᴏʀᴛ", url="https://t.me/HumanzBotSupport"),
         InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴩᴇʀ", url="https://t.me/BijiKacang"),
        ],
    ]

    START = """
Hᴇʏ {},
{}Adalah Bot Khusus Untuk Mengambil String Session Dengan Mudah Dan Aman. Yang Di Rancang Oleh [Humanz](t.me/BijiKacang).\n━━━━━━━━━━━━━━━━━━━━━━━\nJika Anda Tidak Mempercayai Bot Ini
Jangan Gunakan Bot Ini Dan Blokir Saja Aja!\n━━━━━━━━━━━━━━━━━━━━━━━\nMaintance By [Humanz](t.me/BijiKacang)
    """
