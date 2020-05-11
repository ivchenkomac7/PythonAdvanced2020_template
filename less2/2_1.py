# Создать класс автомобиля. Описать общие аттрибуты. Создать
# классы легкового автомобиля и грузового. Описать в основном
# классе базовые аттрибуты для автомобилей. Будет плюсом если в
# классах наследниках переопределите методы базового класса.

class Vehicle:
    description = "The class for vehicle"

    def __init__(self, model, vin):
        self._model = model
        self._vin = vin

    def get_model(self):
        return self._model

    def set_model(self, value):
        self._model = value

    def get_vin(self):
        return self._vin

    def set_vin(self, value):
        self._vin = value
