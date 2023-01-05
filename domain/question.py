import abc


class Question(abc.ABC):
    def __init__(self, description: dict = None):
        self._max_points = None

        if description:
            self.__load_from_dict(description)

    def __load_from_dict(self, description):
        self._max_points = description['max_points']

    @property
    def max_points(self):
        return self._max_points

    @abc.abstractmethod
    def perform(self) -> int:
        raise NotImplementedError
