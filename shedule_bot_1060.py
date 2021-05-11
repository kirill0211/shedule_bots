
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
TOKEN = "1623120001:AAFqRnhlwIAP_L4m7LGQvqiyE-jyU0cjZ9o"


# Monday = '''Главный урок
# Главный урок
# Обществознание
# Обществознание
# Русский язык
# Живопись
# Искусство'''
#
# Tuesday = '''Главный урок
# Главный урок
# Математика
# Химия
# История
# Информатика
# Английский язык
# Искусство'''
#
# Wednesday = '''Главный урок
# Главный урок
# Химия
# Физика профильная
# Физика профильная
# Информатика
# Английский язык
# Физ-ра'''
#
# Thursday = '''Главный урок
# Главный урок
# Биология
# Русский язык профильный
# Эвритмия
# Математика
# Проект
# Проект'''
#
# Friday = '''Главный урок
# Главный урок
# Математика
# Математика
# История
# Физика профильная
# Английский язык
# Русский язык'''
# Time = '''
# (lesson# 1)_ 9: 05 - 9: 40
#
# (lesson# 2)_ 9: 50 - 10: 25
#
# (lesson# 3)_ 10: 45 - 11: 25
#
# (lesson# 4)_ 11: 40 - 12: 20
#
# (lesson# 5)_ 12: 30 - 13: 10
#
# (lesson# 6)_ 13: 30 - 14: 10
#
# (lesson# 7)_ 14: 30 - 15: 10
#
# (lesson# 8)_ 15: 20 - 16: 00'''

def main():
    updater = Updater(token=TOKEN)  # объект, который ловит сообщения из телеграм
    dispatcher = updater.dispatcher
    handler = MessageHandler(Filters.all, do_echo)  # отфильтровываем сообщения: теперь устройство должно реагировать
    start_handler = CommandHandler('start', do_start)
    help_handler = CommandHandler('help', do_help)
    keyboard_handler = MessageHandler(Filters.text, do_something)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(keyboard_handler)
    dispatcher.add_handler(handler)
    updater.start_polling()
    updater.idle()
def do_echo(update: Update, context):
    user = update.message.from_user.is_bot
    name = update.message.from_user.first_name
    if user:
        update.message.reply_text(text=f"Ты - бот! Уходи отсюда!!!")
    else:
        update.message.reply_text(text=f"ААААА! {name} что ты делаешь?")
        update.message.reply_text(text="Я не понимаю")

def do_start(update, context):
    keyboard = [
        ["расписание на Понедельник", "расписание на Вторник", "расписание на Среду"],
        ["расписание на Четверг", "расписание на Пятницу"],
        ["Время проведения урока"]
    ]
    update.message.reply_text(text="Hallo!",
                              reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True,
                                                               resize_keyboard=True))  # текст сообщения, который бот автоматически будет выдавать
    update.message.reply_text(text="choose the answer you want",
                       reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True,
                                                        resize_keyboard=True))
def do_help(update, context):
    update.message.reply_text(text="что случилось? Всё ж было норм")
def do_something(update, context):
    text = update.message.text
    if text.lower() == "расписание на понедельник":
        update.message.reply_text(text=Monday, reply_markup=ReplyKeyboardRemove())
    elif text.lower() == "расписание на вторник":
        update.message.reply_text(text=Tuesday, reply_markup=ReplyKeyboardRemove())
    elif text.lower() == "расписание на среду":
        update.message.reply_text(text=Wednesday, reply_markup=ReplyKeyboardRemove())
    elif text.lower() == "расписание на четверг":
        update.message.reply_text(text=Thursday, reply_markup=ReplyKeyboardRemove())
    elif text.lower() == "расписание на пятницу":
        update.message.reply_text(text=Friday, reply_markup=ReplyKeyboardRemove())
    elif text.lower() == "время проведения урока":
        update.message.reply_text(text=Time, reply_markup=ReplyKeyboardRemove())
    else:
        update.message.reply_text(text="Wrong day", reply_markup=ReplyKeyboardRemove())
main()

