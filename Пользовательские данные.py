from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler


def start(bot, update):
    update.message.reply_text(
        "Привет. Пройдите небольшой опрос, пожалуйста!\n"
        "Вы можете прервать опрос, послав команду /stop.\n"
        "В каком городе вы живете?")

    return 1


def first_response(bot, update, user_data):  # Добавили словарь user_data в параметры.
    user_data['locality'] = update.message.text  # Сохраняем ответ в словаре.
    update.message.reply_text("Какая погода в городе {0}?".format(user_data['locality']))
    return 2


def second_response(bot, update, user_data):  # Добавили словарь user_data в параметры.
    weather = update.message.text
    update.message.reply_text("Спасибо за участие в опросе! Привет, {0}!". \
                              format(user_data['locality']))  # Используем user_data в ответе.
    return ConversationHandler.END


def stop(bot, update):
    update.message.reply_text("Жаль. А было бы интересно пообщаться. Всего доброго!")
    return ConversationHandler.END


def main():
    updater = Updater("532909432:AAGonfQ-xYeoNlaTcJf4wkQ1ribNRRKzAx8")
    dp = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],  # Точка входа в диалог.
        # В данном случае команда /start. Она задает первый вопрос.

        states={
            # Состояния внутри диалога. В данном случае два обработчика сообщений, фильтрующих текстовые сообщения.
            1: [MessageHandler(Filters.text, first_response, pass_user_data=True)],
            # Добавили user_data для сохранения ответа.
            2: [MessageHandler(Filters.text, second_response, pass_user_data=True)]  # ...и для его использования.
        },
        fallbacks=[CommandHandler('stop', stop)]  # Точка прерывания диалога. В данном случае команда /stop.
    )

    dp.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()