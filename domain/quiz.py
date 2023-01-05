class Quiz:
    def __init__(self, description: dict = None):
        self.__questions = []
        self.__points = None
        self.__max_points = None
        self.__name = None

        if description:
            self.__load_from_dict(description)

    def __load_from_dict(self, description):
        self.__name = description['name']

        # TODO: загрузить вопросы
        # TODO: для каждого вопроса в description['questions'],
        # TODO: создать объект нужного типа и положить его в self.__questions

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

        # TODO: У каждого вопроса вызвать метод perform и прибавить то, что он вернул к self.__points
        # TODO: Максимальный балл за вопроса прибавить к self.__max_points

        # TODO: подвести итоги - сказать какой процент выполнения
