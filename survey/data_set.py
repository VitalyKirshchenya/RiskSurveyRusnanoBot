import json
from admin.settings import DEFAULT_LANGUAGE


class DataSet:
    participants = {}
    q_set_de_ = None
    q_set_en_ = None
    q_set_ru_ = None

    def __init__(self):
        try:
            with open('survey/mandatory_questions_de.json') as file:
                self.q_set_de_ = json.load(file)
        except FileNotFoundError:
            print('Language: German not available!')
        try:
            with open('survey/mandatory_questions_en.json') as file:
                self.q_set_en_ = json.load(file)
        except FileNotFoundError:
            print('Language: English not available!')
        try:
            with open('survey/mandatory_questions_ru.json') as file:
                self.q_set_ru_ = json.load(file)
        except FileNotFoundError:
            print('Language: Russian not available!')
        return

    def get_participant(self, chat_id):
        return self.participants[chat_id]

    def add_participant(self, user):
        self.participants[user.chat_id] = user
        return

    def return_question_set_by_language(self, lang):
        if lang == 'de' and self.q_set_de_ is not None:
            return self.q_set_de_
        elif lang == 'en' and self.q_set_en_ is not None:
            return self.q_set_en_
        elif lang == 'ru' and self.q_set_ru_ is not None:
            return self.q_set_ru_
        else:
            return self.return_question_set_by_language(DEFAULT_LANGUAGE)
