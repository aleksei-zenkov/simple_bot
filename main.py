from aiogram import Bot, Dispatcher, executor, types
import redis

bot = Bot(token='5578408826:AAEQKMhIMK4M-p91wYwmwc8V5_tMeSUvReE')
dp = Dispatcher(bot)

redis_db = redis.from_url("redis://default:uIdGq8c8zpJyCDPZiYJUxV06By9tWBKU@redis-10752.c243.eu-west-1-3.ec2.cloud.redislabs.com:10752")

@dp.message_handler(commands=['start'])
async def welcome_reply(message: types.Message):
  print(message)
  await bot.send_animation(message.from_user.id, 'https://media0.giphy.com/media/3oEjI67Egb8G9jqs3m/giphy.gif')
  chat_id = message.from_user.id
  redis_db.hset(chat_id, 'user', message.from_user.full_name)
  user = redis_db.hget(chat_id, 'user')
  print(f'redis user: {user}')
if __name__ == '__main__':

    executor.start_polling(dp)
