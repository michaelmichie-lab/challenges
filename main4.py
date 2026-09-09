class Treasure:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class Location:
    def __init__(self, name):
        self.name = name
        self.treasures = []

    def add_treasure(self, treasure):
        self.treasures.append(treasure)

    def show_treasures(self):
        print(f"\n--- Treasures at {self.name} ---")
        if not self.treasures:
            print("No treasures available.")
        else:
            for treasure in self.treasures:
                print(f"- {treasure.name} (Value: {treasure.value})")


class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.score = 0

    def collect(self, treasure):
        self.inventory.append(treasure)
        self.score += treasure.value
        print(f"{self.name} collected a {treasure.name} (+{treasure.value} pts)!")

    def show_inventory(self):
        print(f"\n--- {self.name}'s Inventory ---")
        if not self.inventory:
            print("Inventory is empty.")
        else:
            for treasure in self.inventory:
                print(f"- {treasure.name} (Value: {treasure.value})")
        print(f"Total Score: {self.score}")


gold_coin = Treasure("Gold Coin", 100)
diamond = Treasure("Diamond", 500)
ancient_map = Treasure("Ancient Map", 250)

cave = Location("Dark Cave")
beach = Location("Hidden Beach")

cave.add_treasure(gold_coin)
cave.add_treasure(diamond)
beach.add_treasure(ancient_map)

player1 = Player("Amina")
player2 = Player("Liam")

cave.show_treasures()
beach.show_treasures()

player1.collect(gold_coin)
player1.collect(diamond)
player2.collect(ancient_map)

player1.show_inventory()
player2.show_inventory()