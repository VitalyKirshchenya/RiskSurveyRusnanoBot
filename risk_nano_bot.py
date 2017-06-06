"""
risk-survey-bot

 developed by Kirshchenya Vitaly for RUSNANO
 Supervisor: Fomichov Vladimir
 Company Advisor: Dozhdikov Konstantin


"""

from telegram import Bot, Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, RegexHandler
from telegram import TelegramError

from survey.questions import initialize_participants
from survey.questions import question_handler
from survey.questions import continue_survey
from survey.set_keyboard import get_keyboard_inline
from survey.set_keyboard import keyboard_menu
from survey.participant import Participant

from survey.set_keyboard import languages

from admin.settings import INFO_TEXT
from admin.settings import STOP_TEXT
from admin.settings import DEFAULT_LANGUAGE
from admin.settings import DELETE
from admin.settings import TOKEN
from admin.settings import DESCRIPTIONS
from admin.settings import DESCRIPTIONS_INTRO
from survey.model import model_predict

import os, glob, re

data_set = None


def start(bot: Bot, update: Update):
    global data_set
    if update.message.chat_id not in data_set.participants:
        reply_markup = ReplyKeyboardMarkup(languages)
        try:
            bot.send_message(chat_id=update.message.chat_id, text="Please choose a language:",
                             reply_markup=reply_markup)
        except TelegramError as error:
            if error.message == 'Unauthorized':
                return
        participant = Participant(update.message.chat_id, message_id=update.message.message_id)
        data_set.participants[update.message.chat_id] = participant
    else:
        user = data_set.participants[update.message.chat_id]
        # A user that has already completed the survey tries to do it again.
        if user.pointer_ == 0xFFFF:
            reply_markup = ReplyKeyboardMarkup(languages)
            try:
                bot.send_message(chat_id=update.message.chat_id, text="Please choose a language:",
                                 reply_markup=reply_markup)
            except TelegramError as error:
                if error.message == 'Unauthorized':
                    return
            participant = Participant(update.message.chat_id, message_id=update.message.message_id)
            data_set.participants[update.message.chat_id] = participant
        else:
            continue_survey(user, bot)


def delete(bot: Bot, update: Update):
    if not DELETE:
        return

    global data_set
    chat_id = update.message.chat_id
    user = data_set.participants[update.message.chat_id]
    if user.pointer_ == 0XFFFF:
        reply_markup = keyboard_menu(user.language_)
    else:
        reply_markup = keyboard_menu('en')
    user.active_ = False
    user.delete_participant()

    try:
        file = 'survey/data_incomplete/' + str(user.chat_id_) + '*.csv'
        for f in glob.glob(file):
            os.remove(f)
    except OSError:
        pass

    try:
        file = 'survey/data_complete/' + str(user.chat_id_) + '*.csv'
        for f in glob.glob(file):
            os.remove(f)
    except OSError:
        pass

    del data_set.participants[update.message.chat_id]
    try:
        bot.send_message(chat_id=chat_id, text="Successfully deleted DB entry and user data. To restart enter /start",
                         reply_markup=reply_markup)
    except TelegramError as error:
        if error.message == 'Unauthorized':
            user.pause()


def stop(bot: Bot, update: Update):
    global data_set
    chat_id = update.message.chat_id
    user = data_set.participants[update.message.chat_id]
    user.pause()
    reply_markup = keyboard_menu(user.language_)
    try:
        message = STOP_TEXT[user.language_]
        bot.send_message(chat_id=chat_id, text=message, reply_markup=reply_markup)
    except KeyError:
        message = STOP_TEXT[DEFAULT_LANGUAGE]
        bot.send_message(chat_id=chat_id, text=message, reply_markup=reply_markup)
    except TelegramError as error:
        if error.message == 'Unauthorized':
            user.pause()


def msg_handler(bot, update):
    global data_set
    question_handler(bot, update, data_set)


def info(bot: Bot, update: Update):
    global data_set
    try:
        user = data_set.participants[update.message.chat_id]
        message = INFO_TEXT[user.language_]
        reply_markup = keyboard_menu(user.language_)
        try:
            bot.sendMessage(update.message.chat_id, text=message, reply_markup=reply_markup)
        except TelegramError:
            return
    except KeyError:
        message = INFO_TEXT[DEFAULT_LANGUAGE]
        try:
            bot.sendMessage(update.message.chat_id, text=message)
        except TelegramError:
            return


def level_description(bot, update):
    global data_set
    query = update.callback_query
    try:
        user = data_set.participants[query.message.chat_id]
        language = user.language_
    except KeyError:
        language = DEFAULT_LANGUAGE

    # if query.data == 'back':
    #     reply_markup = keyboard_menu(language)
    #     try:
    #         bot.editMessageText(text=query.message.text, chat_id=query.message.chat_id,
    #                             message_id=query.message.message_id, reply_markup=reply_markup)
    #     except TelegramError:
    #         return
    # else:
    message = DESCRIPTIONS[query.data]
    keyboard = get_keyboard_inline(language)
    try:
        bot.editMessageText(text=message, chat_id=query.message.chat_id, message_id=query.message.message_id
                            , reply_markup=keyboard)
    except TelegramError as error:
        print(error)
        return


def level_description_intro(bot, update):
    global data_set
    try:
        user = data_set.participants[update.message.chat_id]
        language = user.language_
    except KeyError:
        language = DEFAULT_LANGUAGE
    message = DESCRIPTIONS_INTRO[language]
    keyboard = get_keyboard_inline(language)
    try:
        bot.sendMessage(text=message, chat_id=update.message.chat_id, reply_markup=keyboard)
    except TelegramError as error:
        print(error)
        return


def recommendations(bot, update):
    global data_set
    try:
        user = data_set.participants[update.message.chat_id]
    except KeyError:
        user = data_set.participants[DEFAULT_LANGUAGE]
    message = 'К сожалению данная функция еще не работает'
    keyboard = keyboard_menu(user.language_)
    try:
        bot.sendMessage(text=message, chat_id=update.message.chat_id, reply_markup=keyboard)
    except TelegramError:
        return


def main():
    updater = Updater(TOKEN[0])
    dp = updater.dispatcher

    global data_set
    data_set = initialize_participants()
    dp.add_handler(RegexHandler('^start|начать|старт|Старт|Начать сначала|Начать|Start again$', start))
    dp.add_handler(RegexHandler('^Уровни модели зрелости|Maturity model levels$', level_description_intro))
    dp.add_handler(RegexHandler('^Информация о системе|Information about system$$', info))
    dp.add_handler(RegexHandler('^Удалить данные обо мне|Delete data about me$', delete))
    dp.add_handler(RegexHandler('^Personal recommendations|Персональные рекомендации$', recommendations))

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('delete_me', delete))
    dp.add_handler(CommandHandler('stop', stop))
    dp.add_handler(CommandHandler('info', info))
    dp.add_handler(MessageHandler(Filters.text, callback=msg_handler))
    updater.dispatcher.add_handler(CallbackQueryHandler(level_description))
    # model = model_predict()

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
