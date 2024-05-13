from car import Car


# Main program
# We demonstrate how to create an instance of Car and access its attributes and methods.
if __name__ == "__main__":
    # Create a car object
    my_car = Car("Toyota", "Corolla", 2020, "red", "automatic")

    # Access attributes and methods
    print("Brand:", my_car.get_brand())          # Output: Toyota
    print("Model:", my_car.get_model())          # Output: Corolla
    print("Year:", my_car.get_year())            # Output: 2020
    print("Color:", my_car.get_color())          # Output: red
    print("Transmission:", my_car.get_transmission())  # Output: automatic

    my_car.drive()  # Output: Toyota Corolla (2020) is being driven
