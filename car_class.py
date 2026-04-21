class Car:
    # Constructor
    def __init__(self, brand, model):
        # Attributes (private by convention with underscore)
        self._brand = brand
        self._model = model
        self._speed = 0

    # Method to accelerate
    def accelerate(self, increment):
        self._speed += increment

    # Method to display info
    def display_status(self):
        print(f"{self._brand} is running at {self._speed} km/h.")


if __name__ == "__main__":
    # Creating object of the Car class
    corolla = Car("Toyota", "Corolla")
    mustang = Car("Ford", "Mustang")

    corolla.accelerate(20)
    mustang.accelerate(20)

    # Displaying status of each Car
    corolla.display_status()
    print("-----------------")
    mustang.display_status()
