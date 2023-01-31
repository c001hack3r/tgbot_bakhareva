# import cherrypy
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import description as dn, config


# WEBHOOK_HOST = '185.22.233.223'
# WEBHOOK_PORT = 443
# WEBHOOK_LISTEN = '0.0.0.0'

# WEBHOOK_SSL_CERT = './webhook_cert.pem'  # Путь к сертификату
# WEBHOOK_SSL_PRIV = './webhook_pkey.pem'  # Путь к приватному ключу

# WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
# WEBHOOK_URL_PATH = "/%s/" % (config.TOKEN)

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

# # Наш вебхук-сервер
# class WebhookServer(object):
#     @cherrypy.expose
#     def index(self):
#         if 'content-length' in cherrypy.request.headers and \
#                         'content-type' in cherrypy.request.headers and \
#                         cherrypy.request.headers['content-type'] == 'application/json':
#             length = int(cherrypy.request.headers['content-length'])
#             json_string = cherrypy.request.body.read(length).decode("utf-8")
#             update = telebot.types.Update.de_json(json_string)
#             # Эта функция обеспечивает проверку входящего сообщения
#             bot.get_updates([update])
#             return ''
#         else:
#             raise cherrypy.HTTPError(403)


#Основные кнопки
main_menu = InlineKeyboardMarkup()
main_menu.row(types.InlineKeyboardButton(text="Виды занятий", callback_data="training"))
main_menu.row(types.InlineKeyboardButton(text="Обо мне", callback_data="about_me"))
main_menu.insert(types.InlineKeyboardButton(text='Telegram', url='t.me/bakhareva_fit'))
# main_menu.insert(types.InlineKeyboardButton(text='Instagram', url='instagram.com/bakhareva__fit/'))
main_menu.row(types.InlineKeyboardButton(text='Твоя мотивация', callback_data='u_motion'))
main_menu.row(types.InlineKeyboardButton(text='Запишись на первую пробную тренировку!', url='t.me/Bakharevafit'))
#Кнопка Закрыть
# close_btm = InlineKeyboardMarkup()
# close_btm.row(types.InlineKeyboardButton(text='Закрыть', callback_data='close'))
#Кнопка Назад в главное меню
back_to_mm = InlineKeyboardMarkup()
back_to_mm.row(types.InlineKeyboardButton(text='< Назад в главное меню', callback_data='back_to_mm'))
#Кнопка Привет!
hello_btm = InlineKeyboardMarkup()
hello_btm.row(types.InlineKeyboardButton(text='Привет!', callback_data='hello_btm'))
#Подменю Тренировки
train_info = InlineKeyboardMarkup()
train_info.row(InlineKeyboardButton(text='Персональные тренировки', callback_data='personal_train'))
train_info.row(InlineKeyboardButton(text='Парные', callback_data='twice_train'))
train_info.insert(InlineKeyboardButton(text='Мини-группа', callback_data='mini_group_train'))
train_info.row(InlineKeyboardButton(text='Групповая', callback_data='group_train'))
train_info.insert(InlineKeyboardButton(text='Тренировки "Онлайн"', callback_data='online_train'))
train_info.row(InlineKeyboardButton(text='Консультации по питанию', callback_data='dietary_plan'))
train_info.row(types.InlineKeyboardButton(text='< Назад в главное меню', callback_data='back_to_mm'))
#Выход из тренировок
back_to_training = InlineKeyboardMarkup()
back_to_training.row(InlineKeyboardButton(text='Узнать стоимость >>', url='t.me/Bakharevafit'))
back_to_training.row(InlineKeyboardButton(text='< Назад к тренировкам', callback_data='training'))
back_to_training.row(InlineKeyboardButton(text='<< Назад в главное меню', callback_data='back_to_mm'))

#Начало диалога
@dp.message_handler(commands = ['start','help'])
async def command_start(message: types.Message):
    await message.answer(dn.start_msg, parse_mode='markdown', reply_markup=main_menu)
    await bot.send_message('392603415', f'⚡️Новая активность:\n\
Time: {message.date}\n\
User id: {message.from_user.id}\n\
Name: {message.from_user.first_name} {message.from_user.last_name}\n\
Username: @{message.from_user.username}')
    


