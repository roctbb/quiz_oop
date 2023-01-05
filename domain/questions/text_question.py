from domain.question import Question


class TextQuestion(Question):
    def __init__(self, description):
        super().__init__(description)

        self.__text = description['params']['text']
        self.__correct_answer = description['params']['correct'].lower().strip()

    def perform(self) -> int:
        print(f"Вопрос: {self.__text}")

        answer = input('Ваш ответ: ').lower().strip()

        print("\n")

        if answer == self.__correct_answer:
            return self._max_points
        else:
            return 0
