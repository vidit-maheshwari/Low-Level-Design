class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I am an animal."
    

class Dog(Animal):
    def speak(self):
        return "Woof! I am a dog."
    
class Cat(Animal):
    def speak(self):
        return "Meow! I am a cat."
    

if __name__ == "__main__":
    dog = Dog("Buddy")
    cat = Cat("Whiskers")

    print(dog.speak())  # Output: Woof! I am a dog.
    print(cat.speak())  # Output: Meow! I am a cat.