#Ответ на нажатие кнопки Обо мне        
@dp.callback_query_handler(text='about_me')
async def about_me_info(callback: types.CallbackQuery):
    # await bot.delete_message(callback.from_user.id, callback.message.message_id)
    # await bot.send_video(callback.from_user.id, open('media/about_me.mp4','rb'))
    await bot.send_photo(callback.from_user.id, 'AgACAgIAAxkBAAIBpWPZAAFDTBCXAjDwDI_r-cGbIp2tNAAChsIxG6_xyEpyVxHaQc_Y1wEAAwIAA3MAAy0E')
    await callback.message.answer(dn.about_me, parse_mode='markdown', reply_markup=back_to_mm)
    await callback.answer()

#Ответ на нажатие кнопки "Твоя мотивация"
@dp.callback_query_handler(text='u_motion')
async def motion_info(callback: types.CallbackQuery):
    await bot.send_video(callback.from_user.id, 'BAACAgIAAxkBAAO7Y8XFooD3NbwFS_AROUR9xS9MkdoAAvwkAAKZljBKcIw40r1ZQT4tBA')
    await callback.message.answer(dn.u_motion, parse_mode='markdown', reply_markup=back_to_mm)
    await callback.answer()

#Ответ на нажатие кнопки Тренировки   
@dp.callback_query_handler(text='training')
async def uslugi_info(callback: types.CallbackQuery):
    await callback.message.edit_text(dn.training, parse_mode='markdown', reply_markup=train_info)
    await callback.answer()
#Ответ на нажатие кнопки Персональные тренировки   
@dp.callback_query_handler(text='personal_train')
async def personal_train_info(callback: types.CallbackQuery):
    await callback.message.edit_text(dn.personal_train, parse_mode='markdown', reply_markup=back_to_training)
    await callback.answer()
#Ответ на нажатие кнопки Парные тренировки   
@dp.callback_query_handler(text='twice_train')
async def twice_train_info(callback: types.CallbackQuery):
    await callback.message.edit_text(dn.twice_train, parse_mode='markdown', reply_markup=back_to_training)
    await callback.answer()
#Ответ на нажатие кнопки Тренировки в мини группе   
@dp.callback_query_handler(text='mini_group_train')
async def mini_group_train_info(callback: types.CallbackQuery):
    await callback.message.edit_text(dn.mini_group_train, parse_mode='markdown', reply_markup=back_to_training)
    await callback.answer()
#Ответ на нажатие кнопки Групповые тренировки   
@dp.callback_query_handler(text='group_train')
async def group_train_info(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id, 'AgACAgIAAxkBAAIBvWPZA96rDk-sN5VpDE_P2n_2ueQBAAKQwjEbr_HISr6Q9PqSmJuvAQADAgADcwADLQQ')
    await callback.message.answer(dn.group_train, parse_mode='markdown', reply_markup=back_to_training)
    await callback.answer()
#Ответ на нажатие кнопки Онлайн тренировки   
@dp.callback_query_handler(text='online_train')
async def online_train_info(callback: types.CallbackQuery):
    await callback.message.edit_text(dn.online_train, parse_mode='markdown', reply_markup=back_to_training)
    await callback.answer()
#Ответ на нажатие кнопки План питания   
@dp.callback_query_handler(text='dietary_plan')
async def dietary_plan_info(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id, 'AgACAgIAAxkBAAIBgmPY-aTKkZ8ctRA4PDQQ1Dbzv24BAAJrwjEbr_HISkCyRF0iygLhAQADAgADcwADLQQ',)
    await callback.message.answer(dn.dietary_plan, parse_mode='markdown', reply_markup=back_to_training)
    await callback.answer()

#Ответ на нажатие кнопки Назад в главное меню
@dp.callback_query_handler(text='back_to_mm')
async def back_to_mm_info(callback: types.CallbackQuery):
    await callback.message.edit_text(dn.start_msg, parse_mode='markdown', reply_markup=main_menu)
    await callback.answer()

# Получем file_id видео и фото
# @dp.message_handler(content_types=["video"])
# async def video_cmd(message):
#     id_video = message.video.file_id
#     await bot.send_message('720076833', id_video)
# @dp.message_handler(content_types=['photo'])
# async def photo_cmd(message):
#     id_photo = message.photo[0]['file_id']
#     await bot.send_message('720076833', id_photo)

# #Ответ на нажатие кнопки Закрыть
# @dp.callback_query_handler(text='close')
# async def close_button(message: types.Message):
#      await bot.delete_message(message.from_user.id, message.message.message_id)

executor.start_polling(dp, skip_updates=True)