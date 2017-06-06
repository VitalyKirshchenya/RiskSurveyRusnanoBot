# Telegram Token

TOKEN = ["273491574:AAF1C2VrDhkAw5a9f05QcZGeX1wjIWv5ZNI"]
# TOKEN = ["155567146:AAH3MaKUD-nnHgPOhNrKP0VtfczKiIL07Fs"]
# Debug mode on/off
DEBUG = False

# /delete command enabled/disabled
DELETE = True

# Default language if something goes wrong.
DEFAULT_LANGUAGE = 'ru'

# Default timezone if something goes wrong.
DEFAULT_TIMEZONE = 'Europe/Moscow'

# OR    - One condition is enough
# AND   - All conditions must hold
CONDITION_SCHEME = 'OR'

INFO_TEXT = {
    "de": "The system \"Check Risk Management Maturity\" allows to define risk management maturity level"
          "in your organisation based on your answers in four different areas:\n"
          "1) Risk-based decision making and integration of risk management into business processes\n"
          "2) Development of a culture of risk management in the organisation\n"
          "3) The organization's risk management unit\n"
          "4) Management of certain types of risks",
    "en": "The system \"Check Risk Management Maturity\" allows to define risk management maturity level"
          "in your organisation based on your answers in four different areas:\n"
          "1) Risk-based decision making and integration of risk management into business processes\n"
          "2) Development of a culture of risk management in the organisation\n"
          "3) The organization's risk management unit\n"
          "4) Management of certain types of risks",
    "ru": "Система \"Check Risk Management Maturity\" позволяет определить уровень зрелости"
          "риск менеджмента в вашей организации на основе Ваших ответов на вопросы в четырех областях:\n"
          "1) Принятия решений с учетом рисков и интеграция управления рисками в бизнес-процессы\n"
          "2) Развитие культуры управления рисками в организации\n"
          "3) Подразделение по управлению рисками в организации\n"
          "4) Управление отдельными видами рисков"
}

FINAL_TEXT = {
    "de": "Vielen Dank für deine Teilnahme! "
          "Sie werden der Ergebnis nach weniger sekunden erhalten",
    "en": "Thank you for your participation! "
          "You will get the result in several seconds",
    "ru": "Большое спасибо за ваше участие! "
          "Вы получите результат через несколько секунд"

}

STOP_TEXT = {
    "de": "Vielen Dank für deine Teilnahme! "
          "Wenn du möchtest würden wir uns über eine Nachricht freuen,"
          " warum du nicht mehr weitermachen willst. Falls du es dir anders"
          " überlegst, kannst du jederzeit wieder teilnehmen, indem du uns eine"
          " Nachricht mit \"/start\" schickst.",
    "en": "Thank you for your participation! If "
          "you want to, we would appreciate a message "
          "why you don't feel like continuing the study. "
          "Anyway, if you change your mind, you can resume "
          "by sending us a message with the word \"/start\".",
    "ru": "Большое спасибо за ваше участие!"
          "Если Вас это не затруднит, сообщите нам почему вы не захотели продолжить"
          "данное исследование, мы будем очень благодарны."
          "Если передумаете просто нажмите \"/start\" "
}

ALL_LEVELS = {
    "de": "The scale of the maturity model has five levels:\n\n"
          "***Advanced***\n"
          "***Basic Plus***\n"
          "***Basic***\n"
          "***Ad Hoc Plus***\n"
          "***Ad Hoc***\n\n"
          "If you want to get information about certain maturity level press it",

    "en": "The scale of the maturity model has five levels:\n\n"
          "***Advanced***\n"
          "***Basic Plus***\n"
          "***Basic***\n"
          "***Ad Hoc Plus***\n"
          "***Ad Hoc***\n\n"
          "If you want to get information about certain maturity level press it",

    "ru": "Шкала модели уровня зрелости содержит пять уровней:\n\n"
          "***Зрелый***\n"
          "***Развивающийся Плюс***\n"
          "***Развивающийся***\n"
          "***Формирующийся Плюс***\n"
          "***Формирующийся***\n\n"
          "Чтобы получить информацию о конкретном уровне зрелости, нажмите на него или напишите его название "
          "в любой момент"
}

MATURITY = {
    "de": "Maturity level of risk management in your organisation is ",
    "en": "Maturity level of risk management in your organisation is ",
    "ru": "Уровень зрелости риск менеджмента в вашей организации "
}

