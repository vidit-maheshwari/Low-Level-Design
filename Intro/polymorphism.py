class Car:
    def __init__(self, company, model):
        self.company = company
        self.model = model

    def display_info(self):
        return f"Car: {self.company} {self.model}"
    
    def start_engine(self):
        return "The engine is starting..."
    

class ElectricCar(Car):
    def start_engine(self):
        return "The electric motor is starting silently..."
    
class GasolineCar(Car):
    def start_engine(self):
        return "The gasoline engine is roaring to life..."
    

if __name__ == "__main__":
    electric_car = ElectricCar("Tesla", "Model S")
    gasoline_car = GasolineCar("Ford", "Mustang")

    print(electric_car.display_info())  # Output: Car: Tesla Model S
    print(electric_car.start_engine())  # Output: The electric motor is starting silently...

    print(gasoline_car.display_info())  # Output: Car: Ford Mustang
    print(gasoline_car.start_engine())  # Output: The gasoline engine is roaring to life...