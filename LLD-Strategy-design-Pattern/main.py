from abc import ABC, abstractmethod


# Strategy Interface
class FareStrategy(ABC):
    @abstractmethod
    def calculate_fare(self, distance: float, total_time: float) -> float:
        pass


# Concrete Strategy 1
class StandardRide(FareStrategy):
    def __init__(self, base_fare, per_km_rate, per_minute_rate):
        self.base_fare = base_fare
        self.per_km_rate = per_km_rate
        self.per_minute_rate = per_minute_rate

    def calculate_fare(self, distance: float, total_time: float) -> float:
        return (
            self.base_fare
            + (self.per_km_rate * distance)
            + (self.per_minute_rate * total_time)
        )


# Concrete Strategy 2
class PremiumRide(FareStrategy):
    def __init__(self, base_fare, per_km_rate, per_minute_rate):
        self.base_fare = base_fare
        self.per_km_rate = per_km_rate
        self.per_minute_rate = per_minute_rate

    def calculate_fare(self, distance: float, total_time: float) -> float:
        return (
            self.base_fare
            + (self.per_km_rate * distance)
            + (self.per_minute_rate * total_time)
        )


# Context Class
class Ride:
    def __init__(self, fare_strategy: FareStrategy):
        self.fare_strategy = fare_strategy

    def set_fare_strategy(self, fare_strategy: FareStrategy):
        self.fare_strategy = fare_strategy

    def calculate_fare(self, distance: float, total_time: float) -> float:
        return self.fare_strategy.calculate_fare(distance, total_time)


if __name__ == "__main__":
    distance = 10
    total_time = 30

    standard_strategy = StandardRide(base_fare=5, per_km_rate=2, per_minute_rate=0.5)
    premium_strategy = PremiumRide(base_fare=10, per_km_rate=3, per_minute_rate=1)

    ride = Ride(standard_strategy)
    print("Standard Ride Fare:", ride.calculate_fare(distance, total_time))

    ride.set_fare_strategy(premium_strategy)
    print("Premium Ride Fare:", ride.calculate_fare(distance, total_time))