MATURITY_LEVEL = [
    {
        "de": "***Ad Hoc***",
        "en": "***Ad Hoc***",
        "ru": "***Формирующийся***"
    },
    {
        "de": "***Ad Hoc Plus***",
        "en": "***Ad Hoc Plus***",
        "ru": "***Формирующийся Плюс***"
    },
    {
        "de": "***Basic***",
        "en": "***Basic***",
        "ru": "***Развивающийся***"
    },
    {
        "de": "***Basic Plus***",
        "en": "***Basic Plus***",
        "ru": "***Развивающийся Плюс***"
    },
    {
        "de": "***Advanced***",
        "en": "***Advanced***",
        "ru": "***Зрелый***"
    }
]

COMMANDS = {'***Ad Hoc***', '***Формирующийся***', '***Ad Hoc Plus***', '***Формирующийся Плюс***', '***Basic***',
            '***Развивающийся***', '***Развивающийся***', '***Basic Plus***', '***Advanced***', '***Зрелый***'}

DESCRIPTIONS = {
        "***Ad Hoc DE***": "***Ad Hoc***",
        "***Ad Hoc***": "***Ad Hoc***\n\n"
                        "This level is characterized by:\n"
                        "1) Risks are not analysed or analysed after the event;\n"
                        "2) Company employees assess risks intuitively;\n"
                        "3) Changes in strategy are implemented after the risk occurs, rather than preventive;\n"
                        "4) The decisions are made without involving experts in the field of risks;\n"
                        "5) The company does not have tolerance to risks;\n"
                        "6) The organization does not have an approved risk management policy.",

        "***Формирующийся***": "***Формирующийся***\n\n"
                               "Для данного уровня характерно:\n"
                               "1) Полное отсутствие анализа рисков в компании или анализ их постфактум;\n"
                               "2) Сотрудники компании оценивают риски интуитивно;\n"
                               "3) Изменения в стратегии происходят только когда риски "
                               "реализуется и приносит большие потери;\n"
                               "4) Решения принимаются без привлечения экспертов в области рисков;\n"
                               "5) В компании не установлена толерантность к рискам;\n"
                               "6) В организации отсутствует утвержденная политика управления рисками.\n",

        "***Ad Hoc Plus*** DE": "***Ad Hoc Plus***",

        "***Ad Hoc Plus***": "***Ad Hoc Plus***\n\n"
                             "This level is characterized by:\n"
                             "1) Risk analysis is carried out but irregularly;\n"
                             "2) Risk management is not related to the activities of the internal "
                             "audit or internal control of the company;\n"
                             "3) Responsibility for the identification, analysis and management of risks "
                             "is not enshrined in the regulatory documents or assigned to risk managers;\n"
                             "4) Training in risk management for company employees is not carried out;\n"
                             "5) The results of the risk analysis are not documented;\n"
                             "6) There is risk identification only for the main business process;\n",

        "***Формирующийся Плюс***": "***Формирующийся Плюс***\n\n"
                                    "Для данного уровня характерно:\n"
                                    "1) Анализ рисков осуществляется нерегулярно;\n"
                                    "2) Управление рисками не связано с деятельностью отдела внутреннего "
                                    "аудита или внутреннего контроля компании;\n"
                                    "3) Роли и обязанности в рамках процессов управления рисками "
                                    "закреплены за риск-менеджерами;\n"
                                    "4) Ответственность за выявление, анализ и управление рисками не закреплена "
                                    "в уставе, регламентирующих документах, положениях о подразделениях "
                                    "и должностных инструкциях;\n"
                                    "5) Не осуществляется обучение сотрудников компании в области управления рисками\n"
                                    "6) Результаты анализа рисков не докумментируются.\n",

        "***Basic*** DE": "***Basic***",

        "***Basic***": "***Basic***\n\n"
                       "This level is characterized by:\n"
                       "1) Risk analysis is carried out regularly, but this procedure is not connected with "
                       "the actualization of strategic goals and budgets;\n"
                       "2) There are no regulations about the considering the results of risk analysis;\n"
                       "3) There are plans about defining risk-appetite;\n"
                       "4) The results of the risk analysis are not always documented;\n"
                       "5) The risk manager can participate in collegiate bodies but not as a full member;\n"
                       "6) A risk management policy developed and approved by the CEO.\n",

        "***Развивающийся***": "***Развивающийся***\n\n"
                                "Для данного уровня характерно:\n"
                                "1) Анализ рисков проводится регулярно, но данная процедура никак не связана с "
                               "обновлением стратегии или бюджетированием;\n"
                                "2) Нет никакоц регламентации об обязательном рассмотрении "
                               "результатов анализв рисков;\n"
                                "3) В ближайщем будущем планируется ввести и зарегламентировать риск-аппетит;\n"
                                "4) Результаты анализа рисков не всегда документируются;\n"
                                "5) Риск-менеджер может учавствовать в совете директоров, но без права голоса;\n"
                                "6) Разработана политика управления рисками, утвержденная генералььным директором.\n",

        "***Basic PlusDE***": "***Basic Plus***",

        "***Basic Plus***": "***Basic Plus***\n\n"
                            "This level is characterized by:\n"
                            "1) Risks associated with the main business processes of the organization are "
                            "identified, assessed and managed once a year or more often;\n"
                            "2) The organization uses primarily high-quality tools for risk assessment;\n"
                            "3) The results of the risk analysis are documented;\n"
                            "4) Roles and responsibilities within risk management processes are assigned "
                            "to management and risk managers;\n"
                            "5) Responsibility for the identification, analysis and management of risks "
                            "is only enshrined in the policy;\n"
                            "6) Goals, objectives and annual budget are formed based on risk analysis;\n"
                            "7) Key personnel responsible for managing significant risks for the organization "
                            "have been trained over the past two years.\n",

        "***Развивающийся Плюс***": "***Развивающийся Плюс***\n\n"
                                    "Для данного уровня характерно:\n"
                                    "1) Риски связанные с основными бизнес процессами в организации "
                                    "идентифицируются, оцениваются и управляются чаще чем раз в год;\n"
                                    "2) Организация использует современный высоко-качественные "
                                    "инструменты анадиза рисков\n"
                                    "3) Результаты анализа рисков документируются;\n"
                                    "4) Роли и обязанности в рамках процесса управления рисками закреплены "
                                    "за менеджерами и за риск-менеджерами;\n"
                                    "5) Ответственность за выявление, анализ и управление рисками закреплена "
                                    "только в политике/ положении/регламенте по управлению рисками;\n"
                                    "6) Ключевые сотрудники, ответственные за управление существенными "
                                    "для организации рисками, проходили обучение основам управления рисками "
                                    "в течение последнего года.\n",

        "***AdvancedDE***": "***Advanced***",

        "***Advanced***": "***Advanced***\n\n"
                        "This level is characterized by:\n"
                        "1) Risk management tools are integrated directly into planning and budgeting processes,"
                          "risk management is the important part of setting goals and strategy;\n"
                        "2) The significant decisions are taken only after risk analysis;\n"
                        "3) Risk manager is a full member of key collegial bodies of the company;\n"
                        "4) Information on risk management is timely and transparently communicated to all "
                          "stakeholders, including investors, insurance companies, "
                          "government agencies, banks and others;\n"
                        "5) Roles and responsibilities within risk management processes are assigned to the management,"
                          " the board of directors and risk managers;\n"
                        "6) The company uses different methods to analyse different risks.\n",

        "***Зрелый***": "***Зрелый***\n\n"
                        "Для данного уровня характерно:\n"
                        "1) Инструменты риск менеджмента интегриррованы непосредственно в процессы "
                        "бюджетирования и планирования риск менеджмент является неотемлемым "
                        "элементом при составлении стратегии и установки целей;\n"
                        "2) Значительные решения принимаются только после анализы рисков;\n"
                        "3) Риск менеджер является полноправным участником совета директоров;\n"
                        "4) Информация об управлении рисками своевременно и в полном обьеме предоставляется "
                        "всем заинтересованым сторонам, включая инвесторов, банки, страховые компании, государство;\n"
                        "5) Обязаности и ответственность внутри процесса управления рисками закреплена "
                        "за управляющими, советом директоров и риск менеджерами;\n"
                        "6) Компания использует различные инструменты и методы для анализа различных рисков.\n"
}

DESCRIPTIONS_INTRO = {
    "de": "Press the level you want to get information about",
    "en": "Press the level you want to get information about",
    "ru": "Нажмите на уровень зрелости о котором хотите узнать подробно"
}

BACK_BUTTON = {
    "de": "Back to main menu",
    "en": "Back to main menu",
    "ru": "Вернуться в основное меню"
}

KEYBOARD_MENU = [
    {
        "de": "Maturity model levels",
        "en": "Maturity model levels",
        "ru": "Уровни модели зрелости"
    },
    {
        "de": "Personal recommendations",
        "en": "Personal recommendations",
        "ru": "Персональные рекомендации"
    },
    {
        "de": "Start again",
        "en": "Start again",
        "ru": "Начать сначала"
    },
    {
        "de": "Information about system",
        "en": "Information about system",
        "ru": "Информация о системе"
    },
    {
        "de": "Delete data about me",
        "en": "Delete data about me",
        "ru": "Удалить данные обо мне"
    }
]