from telegram.ext import Updater, MessageHandler, Filters


# Определяем функцию-обработчик сообщений.
def echo(bot, update):
    update.message.reply_text(update.message.text)
    update.message.reply_text('Я получил сообщение "{}".'.format(update.message.text))


def main():
    updater = Updater("495973310:AAE0ikxVW41zJI9mqroKW5NANrrDvbMwRRw")

    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, echo))

    updater.start_polling()
    print('Bot started')
    updater.idle()


if __name__ == '__main__':
    main()