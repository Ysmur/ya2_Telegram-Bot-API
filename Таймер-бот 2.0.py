from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Обычный обработчик, как и те, которыми мы пользовались раньше.
# Но с дополнительными параметрами, которые раньше не использовали:
# job_queue - очередь задач, в которую мы добавим свою задачу.
# chat_data - словарь для передачи данных, между обработчиками сообщений от того же собеседника.

def set_timer(bot, update, job_queue, chat_data, args):
    # создаем задачу task в очереди job_queue через 20 секунд
    # передаем ей идентификатор текущего чата (будет доступен через job.context)

    delay = int(args[0]) if len(args) > 0 else 20  # секунд

    job = job_queue.run_once(task, delay, context=update.message.chat_id)

    # Запоминаем в пользовательских данных созданную задачу.
    chat_data['job'] = job

    # Присылаем сообщение о том, что все получилось.
    update.message.reply_text('Вернусь через {delay} секунд!'.format(**locals()))


def task(bot, job):
    bot.send_message(job.context, text='Вернулся!')


def unset_timer(bot, update, chat_data):
    # Проверяем, что задача ставилась. (вот, зачем нужно было ее записать в chat_data)
    if 'job' in chat_data:
        # планируем удаление задачи (выполнится, когда будет возможность)
        chat_data['job'].schedule_removal()
        # и очищаем пользовательские данные
        del chat_data['job']

    update.message.reply_text('Хорошо, вернулся сейчас!')


def main():
    updater = Updater("495973310:AAE0ikxVW41zJI9mqroKW5NANrrDvbMwRRw")

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("set_timer", set_timer, pass_job_queue=True, pass_chat_data=True, pass_args=True))
    dp.add_handler(CommandHandler("unset_timer", unset_timer, pass_chat_data=True))

    updater.start_polling()
    print('Bot started')
    updater.idle()


if __name__ == '__main__':
    main()