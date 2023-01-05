from domain.questions.text_question import TextQuestion


class Quiz:
    def __init__(self, description: dict = None):
        self.__questions = []
        self.__points = 0
        self.__max_points = 0
        self.__name = ""

        if description:
            self.__load_from_dict(description)

    def __load_from_dict(self, description):
        self.__name = description['name']

        # для каждого вопроса из (вопросов из описания)
        for question in description['questions']:
            # если (тип вопроса) - это "текст"
            if question['type'] == 'text':
                # мои вопросы добавить новый объект текстовый вопрос с параметром описание вопроса
                self.__questions.append(TextQuestion(question))

            # TODO: добавить создание вопросов с выбором варианта

    @property
    def questions(self):
        return tuple(self.__questions)

    @property
    def points(self):
        return self.__points

    @property
    def max_points(self):
        return self.__max_points

    @property
    def name(self):
        return self.__name

    def perform(self):
        print(f"Добро пожаловать в квиз << {self.name} >>")

        for question in self.__questions:
            self.__points += question.perform()
            self.__max_points += question.max_points

        print(f"Вы набрали {self.points} / {self.max_points}")