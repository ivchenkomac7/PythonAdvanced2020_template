# тест

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
