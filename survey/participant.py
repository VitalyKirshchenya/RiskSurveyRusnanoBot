import pickle
import sqlite3
import time
from admin import settings


class Participant:
    def __init__(self, chat_id=None, init=True, message_id = None):
        self.chat_id_ = 0
        self.language_ = ''
        self.country_ = ''
        self.timezone_ = ''
        self.city_ = ''
        self.industry_ = ''
        self.part_ = 0
        self.block_ = -1
        self.question_ = -1
        self.pointer_ = 0
        self.conditions_ = []
        self.maturity_level = ''
        self.next_block = None
        self.part_name = None
        self.block_name = None
        self.new_block = True
        self.data_set_ = {}

        self.q_set_ = None
        self.auto_queue_ = False
        self.block_complete_ = False
        self.q_idle_ = False
        self.active_ = True
        self.last_ = False
        self.chat_id_ = chat_id
        self.message_id = message_id
        if init:
            try:
                db = sqlite3.connect('survey/participants.db')
                db.execute("INSERT INTO participants (ID, data_set, conditions, country, city, industry,"
                           "language, timezone, question, part, block, q_idle, active, pointer, maturity_level)"
                           "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                           (chat_id, pickle.dumps({}), pickle.dumps([]), '', '', '', '', '', -1, 1, -1, 0, 1, 0, ''))
                db.commit()
                db.close()
                text = "User:\t" + str(self.chat_id_) + "\tregistered.\t" + time.strftime("%X %x\n")
                try:
                    with open('log.txt', 'a') as log:
                        log.write(text)
                except OSError or IOError as error:
                    print(error)
            except sqlite3.Error as error:
                print(error)

    def set_language(self, language):
        if language == ('Deutsch' or 'de'):
            lang = 'de'
        elif language == ('English' or 'en'):
            lang = 'en'
        elif language == ('Русский' or 'ru'):
            lang = 'ru'
        else:
            lang = settings.DEFAULT_LANGUAGE

        self.language_ = lang
        try:
            db = sqlite3.connect('survey/participants.db')
            db.execute("UPDATE participants SET language=? WHERE ID=?", (lang, self.chat_id_))
            db.commit()
            db.close()
        except sqlite3.Error as error:
            print(error)
        return

    def set_data_set(self, data_set):
        self.data_set_ = data_set
        data_set = pickle.dumps(data_set)
        try:
            db = sqlite3.connect('survey/participants.db')
            db.execute("UPDATE participants SET data_set=? WHERE ID=?", (data_set, self.chat_id_))
            db.commit()
            db.close()
        except sqlite3.Error as error:
            print(error)
        return

    def set_country(self, country):
        self.country_ = country
        try:
            db = sqlite3.connect('survey/participants.db')
            db.execute("UPDATE participants SET country=? WHERE ID=?", (country, self.chat_id_))
            db.commit()
            db.close()
        except sqlite3.Error as error:
            print(error)
        return

    def set_city(self, city):
        self.city_ = city
        try:
            db = sqlite3.connect('survey/participants.db')
            db.execute("UPDATE participants SET city=? WHERE ID=?", (city, self.chat_id_))
            db.commit()
            db.close()
        except sqlite3.Error as error:
            print(error)
        return

    def set_industry(self, industry):
        self.industry_ = industry
        try:
            db = sqlite3.connect('survey/participants.db')
            db.execute("UPDATE participants SET industry=? WHERE ID=?", (industry, self.chat_id_))
            db.commit()
            db.close()
        except sqlite3.Error as error:
            print(error)
        return

    def set_part(self, part):
        self.part_ = part
        try:
            db = sqlite3.connect('survey/participants.db')
            db.execute("UPDATE participants SET part=? WHERE ID=?", (self.part_, self.chat_id_))
            db.commit()
            db.close()
        except sqlite3.Error as error:
            print(error)
        return self.part_


    def add_conditions(self, condition):
        if condition == []:
            return
        self.conditions_.append(condition)
        try:
            db = sqlite3.connect('survey/participants.db')
            db.execute("UPDATE participants SET conditions=? WHERE ID=?",
                       (pickle.dumps(self.conditions_), self.chat_id_))
            db.commit()
            db.close()
        except sqlite3.Error as error:
            print(error)
        return

    def set_block(self, block):
        self.block_ = block
        try:
            db = sqlite3.connect('survey/participants.db')
            db.execute("UPDATE participants SET block=? WHERE ID=?", (self.block_, self.chat_id_))
            db.commit()
            db.close()
        except sqlite3.Error as error:
            print(error)
        return self.block_

    def increase_block(self):
        self.block_ += 1
        try:
            db = sqlite3.connect('survey/participants.db')
            db.execute("UPDATE participants SET block=? WHERE ID=?", (self.block_, self.chat_id_))
            db.commit()
            db.close()
        except sqlite3.Error as error:
            print(error)
        return self.block_

    def set_question(self, question):
        self.question_ = question
        try:
            db = sqlite3.connect('survey/participants.db')
            db.execute("UPDATE participants SET question=? WHERE ID=?", (self.question_, self.chat_id_))
            db.commit()
            db.close()
        except sqlite3.Error as error:
            print(error)
        return self.question_

    def increase_question(self):
        self.question_ += 1
        try:
            db = sqlite3.connect('survey/participants.db')
            db.execute("UPDATE participants SET question=? WHERE ID=?", (self.question_, self.chat_id_))
            db.commit()
            db.close()
        except sqlite3.Error as error:
            print(error)
        return self.question_

    def set_pointer(self, pointer):
        self.pointer_ = pointer
        try:
            db = sqlite3.connect('survey/participants.db')
            db.execute("UPDATE participants SET pointer=? WHERE ID=?", (self.pointer_, self.chat_id_))
            db.commit()
            db.close()
        except sqlite3.Error as error:
            print(error)
        return self.pointer_

    def increase_pointer(self):
        self.pointer_ += 1
        try:
            db = sqlite3.connect('survey/participants.db')
            db.execute("UPDATE participants SET pointer=? WHERE ID=?", (self.pointer_, self.chat_id_))
            db.commit()
            db.close()
        except sqlite3.Error as error:
            print(error)
        return self.pointer_

    def set_q_idle(self, state):
        self.q_idle_ = state
        try:
            db = sqlite3.connect('survey/participants.db')
            db.execute("UPDATE participants SET q_idle=? WHERE ID=?", (self.q_idle_, self.chat_id_))
            db.commit()
            db.close()
        except sqlite3.Error as error:
            print(error)
        return self.part_

    def set_active(self, state):
        self.active_ = state
        try:
            db = sqlite3.connect('survey/participants.db')
            db.execute("UPDATE participants SET active=? WHERE ID=?", (self.active_, self.chat_id_))
            db.commit()
            db.close()
        except sqlite3.Error as error:
            print(error)
        return self.part_

    def delete_participant(self):
        try:
            db = sqlite3.connect('survey/participants.db')
            db.execute("DELETE FROM participants WHERE ID LIKE ?", (str(self.chat_id_) + '%',))
            db.commit()
            db.close()
        except sqlite3.Error as error:
            print(error)
        text = "User:\t" + str(self.chat_id_) + "\tunregistered.\t" + time.strftime("%X %x\n")
        try:
            with open('log.txt', 'a') as log:
                log.write(text)
        except OSError or IOError as error:
            print(error)
        return 0

    def change_chat_id(self):
        new_id = str(self.chat_id_) + '_' + str(self.message_id)
        try:
            db = sqlite3.connect('survey/participants.db')
            db.execute("UPDATE participants SET ID=? WHERE ID=?", (new_id, self.chat_id_))
            db.commit()
            db.close()
        except sqlite3.Error as error:
            print(error)
        return new_id

    def set_maturity_level(self, maturity_level_):
        try:
            db = sqlite3.connect('survey/participants.db')
            db.execute("UPDATE participants SET maturity_level=? WHERE ID=?", (maturity_level_, self.chat_id_))
            db.commit()
            db.close()
        except sqlite3.Error as error:
            print(error)

    def set_next_block(self):
        q_set = self.q_set_
        try:
            block = q_set[self.pointer_]["blocks"][self.block_ + 1]
            self.next_block = [self.pointer_, self.block_ + 1, block]
            return q_set[self.pointer_]["part"]
        except IndexError:
            try:
                block = q_set[self.pointer_ + 1]["blocks"][0]
                self.next_block = [self.pointer_ + 1, 0, block]

                return q_set[self.pointer_ + 1]["part"]
            except IndexError:
                self.next_block = None

    def set_part_name(self):
        q_set = self.q_set_

    def check_last_q(self):
        que_set = self.q_set_
        num_b = len(que_set[self.pointer_]["blocks"])
        num_q = len(que_set[self.pointer_]["blocks"][self.block_]["questions"])
        try:
            if self.question_ == num_q - 1:
                if self.block_ == num_b - 1:
                    self.block_name = que_set[self.pointer_+1]["blocks"][0]["block_name"]
                else:
                    self.block_name = que_set[self.pointer_]["blocks"][self.block_+1]["block_name"]
                return self.block_name
        except IndexError:
            self.block_name = None

    def check_last_b(self):
        que_set = self.q_set_
        num_b = len(que_set[self.pointer_]["blocks"])
        num_q = len(que_set[self.pointer_]["blocks"][num_b-1]["questions"])
        try:
            if self.block_ == num_b - 1:
                if self.question_ == num_q - 1:
                    self.part_name = que_set[self.pointer_+1]["part_name"]
                    return self.part_name
        except IndexError:
            self.part_name = None

    def check_requirements(self, question):
        condition = question["condition_required"]
        if condition == []:
            return True

        if settings.CONDITION_SCHEME == "OR":
            for element in condition:
                if element in self.conditions_:
                    return True
            return False
        elif settings.CONDITION_SCHEME == "AND":
            for element in condition:
                if element not in self.conditions_:
                    return False
            return True

    def pause(self):
        self.active_ = False