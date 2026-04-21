from enum import Enum


class TrafficLight(Enum):
    RED = 30
    YELLOW = 5
    GREEN = 25

    def next(self) -> "TrafficLight":
        if self == TrafficLight.RED:
            return TrafficLight.GREEN
        elif self == TrafficLight.GREEN:
            return TrafficLight.YELLOW
        else:
            return TrafficLight.RED

    def display(self) -> None:
        print(f"{self.name} ({self.value}s)")


if __name__ == "__main__":
    light = TrafficLight.RED
    for _ in range(6):
        light.display()
        light = light.next()
