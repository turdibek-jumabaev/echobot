from loader import bot

# /help - buyrug'iga javob qaytarish
@bot.message_handler(commands=['help'])
async def bot_help(message):
    await bot.send_message(chat_id=message.chat.id, text="Qanday yordam kerak?")