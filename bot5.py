import os
import telebot

# token = os.getenv['TOKEN']
bot = telebot.TeleBot('') #anadimos el token
updates = bot.get_updates()
message = updates[0].message
from_user = message.from_user
id = from_user.id
get_me = bot.get_me()

@bot.message_handler(commands=['foto', 'photo'])
def foto(mensaje):
    bot.send_chat_action(id, 'typing')
    photo = open('ucrish.jpg', 'rb')
    bot.send_photo(id, photo)

@bot.message_handler(commands=['video', 'mp4'])
def documento(mensaje):
    bot.send_chat_action(id, 'typing')
    video = open('video.mp4', 'rb')
    bot.send_video(id, video)

bot.polling()