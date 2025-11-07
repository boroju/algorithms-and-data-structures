import unittest
from vehicle import Vehicle
from car import Car


class TestVehicle(unittest.TestCase):
    def test_vehicle_attributes(self):
        vehicle = Car("Toyota", "Corolla", 2020, "Red", "Automatic")
        self.assertEqual(vehicle.get_brand(), "Toyota")
        self.assertEqual(vehicle.get_model(), "Corolla")
        self.assertEqual(vehicle.get_year(), 2020)
        self.assertEqual(vehicle.get_color(), "Red")
        self.assertEqual(vehicle.get_transmission(), "Automatic")

    def test_drive_method(self):
        vehicle = Car("Toyota", "Corolla", 2020, "Red", "Automatic")
        expected_output = "Driving Toyota Corolla (2020) with Automatic transmission."
        self.assertEqual(vehicle.drive(), expected_output)


if __name__ == "__main__":
    unittest.main()
