from abc import ABC, abstractmethod


# Define an abstract base class Vehicle with attributes like
# brand, model, and year, along with an abstract method drive.
class Vehicle(ABC):
    def __init__(self, brand, model, year):
        self._brand = brand
        self._model = model
        self._year = year

    # Encapsulate the attributes by using getter methods (get_make, get_model, get_year, get_color)
    def get_brand(self):
        return self._brand

    def get_model(self):
        return self._model

    def get_year(self):
        return self._year

    @abstractmethod
    def drive(self):
        pass
