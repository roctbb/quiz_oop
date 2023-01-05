from domain.question import Question

class ChoiceQuestion(Question):
    # TODO: реализовать конструктор, который получает описание вопроса, и инициализирует параметры
    # TODO: реализовать метод perform, который перечатает вопрос, спрашивает ответ и возвращает кол-во баллов

    def __init__(self, desciption):
        super().__init__(desciption)


