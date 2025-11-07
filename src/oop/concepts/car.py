from vehicle import Vehicle


# Concrete class Car inheriting from Vehicle
# The Car class inherits from Vehicle and adds 2 new attributes color and transmission.
class Car(Vehicle):
    def __init__(self, brand, model, year, color, transmission):
        super().__init__(brand, model, year)
        self._color = color
        self._transmission = transmission

    # Polymorphism by implementing the drive method differently in the Car class
    def drive(self):
        return f"Driving {self.get_brand()} {self.get_model()} ({self.get_year()}) with {self._transmission} transmission."

    def get_color(self):
        return self._color

    def get_transmission(self):
        return self._transmission