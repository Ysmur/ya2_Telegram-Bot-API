from telegram.ext import Updater, MessageHandler, CommandHandler, Filters
import time


def echo(bot, update):
    update.message.reply_text(update.message.text)


def start(bot, update):
    update.message.reply_text("Привет! Я эхо-бот. Напишите мне что-нибудь, и я пришлю это назад!")


def help(bot, update):
    update.message.reply_text("Я пока не умею помогать... Я только ваше эхо.")


def get_time(bot, update):
    update.message.reply_text(time.asctime().split(" ")[3])


def get_date(bot, update):
    update.message.reply_text(", ".join(time.asctime().split(" ")[1:3]))


def main():
    updater = Updater("495973310:AAE0ikxVW41zJI9mqroKW5NANrrDvbMwRRw")

    dp = updater.dispatcher

    text_handler = MessageHandler(Filters.text, echo)
    dp.add_handler(text_handler)
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("time", get_time))
    dp.add_handler(CommandHandler("date", get_date))

    updater.start_polling()
    print('Bot started')
    updater.idle()


if __name__ == '__main__':
    main()