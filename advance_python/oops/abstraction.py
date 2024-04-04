from abc import ABC, abstractmethod

class animal(ABC):
    @abstractmethod
    def speak():
        pass

class Dog(animal):
    def speak(self, voice):
        return voice

class Cat( animal):
    def speak(self,voice):
        return voice

class Chakli( animal):
    def speak(self,voice):
        return voice
    
d = Dog()
print(d.speak("bho bho"))

c = Cat()
print(c.speak("meow meow"))