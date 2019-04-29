from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

reply_keyboard = [['/address', '/phone', '/site', '/work_time'], ['/close']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)


def start(bot, update):
    update.message.reply_text("Я бот-справочник. Какая информация вам нужна?", reply_markup=markup)


# Напишем соответствующие функции.
def address(bot, update):
    update.message.reply_text("Адрес: г. Москва, ул. Льва Толстого, 16")


def phone(bot, update):
    update.message.reply_text("Телефон: +7(495)776-3030")


def site(bot, update):
    update.message.reply_text("Сайт: http://www.yandex.ru/company")


def work_time(bot, update):
    update.message.reply_text("Время работы: пн-пт -- 9-00 - 19-00")


def close(bot, update):
    update.message.reply_text("Ok", reply_markup=ReplyKeyboardRemove())


def main():
    updater = Updater("495973310:AAE0ikxVW41zJI9mqroKW5NANrrDvbMwRRw")

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))

    # Зарегистрируем их в диспетчере.
    dp.add_handler(CommandHandler("address", address))
    dp.add_handler(CommandHandler("phone", phone))
    dp.add_handler(CommandHandler("site", site))
    dp.add_handler(CommandHandler("work_time", work_time))
    dp.add_handler(CommandHandler("close", close))

    updater.start_polling()
    print('Bot started')
    updater.idle()


if __name__ == '__main__':
    main()