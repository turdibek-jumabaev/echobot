from loader import bot

# /start - buyrug'iga javob qaytarish
@bot.message_handler(commands=['start'])
async def bot_start(message):
    await bot.send_message(chat_id=message.chat.id, text=f"Salom {message.from_user.first_name}")
