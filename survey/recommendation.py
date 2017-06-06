import json
from admin.settings import DEFAULT_LANGUAGE


def __init__(self):
    try:
        with open('survey/recommendations_de.json') as file:
            self.q_set_de_ = json.load(file)
    except FileNotFoundError:
        print('Language: German not available!')
    try:
        with open('survey/recommendations_de.json') as file:
            self.q_set_en_ = json.load(file)
    except FileNotFoundError:
        print('Language: English not available!')
    try:
        with open('survey/recommendations_de.json') as file:
            self.q_set_ru_ = json.load(file)
    except FileNotFoundError:
        print('Language: Russian not available!')
    return


def return_recommendations_de_by_language(self, lang):
    if lang == 'de' and self.q_set_de_ is not None:
        return self.q_set_de_
    elif lang == 'en' and self.q_set_en_ is not None:
        return self.q_set_en_
    elif lang == 'ru' and self.q_set_ru_ is not None:
        return self.q_set_ru_
    else:
        return self.return_question_set_by_language(DEFAULT_LANGUAGE)


def get_recommendations(user, ml):

    recommend_set = return_recommendations_de_by_language(user.lanuage_)
