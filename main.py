class Pet:
    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type
        self.hunger = 5
        self.energy = 5

    def feed(self):
        self.hunger -= 1
        print(f"{self.name} enjoyed the food! Hunger level decreased to {self.hunger}.")

    def play(self):
        self.hunger += 1
        self.energy -= 1
        print(f"{self.name} had fun playing! Hunger is now {self.hunger} and energy is {self.energy}.")

    def status(self):
        print(f"--- {self.name}'s Status ---")
        print(f"Type: {self.animal_type}")
        print(f"Hunger Level: {self.hunger}")
        print(f"Energy Level: {self.energy}\n")



pet1 = Pet("Milo", "Dog")
pet2 = Pet("Luna", "Cat")

pet1.status()
pet2.status()

pet1.feed()
pet1.play()
print()

pet1.status()
pet2.status()